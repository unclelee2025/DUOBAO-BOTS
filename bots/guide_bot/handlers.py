import os
import re

from telebot import types
from .utils import is_private

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_LANGUAGE = "zh"
CHAT_LANGUAGE_PREFERENCE = {}

RECENT_DRAW_URL = "https://1ubox.games/#/find"

LOCALES = {
    "zh": {
        "project_name": "ONE·1U夺宝",
        "text": {
            "start": (
                "👋 欢迎您！Web3 的先驱：\n\n"
                "这里是【{project_name}】官方助手\n"
                "用于帮助您了解 ONE·1U 夺宝的玩法流程\n\n"
                "特点：\n"
                "• 无需注册\n"
                "• 各大交易所 Web3 钱包自主操作，安全可靠\n"
                "• 所有记录 SOL 链上可查，真实有效\n\n"
                "您的好运从这里开始 🎉"
            ),
            "newbie_entry": (
                "很多第一次接触的用户，主要关心这 4 点👇\n\n"
                "1️⃣ 操作是否自己完成？\n"
                "2️⃣ 结果怎么产生？\n"
                "3️⃣ 流程是否可验证？\n"
                "4️⃣ 资金是否安全？\n\n"
                "我可以按流程给你简单说明 👍"
            ),
            "funds": (
                "🔐 关于资金安全\n\n"
                "• 优先推荐使用币安、欧易等交易所的 Web3 钱包\n"
                "• 钱包永不授权其他人，只有自己操作登录与支付\n"
                "• 参与资金由链上智能合约托管，平台不代管资产\n"
                "• 所有参与步骤均可在链上查询\n\n"
                "简单说：👍 你只是花一次 U 体验一次公平链上流程"
            ),
            "result": (
                "🎲 关于中奖规则\n\n"
                "• 每轮结果由链上随机数 (VRF) 生成\n"
                "• 无人工干预\n"
                "• 中奖地址公开，可在链上查询交互信息\n\n"
                "链上公平才是 ONE 追求的 Web3 精神"
            ),
            "flow": (
                "📤 一次完整流程大致如下：\n\n"
                "1. 打开参与页面\n"
                "2. 选择对应轮次\n"
                "3. 钱包确认操作\n"
                "4. 等待链上结果生成\n"
                "5. 按规则结算\n\n"
                "很多用户会先看一轮再决定"
            ),
            "direct": (
                "📱 移动端：\n"
                "在币安、欧易等交易所 Web3 钱包的 DApp 浏览器中搜索：\n"
                "➡️ 1ubox.games\n\n"
                "🖥️ PC 端：\n"
                "浏览器直接打开：https://1ubox.games\n\n"
                "✳️ 提示：PC 端参与需要提前安装主流 Web3 钱包浏览器插件"
            ),
            "ready": (
                "👍 明白了\n\n"
                "你可以直接查看当前开放的参与轮次\n"
                "是否参与，完全由你自行决定"
            ),
            "not_ready": (
                "没关系\n\n"
                "如果你只是想了解流程：\n"
                "• 可以先不操作\n"
                "• 只看流程说明\n"
                "• 或进群交流\n\n"
                "需要的时候，我也可以提供钱包入门说明"
            ),
            "wallet_guide": (
                "🛡️ 钱包基础说明\n"
                "- 钱包是你自己管理资产的工具，平台不代管也不控制\n"
                "- 一定要保存好助记词/私钥，任何索要都是诈骗\n"
                "- 仅从官网渠道下载钱包应用，避免第三方篡改\n"
                "- 首次使用建议：创建钱包 → 备份助记词 → 小额测试 → 再操作\n"
                "- 不熟悉可以先看流程或进群交流，再决定是否参与"
            ),
            "pause": (
                "没关系\n\n"
                "你可以先看看流程或在群里交流，等准备好了再回来"
            ),
            "trust_buffer": (
                "🕰️ 提醒一下\n\n"
                "很多用户的顺序是：\n"
                "1️⃣ 先了解规则\n"
                "2️⃣ 看别人怎么玩\n"
                "3️⃣ 再决定是否参与\n\n"
                "你可以完全按照自己的节奏来"
            ),
            "support": (
                "你可以直接描述你的问题\n"
                "点击下方按钮联系人工客服（请勿发送助记词或口令）\n\n"
                "🧾 链上查询：https://solscan.io/"
            ),
            "unknown": (
                "我还没识别到你的问题。\n"
                "你可以换个说法，或点击“📞 人工客服”转人工"
            ),
            "rule": (
                "🎲 关于中奖规则\n\n"
                "• 每轮结果由链上随机数 (VRF) 生成\n"
                "• 无人工干预\n"
                "• 中奖地址公开，可在链上查询交互信息\n\n"
                "链上公平才是 ONE 追求的 Web3 精神"
            ),
            "group_welcome": (
                "🎉 欢迎 <b>{name}</b> 加入官方群！\n\n"
                "🍀 新成员必读：\n"
                "1) 先私聊引导机器人（点击下方按钮）\n"
                "2) 查看当前夺宝与参与流程\n"
                "3) 不要随便私聊/转账\n\n"
                "⚠️ 管理员不会主动私聊你\n"
                "⚠️ 谨防诈骗"
            ),
            "safety_note": (
                "所有操作由用户钱包完成，流程链上可查，真实有效"
            ),
            "profit_note": (
                "这是基于规则的参与流程，是否适合你需要你自己判断"
            ),
            "trust_note": (
                "项目不代管资产，所有步骤公开、链上可查"
            ),
            "community_prompt": (
                "你可以先进群看看大家怎么操作，再决定是否参与"
            ),
            "community_missing": (
                "暂未配置群链接，稍后再试"
            ),
            "wallet_prompt": (
                "这是钱包基础说明，点击下方按钮查看"
            ),
            "wallet_prompt_no_link": (
                "暂未配置钱包说明链接"
            ),
            "last_result": (
                "你可以查看最近结果：{url}"
            ),
        },
        "buttons": {
            "start_newbie": "👀 新手了解流程",
            "start_direct": "🎯 点击领取幸福",
            "official_channel": "📣 官方频道",
            "newbie_funds": "🔐 资金安全",
            "newbie_result": "🎲 中奖规则",
            "newbie_flow": "📤 完整流程示意",
            "menu_back": "返回主菜单",
            "next_result": "下一步：中奖规则",
            "next_flow": "查看完整流程",
            "flow_demo": "👍 看一轮示例",
            "community_view": "👥 进群看看大家怎么操作",
            "ready_start": "🚀 打开参与页面",
            "not_ready_wallet": "🛡️ 钱包基础说明",
            "not_ready_pause": "⏳ 暂时不操作",
            "demo_recent": "🧾 查看最近结果",
            "support_chain": "🔍 链上查询",
            "support": "📞 人工客服",
            "private_guide": "💬 私聊向导",
        },
        "captions": {
            "flow_photo": "📤 完整参与流程示意图",
            "flow_video": "🎥 一轮完整操作示例",
        },
    },
    "en": {
        "project_name": "ONE·1U Treasure",
        "text": {
            "start": (
                "👋 Welcome, pioneers of Web3:\n\n"
                "This is the official helper for [{project_name}]\n"
                "Built to guide you through the ONE·1U Treasure participation flow\n\n"
                "Highlights:\n"
                "• No registration required\n"
                "• Use your own Web3 wallet on major exchanges for self-custody, it's safe\n"
                "• Every record is verifiable on Solana\n\n"
                "Good luck starts from here 🎉"
            ),
            "newbie_entry": (
                "Many first-time participants mainly care about these 4 points 👇\n\n"
                "1️⃣ Is the action already completed by myself?\n"
                "2️⃣ How are the results generated?\n"
                "3️⃣ Can the process be verified?\n"
                "4️⃣ Is the money safe?\n\n"
                "I can walk you through the flow step by step 👍"
            ),
            "funds": (
                "🔐 About fund safety\n\n"
                "• We recommend using Web3 wallets inside Binance, OKX, or other major exchanges\n"
                "• The wallet never authorizes others, only you confirm login and payments\n"
                "• Participation funds are managed by on-chain smart contracts, the platform does not custody assets\n"
                "• Every step is visible and verifiable on-chain\n\n"
                "In short: 👍 you just experience a fair on-chain flow with a single U"
            ),
            "result": (
                "🎲 About prize rules\n\n"
                "• Each round result is generated on-chain by a random number (VRF)\n"
                "• No manual intervention\n"
                "• Winning addresses are published and chain interactions can be checked\n\n"
                "On-chain fairness is the Web3 spirit ONE is pursuing"
            ),
            "flow": (
                "📤 A full participation flow looks roughly like this:\n\n"
                "1. Open the participation page\n"
                "2. Choose the target round\n"
                "3. Confirm the operation with your wallet\n"
                "4. Wait for the on-chain result\n"
                "5. Settle according to the rules\n\n"
                "Many users watch one round first before making a decision"
            ),
            "direct": (
                "📱 Mobile:\n"
                "Use the DApp browser inside Web3 wallets on Binance, OKX, etc., and search for:\n"
                "➡️ 1ubox.games\n\n"
                "🖥️ Desktop:\n"
                "Open your browser and visit https://1ubox.games\n\n"
                "✳️ Note: Desktop participation requires installing a mainstream Web3 wallet browser extension first"
            ),
            "ready": (
                "👍 Got it\n\n"
                "You can directly check the currently open rounds\n"
                "Whether to join is completely up to you"
            ),
            "not_ready": (
                "No problem\n\n"
                "If you just want to learn about the flow:\n"
                "• You can wait before taking action\n"
                "• Just read the flow guide\n"
                "• Or join the community to chat\n\n"
                "I can also share wallet entry tips when needed"
            ),
            "wallet_guide": (
                "🛡️ Wallet basics\n"
                "- A wallet is the tool you control to manage your assets; the platform doesn't custody or control them\n"
                "- Always keep your mnemonic/private key safe; any request for them is a scam\n"
                "- Only download wallet apps via official channels to avoid tampered versions\n"
                "- For first-time use: create a wallet → backup the mnemonic → test with a small amount → then proceed\n"
                "- If you're unsure, watch the flow or chat in the group before deciding whether to participate"
            ),
            "pause": (
                "No worries\n\n"
                "You can browse the flow or exchange in the group first, then come back when you're ready"
            ),
            "trust_buffer": (
                "🕰️ A quick heads-up\n\n"
                "Many users follow this order:\n"
                "1️⃣ Understand the rules\n"
                "2️⃣ See how others operate\n"
                "3️⃣ Decide whether to participate\n\n"
                "Feel free to take your time"
            ),
            "support": (
                "Describe your issue directly\n"
                "Click the button below to contact human support (do not send mnemonics or passwords)\n\n"
                "🧾 On-chain lookup: https://solscan.io/"
            ),
            "unknown": (
                "I haven't recognized your question yet.\n"
                "Try rephrasing it or tap “📞 Human support” to speak with someone"
            ),
            "rule": (
                "🎲 About prize rules\n\n"
                "• Each round result is generated on-chain by a random number (VRF)\n"
                "• No manual intervention\n"
                "• Winning addresses are published and chain interactions can be checked\n\n"
                "On-chain fairness is the Web3 spirit ONE is pursuing"
            ),
            "group_welcome": (
                "🎉 Welcome <b>{name}</b> to the official group!\n\n"
                "🍀 New member essentials:\n"
                "1) Private message the guide bot (tap the button below)\n"
                "2) Check the current treasure draw and participation flow\n"
                "3) Do not transfer or chat privately unless you initiate it\n\n"
                "⚠️ Admins will not proactively DM you\n"
                "⚠️ Stay alert for scams"
            ),
            "safety_note": (
                "All operations happen through your wallet; the flow is verifiable on-chain and fully transparent"
            ),
            "profit_note": (
                "This is a rules-based participation process; decide for yourself if it fits you"
            ),
            "trust_note": (
                "The project doesn't custody assets; every step is open and traceable on-chain"
            ),
            "community_prompt": (
                "Feel free to join the community to see how others operate before deciding"
            ),
            "community_missing": (
                "Community link is not configured yet, please try again later"
            ),
            "wallet_prompt": (
                "Here is the wallet basics guide"
            ),
            "wallet_prompt_no_link": (
                "Wallet guide link is not configured"
            ),
            "last_result": (
                "You can check the latest results here: {url}"
            ),
        },
        "buttons": {
            "start_newbie": "👀 Beginner flow",
            "start_direct": "🎯 Claim the prize",
            "official_channel": "📣 Official channel",
            "newbie_funds": "🔐 Fund safety",
            "newbie_result": "🎲 Prize rules",
            "newbie_flow": "📤 Full flow guide",
            "menu_back": "Back to main menu",
            "next_result": "Next: Prize rules",
            "next_flow": "View the full flow",
            "flow_demo": "👍 Watch an example",
            "community_view": "👥 Join the community",
            "ready_start": "🚀 Open participation page",
            "not_ready_wallet": "🛡️ Wallet basics",
            "not_ready_pause": "⏳ Pause for now",
            "demo_recent": "🧾 View latest draws",
            "support_chain": "🔍 On-chain lookup",
            "support": "📞 Human support",
            "private_guide": "💬 Chat with the guide",
        },
        "captions": {
            "flow_photo": "📤 Illustration of a complete participation flow",
            "flow_video": "🎥 Demonstration of a full round",
        },
    },
}


