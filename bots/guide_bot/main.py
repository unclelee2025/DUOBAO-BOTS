import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from telebot import TeleBot, apihelper, types
from .config import get_config
from shared.db import GroupDB
from .handlers import register

# 👉 Windows + Clash 代理（你现在一定要加）
# apihelper.proxy = {
#     'http': 'http://127.0.0.1:7899',
#     'https': 'http://127.0.0.1:7899'
# }

cfg = get_config()
bot = TeleBot(cfg["BOT_TOKEN"])
db = GroupDB()
register(bot, cfg, db)

# 设置命令菜单，方便用户快速点击
bot.set_my_commands(
    [
        types.BotCommand("start", "开始/打开菜单"),
        types.BotCommand("help", "人工客服"),
        types.BotCommand("rule", "查看中奖规则"),
        types.BotCommand("last", "最近开奖"),
    ]
)

def main():
    print("Guide bot running...")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
