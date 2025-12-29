import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import time
from telebot import TeleBot, apihelper
from telebot.types import ChatPermissions
from shared.db import GroupDB


# ===== 基本配置 =====
BOT_TOKEN = "8584329291:AAGi9ST0DMU3Ar_fdE6GKI5EV9-Qk6qzypE"

# Windows + Clash（如需要）
# apihelper.proxy = {
#     "http": "http://127.0.0.1:7899",
#     "https": "http://127.0.0.1:7899",
# }

bot = TeleBot(BOT_TOKEN)
db = GroupDB()

# ===== 参数配置 =====
NEW_USER_LINK_BLOCK_SECONDS = 180  # 新成员3分钟内禁发链接
PUNISH_LEVELS = {
    1: 60,        # 第1次：1分钟
    2: 300,       # 第2次：5分钟
    3: 86400,     # 第3次及以上：24小时
}

# ===== 官方白名单链路 =====
WHITELIST_DOMAINS = [
    "https://1ubox.games",
    "https://t.me/@one1ubox",
    "t.me/your_group",
]


# ===== 工具函数 =====
def contains_link(text: str) -> bool:
    if not text:
        return False
    text = text.lower()
    return any(x in text for x in ["http://", "https://", "t.me/", "www."])


def is_whitelisted_link(text: str) -> bool:
    text = text.lower()
    return any(domain in text for domain in WHITELIST_DOMAINS)


def is_admin(chat_id, user_id) -> bool:
    member = bot.get_chat_member(chat_id, user_id)
    return member.status in ("administrator", "creator")


def get_punish_seconds(count: int) -> int:
    return PUNISH_LEVELS.get(count, 86400)


# ===== 记录入群时间（持久化）=====
@bot.message_handler(content_types=["new_chat_members"])
def record_join(message):
    for user in message.new_chat_members:
        db.record_join(message.chat.id, user.id)


# ===== 防广告主逻辑 =====
@bot.message_handler(func=lambda m: m.chat.type in ["group", "supergroup"])
def anti_spam(message):

    # 忽略 Bot
    if message.from_user.is_bot:
        return

    chat_id = message.chat.id
    user_id = message.from_user.id
    now = int(time.time())

    # 管理员放行
    try:
        if is_admin(chat_id, user_id):
            return
    except Exception:
        return

    # 没有链接直接放行
    if not contains_link(message.text):
        return

    # 白名单链接放行
    if is_whitelisted_link(message.text):
        return

    # ===== 判断是否新成员 =====
    join_time = db.get_join_time(chat_id, user_id)
    is_new_user = join_time and (now - join_time < NEW_USER_LINK_BLOCK_SECONDS)

    # ===== 违规次数累计（持久化）=====
    count = db.add_violation(chat_id, user_id)

    punish_seconds = get_punish_seconds(count)

    try:
        # 删除违规消息
        bot.delete_message(chat_id, message.message_id)

        # 禁言
        bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            permissions=ChatPermissions(can_send_messages=False),
            until_date=now + punish_seconds,
        )

        name = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else message.from_user.first_name
        )

        # 提示文案
        if is_new_user:
            reason = "新成员3分钟内禁止发链接"
        else:
            reason = f"第{count}次违规"

        penalty = (
            f"禁言 {punish_seconds // 60} 分钟"
            if punish_seconds < 3600
            else "禁言 24 小时"
        )

        bot.send_message(
            chat_id,
            f"🚫 {name} 发送链接违规\n原因：{reason}\n处罚：{penalty}",
        )

    except Exception as e:
        print("Anti-spam error:", e)


def main():
    print("Advanced anti-spam bot running...")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