def get_locale(lang: str) -> dict:
    return LOCALES.get(lang, LOCALES[DEFAULT_LANGUAGE])


def format_text(lang: str, key: str, **kwargs) -> str:
    locale = get_locale(lang)
    template = locale["text"].get(key) or LOCALES[DEFAULT_LANGUAGE]["text"].get(key, "")
    format_kwargs = {"project_name": locale["project_name"]}
    format_kwargs.update(kwargs)
    return template.format(**format_kwargs)


def get_buttons(lang: str) -> dict:
    return get_locale(lang)["buttons"]


def get_captions(lang: str) -> dict:
    return get_locale(lang)["captions"]


def language_code_to_lang(language_code: str | None) -> str | None:
    if not language_code:
        return None
    normalized = language_code.lower()
    if normalized.startswith("en"):
        return "en"
    if normalized.startswith("zh"):
        return "zh"
    return None


def detect_language_from_text(text: str | None) -> str | None:
    if not text:
        return None
    stripped = text.strip()
    if not stripped:
        return None
    if stripped.startswith("/"):
        return None
    english_chars = len(re.findall(r"[A-Za-z]", stripped))
    cjk_chars = len(re.findall(r"[\u4e00-\u9fff]", stripped))
    if english_chars > cjk_chars:
        return "en"
    if cjk_chars > english_chars:
        return "zh"
    lowered = stripped.lower()
    for keyword in ("english", "guide", "help", "how", "participate"):
        if keyword in lowered:
            return "en"
    return None


