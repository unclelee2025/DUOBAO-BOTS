from telebot import types
from .utils import is_private
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



PROJECT_NAME = "ONE·1U夺宝"

START_TEXT = (
    "👋 欢迎您！Web3的先驱者：\n\n"
    f"这里是【{PROJECT_NAME}】官方助手\n"
    "用于帮助您了解【ONE·1U夺宝】的玩法流程\n\n"
    "特点：\n"
    "• 无需注册\n"
    "• 各大交易所Web3钱包自主操作，安全可靠\n"
    "• 所有记录SOL链上可查，真实有效\n\n"
    "您的幸运从这里开始👇"
)

NEWBIE_ENTRY_TEXT = (
    "很多第一次接触的用户，主要关心这 4 点👇\n\n"
    "1️⃣ 操作是不是自己完成？\n"
    "2️⃣ 结果怎么产生？\n"
    "3️⃣ 过程是否可验证？\n"
    "4️⃣ 资金是否安全？\n\n"
    "我可以按流程给你简单说明。"
)

FUNDS_TEXT = (
    "🔐 关于资金安全\n\n"
    "• 优先推荐使用币安、欧易等交易所Web3钱包\n"
    "• 钱包永不授权只做登陆和支付使用\n"
    "• 参与资金由链上智能合约托管\n"
    "• 所有参与流程皆能在链上查询到\n\n"
    "简单说：\n"
    "👉 您只是花了1U体验了一次真正的链上公平"
)

RESULT_TEXT = (
    "🎲 关于中奖规则\n\n"
    "• 每轮结果由链上随机数（VRF）生成\n"
    "• 无人工干预\n"
    "• 中奖地址公开，可通过链上查询其交互信息\n\n"
    "链上公平才是ONE追求的Web3精神"
)

FLOW_TEXT = (
    "📄 一次完整流程大致如下：\n\n"
    "1. 打开参与页面\n"
    "2. 选择对应轮次\n"
    "3. 钱包确认操作\n"
    "4. 等待链上结果生成\n"
    "5. 按规则结算\n\n"
    "很多用户会先看一轮再决定"
)

DIRECT_TEXT = (
    "📱 移动端：\n"
    "在币安、欧易等交易所 Web3 钱包的「发现 / DApp」中搜索：\n"
    "👉 1ubox.games\n\n"
    "💻 PC 端：\n"
    "浏览器直接打开：\n"
    "👉 https://1ubox.games\n\n"
    "⚠️ 提示：\n"
    "PC 端参与需提前安装主流 Web3 钱包浏览器插件"
)


READY_TEXT = (
    "👍 明白了\n\n"
    "你可以直接查看当前开放的参与轮次\n"
    "是否参与，完全由你自行决定"
)

NOT_READY_TEXT = (
    "没关系\n\n"
    "如果你只是想了解流程：\n"
    "• 可以先不操作\n"
    "• 只看流程说明\n"
    "• 或进群观摩\n\n"
    "需要的话，我也可以提供钱包入门说明"
)

WALLET_GUIDE_TEXT = (
    "📘 钱包基础说明\n"
    "- 钱包是你自己管理资产的工具，平台不会代管或控制你的资产\n"
    "- 务必保存好助记词/私钥，任何索要助记词的都是诈骗\n"
    "- 只在官方渠道下载钱包应用，避免第三方修改版\n"
    "- 首次使用建议：创建钱包 → 备份助记词 → 小额测试 → 再进行操作\n"
    "- 不熟悉可以先观摩流程或进群交流，再决定是否参与"
)

PAUSE_TEXT = (
    "没关系，你可以先看看流程或群内交流，"
    "等准备好了再回来。"
)

TRUST_BUFFER_TEXT = (
    "ℹ️ 提醒一下\n\n"
    "很多用户的顺序是：\n"
    "1️⃣ 先了解规则\n"
    "2️⃣ 看别人如何操作\n"
    "3️⃣ 再决定是否参与\n\n"
    "你可以完全按自己的节奏来"
)

