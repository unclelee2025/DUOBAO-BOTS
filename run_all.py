import threading

from bots.guide_bot.main import bot as guide_bot
try:
    from bots.welcome_bot.main import bot as welcome_bot
except ModuleNotFoundError:
    welcome_bot = None
from bots.anti_spam_bot.main import bot as anti_bot

def run(bot, name):
    print(f"{name} started")
    bot.infinity_polling()

def maybe_start(bot, name):
    if bot is None:
        print(f"{name} not configured, skipping.")
        return
    threading.Thread(target=run, args=(bot, name)).start()

maybe_start(guide_bot, "GuideBot")
maybe_start(welcome_bot, "WelcomeBot")
maybe_start(anti_bot, "AntiSpamBot")