def resolve_language(text: str | None, language_code: str | None) -> str:
    detected = detect_language_from_text(text)
    if detected:
        return detected
    from_code = language_code_to_lang(language_code)
    if from_code:
        return from_code
    return DEFAULT_LANGUAGE


def set_chat_language(chat_id: int, lang: str) -> None:
    if not chat_id:
        return
    CHAT_LANGUAGE_PREFERENCE[chat_id] = lang


def get_chat_language(chat_id: int, fallback_user=None) -> str:
    stored = CHAT_LANGUAGE_PREFERENCE.get(chat_id)
    if stored:
        return stored
    if fallback_user:
        from_code = language_code_to_lang(getattr(fallback_user, "language_code", None))
        if from_code:
            return from_code
    return DEFAULT_LANGUAGE


def update_chat_language_from_message(chat_id: int, text: str | None, language_code: str | None) -> str:
    if text:
        stripped = text.strip()
        if stripped.startswith("/"):
            stored = CHAT_LANGUAGE_PREFERENCE.get(chat_id)
            if stored:
                return stored
    lang = resolve_language(text or "", language_code)
    set_chat_language(chat_id, lang)
    return lang


def support_buttons(cfg: dict, lang: str) -> list[types.InlineKeyboardButton]:
    buttons = get_buttons(lang)
    urls = [cfg.get("SUPPORT_URL_1"), cfg.get("SUPPORT_URL_2")]
    urls = [url for url in urls if url]
    if urls:
        if len(urls) == 1:
            return [types.InlineKeyboardButton(buttons["support"], url=urls[0])]
        labels = [f"{buttons['support']} 1", f"{buttons['support']} 2"]
        return [
            types.InlineKeyboardButton(label, url=url)
            for label, url in zip(labels, urls)
        ]
    support_url = cfg.get("SUPPORT_URL")
    if support_url:
        return [types.InlineKeyboardButton(buttons["support"], url=support_url)]
    return [types.InlineKeyboardButton(buttons["support"], callback_data="support_info")]