SUPPORT_TEXT = (
    "你可以直接描述你的问题\n"
    "点击下方按钮联系人工客服\n"
    "（请勿发送私钥或助记词）"
    "\n\n🔍 链上查询：https://solscan.io/"
)

UNKNOWN_TEXT = (
    "我还没识别到你的问题。\n"
    "你可以换个说法，或点击“💬 人工客服”转人工。"
)

RULE_TEXT = (
    "🎲 关于中奖规则\n\n"
    "• 每轮结果由链上随机数（VRF）生成\n"
    "• 无人工干预\n"
    "• 中奖地址公开，可通过链上查询其交互信息\n\n"
    "链上公平才是ONE追求的Web3精神"
)

RECENT_DRAW_URL = "https://1ubox.games/#/find"

GROUP_WELCOME_TEMPLATE = (
    "🎉 欢迎 <b>{name}</b> 加入官方群！\n\n"
    "📌 新成员必读：\n"
    "1) 先私聊引导机器人（点击下方按钮）\n"
    "2) 查看当前夺宝、参与流程\n"
    "3) 不要随便私聊/转账\n\n"
    "⚠️ 管理员不会主动私聊你\n"
    "⚠️ 谨防诈骗"
)


def support_button(cfg):
    support_url = cfg.get("SUPPORT_URL")
    if support_url:
        return types.InlineKeyboardButton("💬 人工客服", url=support_url)
    return types.InlineKeyboardButton("💬 人工客服", callback_data="support_info")


def build_start_menu():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("🔰 新手了解流程", callback_data="start_newbie"),
        types.InlineKeyboardButton("🚀 点击领取幸运", callback_data="start_direct"),
        types.InlineKeyboardButton("📢 官方频道", url="https://t.me/luboxgames"),
    )
    return kb


def build_newbie_menu():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("🔐 资金安全", callback_data="newbie_funds"),
        types.InlineKeyboardButton("🎲 中奖规则", callback_data="newbie_result"),
        types.InlineKeyboardButton("📄 完整流程示意", callback_data="newbie_flow"),
        types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"),
    )
    return kb


def build_next_result_menu():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("下一步：中奖规则", callback_data="newbie_result"),
        types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"),
    )
    return kb


def build_next_flow_menu():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("查看完整流程", callback_data="newbie_flow"),
        types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"),
    )
    return kb