def add_support_buttons(kb: types.InlineKeyboardMarkup, cfg: dict, lang: str) -> None:
    for button in support_buttons(cfg, lang):
        kb.add(button)


def build_start_menu(lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton(buttons["start_newbie"], callback_data="start_newbie"),
        types.InlineKeyboardButton(buttons["start_direct"], callback_data="start_direct"),
        types.InlineKeyboardButton(buttons["official_channel"], url="https://t.me/luboxgames"),
    )
    return kb


def build_newbie_menu(lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton(buttons["newbie_funds"], callback_data="newbie_funds"),
        types.InlineKeyboardButton(buttons["newbie_result"], callback_data="newbie_result"),
        types.InlineKeyboardButton(buttons["newbie_flow"], callback_data="newbie_flow"),
        types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"),
    )
    return kb


def build_next_result_menu(lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton(buttons["next_result"], callback_data="newbie_result"),
        types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"),
    )
    return kb


def build_next_flow_menu(lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton(buttons["next_flow"], callback_data="newbie_flow"),
        types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"),
    )
    return kb


def build_flow_menu(cfg: dict, lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton(buttons["flow_demo"], callback_data="flow_demo"))
    group_url = cfg.get("GROUP_URL")
    if group_url:
        kb.add(types.InlineKeyboardButton(buttons["community_view"], url=group_url))
    add_support_buttons(kb, cfg, lang)
    kb.add(types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"))
    return kb


def build_direct_menu(lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"))
    return kb


def build_ready_menu(cfg: dict, lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    app_url = cfg.get("APP_URL")
    group_url = cfg.get("GROUP_URL")
    if app_url:
        kb.add(types.InlineKeyboardButton(buttons["ready_start"], url=app_url))
    if group_url:
        kb.add(types.InlineKeyboardButton(buttons["community_view"], url=group_url))
    add_support_buttons(kb, cfg, lang)
    kb.add(types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"))
    return kb


def build_not_ready_menu(cfg: dict, lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    group_url = cfg.get("GROUP_URL")
    kb.add(types.InlineKeyboardButton(buttons["not_ready_wallet"], callback_data="wallet_guide"))
    if group_url:
        kb.add(types.InlineKeyboardButton(buttons["community_view"], url=group_url))
    kb.add(types.InlineKeyboardButton(buttons["not_ready_pause"], callback_data="direct_pause"))
    add_support_buttons(kb, cfg, lang)
    kb.add(types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"))
    return kb


def build_demo_menu(cfg: dict, lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    app_url = cfg.get("APP_URL")
    if app_url:
        kb.add(types.InlineKeyboardButton(buttons["ready_start"], url=app_url))
    kb.add(types.InlineKeyboardButton(buttons["demo_recent"], url=RECENT_DRAW_URL))
    add_support_buttons(kb, cfg, lang)
    kb.add(types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"))
    return kb


def build_support_back_menu(cfg: dict, lang: str) -> types.InlineKeyboardMarkup:
    buttons = get_buttons(lang)
    kb = types.InlineKeyboardMarkup(row_width=1)
    add_support_buttons(kb, cfg, lang)
    kb.add(types.InlineKeyboardButton(buttons["support_chain"], url="https://solscan.io/"))
    kb.add(types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"))
    return kb


def keyword_reply(text: str, cfg: dict, lang: str):
    lowered = text.lower()
    buttons = get_buttons(lang)

    def has_any(keywords) -> bool:
        for key in keywords:
            haystack = lowered if key.isascii() else text
            if key in haystack:
                return True
        return False

    if has_any(["安全", "资金安全", "safe", "security", "protection"]):
        return format_text(lang, "safety_note"), None
    if has_any([
        "能赚", "收益", "利润", "赚", "利益", "profit", "earn", "win", "reward", "return"
    ]):
        return format_text(lang, "profit_note"), None
    if has_any(["跑路", "信任", "托管", "trust", "custody", "control"]):
        return format_text(lang, "trust_note"), None
    if has_any([
        "怎么", "流程", "入门", "新手", "how", "process", "guide", "steps", "entry", "join"
    ]):
        return format_text(lang, "newbie_entry"), build_newbie_menu(lang)
    if has_any(["结果", "机制", "result", "mechanism", "payout"]):
        return format_text(lang, "result"), build_next_flow_menu(lang)
    if has_any(["规则", "rule", "rules"]):
        return format_text(lang, "rule"), None
    if has_any(["群", "交流", "group", "community", "chat", "discussion"]):
        group_url = cfg.get("GROUP_URL")
        if group_url:
            kb = types.InlineKeyboardMarkup(row_width=1)
            kb.add(types.InlineKeyboardButton(buttons["community_view"], url=group_url))
            kb.add(types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"))
            return format_text(lang, "community_prompt"), kb
        return format_text(lang, "community_missing"), None
    if has_any(["钱包", "绑定", "wallet", "bind", "setup"]):
        bind_url = cfg.get("BIND_URL")
        if bind_url:
            kb = types.InlineKeyboardMarkup(row_width=1)
            kb.add(types.InlineKeyboardButton(buttons["not_ready_wallet"], url=bind_url))
            kb.add(types.InlineKeyboardButton(buttons["menu_back"], callback_data="menu_back"))
            return format_text(lang, "wallet_prompt"), kb
        return format_text(lang, "wallet_prompt_no_link"), None
    return None, None


def register(bot, cfg: dict, db):
    guide_url = None
    try:
        me = bot.get_me()
        if me.username:
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

            name = user.first_name or user.username or "好友"
            lang = language_code_to_lang(user.language_code) or DEFAULT_LANGUAGE
            text = format_text(lang, "group_welcome", name=name)

            kb = types.InlineKeyboardMarkup()
            buttons = get_buttons(lang)
            if guide_url:
                kb.add(
                    types.InlineKeyboardButton(buttons["private_guide"], url=guide_url)
                )
            else:
                kb.add(
                    types.InlineKeyboardButton(buttons["private_guide"], callback_data="menu_back")
                )
            kb.add(
                types.InlineKeyboardButton(buttons["official_channel"], url=official_channel)
            )

            bot.send_message(
                message.chat.id,
                text,
                reply_markup=kb,
                parse_mode="HTML",
            )

    def send_start(chat_id: int, lang: str, text: str | None = None):
        bot.send_message(
            chat_id,
            text or format_text(lang, "start"),
            reply_markup=build_start_menu(lang),
        )

    @bot.message_handler(commands=["start", "menu"])
    def start(msg):
        if not is_private(msg.chat.type):
            return
        lang = update_chat_language_from_message(msg.chat.id, msg.text, msg.from_user.language_code)
        send_start(msg.chat.id, lang)

    @bot.message_handler(commands=["rule"])
    def rule_cmd(msg):
        if not is_private(msg.chat.type):
            return
        lang = update_chat_language_from_message(msg.chat.id, msg.text, msg.from_user.language_code)
        bot.send_message(
            msg.chat.id,
            format_text(lang, "rule"),
            reply_markup=build_support_back_menu(cfg, lang),
        )

    @bot.message_handler(commands=["last"])
    def last_cmd(msg):
        if not is_private(msg.chat.type):
            return
        lang = update_chat_language_from_message(msg.chat.id, msg.text, msg.from_user.language_code)
        bot.send_message(
            msg.chat.id,
            format_text(lang, "last_result", url=RECENT_DRAW_URL),
            reply_markup=build_support_back_menu(cfg, lang),
        )

    @bot.message_handler(commands=["help", "support"])
    def support_cmd(msg):
        if not is_private(msg.chat.type):
            return
        lang = update_chat_language_from_message(msg.chat.id, msg.text, msg.from_user.language_code)
        bot.send_message(
            msg.chat.id,
            format_text(lang, "support"),
            reply_markup=build_support_back_menu(cfg, lang),
        )

    @bot.callback_query_handler(func=lambda c: True)
    def callback(c):
        if not is_private(c.message.chat.type):
            return
        bot.answer_callback_query(c.id)
        lang = get_chat_language(c.message.chat.id, fallback_user=c.from_user)
        data = c.data

        if data == "menu_back":
            send_start(c.message.chat.id, lang)
            return

        if data == "start_newbie":
            bot.send_message(
                c.message.chat.id,
                format_text(lang, "newbie_entry"),
                reply_markup=build_newbie_menu(lang),
            )
            return

        if data == "newbie_funds":
            bot.send_message(
                c.message.chat.id,
                format_text(lang, "funds"),
                reply_markup=build_next_result_menu(lang),
            )
            return

        if data == "newbie_result":
            bot.send_message(
                c.message.chat.id,
                format_text(lang, "result"),
                reply_markup=build_next_flow_menu(lang),
            )
            return

        if data == "newbie_flow":
            with open(os.path.join(BASE_DIR, "swipe_2.png"), "rb") as photo:
                bot.send_photo(
                    c.message.chat.id,
                    photo=photo,
                    caption=get_captions(lang)["flow_photo"],
                    reply_markup=build_flow_menu(cfg, lang),
                )
            return

        if data == "flow_demo":
            with open(os.path.join(BASE_DIR, "flow_demo.mp4"), "rb") as video:
                bot.send_video(
                    c.message.chat.id,
                    video=video,
                    caption=get_captions(lang)["flow_video"],
                    reply_markup=build_demo_menu(cfg, lang),
                )
            return

        if data == "start_direct":
            bot.send_message(
                c.message.chat.id,
                format_text(lang, "direct"),
                reply_markup=build_direct_menu(lang),
            )
            return

        if data == "direct_ready":
            bot.send_message(
                c.message.chat.id,
                f"{format_text(lang, 'ready')}\n\n{format_text(lang, 'trust_buffer')}",
                reply_markup=build_ready_menu(cfg, lang),
            )
            return

        if data == "direct_not_ready":
            bot.send_message(
                c.message.chat.id,
                format_text(lang, "not_ready"),
                reply_markup=build_not_ready_menu(cfg, lang),
            )
            return

        if data == "direct_pause":
            bot.send_message(
                c.message.chat.id,
                f"{format_text(lang, 'pause')}\n\n{format_text(lang, 'trust_buffer')}",
                reply_markup=build_support_back_menu(cfg, lang),
            )
            return

        if data == "wallet_guide":
            bot.send_message(
                c.message.chat.id,
                format_text(lang, "wallet_guide"),
                reply_markup=build_support_back_menu(cfg, lang),
            )
            return

        if data == "support_info":
            bot.send_message(
                c.message.chat.id,
                format_text(lang, "support"),
                reply_markup=build_support_back_menu(cfg, lang),
            )
            return

    @bot.message_handler(func=lambda msg: is_private(msg.chat.type), content_types=["text"])
    def handle_private_text(msg):
        lang = update_chat_language_from_message(msg.chat.id, msg.text, msg.from_user.language_code)
        text = (msg.text or "").strip()
        if not text:
            send_start(msg.chat.id, lang)
            return

        reply_text, reply_markup = keyword_reply(text, cfg, lang)
        if reply_text:
            bot.send_message(
                msg.chat.id,
                reply_text,
                reply_markup=reply_markup or build_support_back_menu(cfg, lang),
            )
            return

        bot.send_message(
            msg.chat.id,
            format_text(lang, "unknown"),
            reply_markup=build_support_back_menu(cfg, lang),
        )