def build_flow_menu(cfg):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("👀 看一轮示例", callback_data="flow_demo"))
    group_url = cfg.get("GROUP_URL")
    if group_url:
        kb.add(types.InlineKeyboardButton("👥 进群看看大家怎么操作", url=group_url))
    kb.add(support_button(cfg))
    kb.add(types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"))
    return kb


def build_direct_menu():
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"))
    return kb


def build_ready_menu(cfg):
    kb = types.InlineKeyboardMarkup(row_width=1)
    app_url = cfg.get("APP_URL")
    group_url = cfg.get("GROUP_URL")
    if app_url:
        kb.add(types.InlineKeyboardButton("🚀 打开参与页面", url=app_url))
    if group_url:
        kb.add(types.InlineKeyboardButton("👥 先去群里看看", url=group_url))
    kb.add(support_button(cfg))
    kb.add(types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"))
    return kb


def build_not_ready_menu(cfg):
    kb = types.InlineKeyboardMarkup(row_width=1)
    group_url = cfg.get("GROUP_URL")
    kb.add(types.InlineKeyboardButton("📘 钱包基础说明", callback_data="wallet_guide"))
    if group_url:
        kb.add(types.InlineKeyboardButton("👥 进群看看", url=group_url))
    kb.add(types.InlineKeyboardButton("⏸ 暂时不操作", callback_data="direct_pause"))
    kb.add(support_button(cfg))
    kb.add(types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"))
    return kb


def build_demo_menu(cfg):
    kb = types.InlineKeyboardMarkup(row_width=1)
    app_url = cfg.get("APP_URL")
    if app_url:
        kb.add(types.InlineKeyboardButton("🚀 打开参与页面", url=app_url))
    kb.add(types.InlineKeyboardButton("🧭 查看最近结果", url=RECENT_DRAW_URL))
    kb.add(support_button(cfg))
    kb.add(types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"))
    return kb


def build_support_back_menu(cfg):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(support_button(cfg))
    kb.add(
        types.InlineKeyboardButton("🔍 链上查询", url="https://solscan.io/")
    )
    kb.add(types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"))
    return kb


def keyword_reply(text, cfg):
    lowered = text.lower()

    def has_any(keywords):
        for key in keywords:
            haystack = lowered if key.isascii() else text
            if key in haystack:
                return True
        return False

    if has_any(["安全吗", "安全", "安全么", "资金安全"]):
        return "所有操作由用户钱包完成，流程链上可查。", None
    if has_any(["能赚吗", "会赚钱吗", "赚钱吗", "赚不赚", "收益", "盈利", "回报","收益率","赚"]):
        return "这是基于规则的参与流程，是否适合你需要自行判断。", None
    if has_any(["会不会跑路", "跑路", "靠谱不", "靠谱吗", "信任","靠谱"]):
        return "项目不代管资产，所有步骤公开在链上。", None
    if has_any(["怎么玩", "怎么参与", "流程", "入门", "新手"]):
        return "我可以按步骤给你说明👇", build_newbie_menu()
    if has_any(["结果", "机制"]):
        return RESULT_TEXT, build_next_flow_menu()
    if has_any(["规则", "规则说明"]):
        return RULE_TEXT, None
    if has_any(["群", "进群", "讨论区", "交流区"]):
        group_url = cfg.get("GROUP_URL")
        if group_url:
            kb = types.InlineKeyboardMarkup(row_width=1)
            kb.add(types.InlineKeyboardButton("👥 看大家怎么玩", url=group_url))
            kb.add(types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"))
            return "你可以先进群看看大家怎么操作。", kb
        return "暂未配置群链接。", None
    if has_any(["钱包", "钱包基础", "绑定"]):
        bind_url = cfg.get("BIND_URL")
        if bind_url:
            kb = types.InlineKeyboardMarkup(row_width=1)
            kb.add(types.InlineKeyboardButton("📘 钱包基础说明", url=bind_url))
            kb.add(types.InlineKeyboardButton("返回主菜单", callback_data="menu_back"))
            return "这里是钱包基础说明。", kb
        return "暂未配置钱包说明链接。", None
    return None, None


def register(bot, cfg, db):
    """
    Register handlers for guide bot.
    """

    guide_username = None
    guide_url = None
    try:
        me = bot.get_me()
        if me.username:
            guide_username = f"@{me.username}"
            guide_url = f"https://t.me/{me.username}"
    except Exception:
        pass
    official_channel = cfg.get("CHANNEL_URL") or "https://t.me/luboxgames"

    @bot.message_handler(content_types=["new_chat_members"])
    def welcome_new_member(message):
        if message.chat.type == "private":
            return

        for user in message.new_chat_members:
            if user.is_bot:
                continue

            name = user.first_name or user.username or "朋友"
            text = GROUP_WELCOME_TEMPLATE.format(name=name)

            kb = types.InlineKeyboardMarkup()
            if guide_url:
                kb.add(
                    types.InlineKeyboardButton(
                        "私聊向导",
                        url=guide_url,
                    )
                )
            else:
                kb.add(
                    types.InlineKeyboardButton(
                        "私聊向导",
                        callback_data="menu_back",
                    )
                )
            kb.add(
                types.InlineKeyboardButton(
                    "官方频道",
                    url=official_channel,
                )
            )

            bot.send_message(
                message.chat.id,
                text,
                reply_markup=kb,
                parse_mode="HTML",
            )


    def send_start(chat_id, text=None):
        bot.send_message(
            chat_id,
            text or START_TEXT,
            reply_markup=build_start_menu(),
        )

    @bot.message_handler(commands=["start", "menu"])
    def start(msg):
        if not is_private(msg.chat.type):
            return
        send_start(msg.chat.id)

    @bot.message_handler(commands=["rule"])
    def rule_cmd(msg):
        if not is_private(msg.chat.type):
            return
        bot.send_message(msg.chat.id, RULE_TEXT, reply_markup=build_support_back_menu(cfg))

    @bot.message_handler(commands=["last"])
    def last_cmd(msg):
        if not is_private(msg.chat.type):
            return
        bot.send_message(
            msg.chat.id,
            f"你可以查看最近结果：{RECENT_DRAW_URL}",
            reply_markup=build_support_back_menu(cfg),
        )

    @bot.message_handler(commands=["help", "support"])
    def support_cmd(msg):
        if not is_private(msg.chat.type):
            return
        bot.send_message(msg.chat.id, SUPPORT_TEXT, reply_markup=build_support_back_menu(cfg))

    @bot.callback_query_handler(func=lambda c: True)
    def callback(c):
        if not is_private(c.message.chat.type):
            return
        bot.answer_callback_query(c.id)

        data = c.data

        if data == "menu_back":
            send_start(c.message.chat.id)
            return

        if data == "start_newbie":
            bot.send_message(c.message.chat.id, NEWBIE_ENTRY_TEXT, reply_markup=build_newbie_menu())
            return

        if data == "newbie_funds":
            bot.send_message(c.message.chat.id, FUNDS_TEXT, reply_markup=build_next_result_menu())
            return

        if data == "newbie_result":
            bot.send_message(c.message.chat.id, RESULT_TEXT, reply_markup=build_next_flow_menu())
            return
        
        if data == "newbie_flow":
            bot.send_photo(
                c.message.chat.id,
                photo=open(os.path.join(BASE_DIR, "swipe_2.png"), "rb"),
                caption="📄 完整参与流程示意图",
                reply_markup=build_flow_menu(cfg),
            )
            return

        if data == "flow_demo":
            bot.send_video(
                c.message.chat.id,
                video=open(os.path.join(BASE_DIR, "flow_demo.mp4"), "rb"),
                caption=("🎥 一轮完整操作示例\n\n"),
                reply_markup=build_demo_menu(cfg),
            )
            return

        if data == "start_direct":
            bot.send_message(c.message.chat.id, DIRECT_TEXT, reply_markup=build_direct_menu())
            return

        if data == "direct_ready":
            bot.send_message(
                c.message.chat.id,
                f"{READY_TEXT}\n\n{TRUST_BUFFER_TEXT}",
                reply_markup=build_ready_menu(cfg),
            )
            return

        if data == "direct_not_ready":
            bot.send_message(
                c.message.chat.id,
                NOT_READY_TEXT,
                reply_markup=build_not_ready_menu(cfg),
            )
            return

        if data == "direct_pause":
            bot.send_message(
                c.message.chat.id,
                f"{PAUSE_TEXT}\n\n{TRUST_BUFFER_TEXT}",
                reply_markup=build_support_back_menu(cfg),
            )
            return

        if data == "wallet_guide":
            bot.send_message(
                c.message.chat.id,
                WALLET_GUIDE_TEXT,
                reply_markup=build_support_back_menu(cfg),
            )
            return

        if data == "support_info":
            bot.send_message(
                c.message.chat.id,
                SUPPORT_TEXT,
                reply_markup=build_support_back_menu(cfg),
            )
            return

    @bot.message_handler(func=lambda msg: is_private(msg.chat.type), content_types=["text"])
    def handle_private_text(msg):
        text = (msg.text or "").strip()
        if not text:
            send_start(msg.chat.id)
            return

        reply_text, reply_markup = keyword_reply(text, cfg)
        if reply_text:
            bot.send_message(
                msg.chat.id,
                reply_text,
                reply_markup=reply_markup or build_support_back_menu(cfg),
            )
            return

        bot.send_message(
            msg.chat.id,
            UNKNOWN_TEXT,
            reply_markup=build_support_back_menu(cfg),
        )
