import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "BOT_TOKEN": os.getenv("BOT_TOKEN"),
        "APP_URL": os.getenv("APP_URL"),
        "BIND_URL": os.getenv("BIND_URL"),
        "GROUP_URL": os.getenv("GROUP_URL"),
        "CHANNEL_URL": os.getenv("CHANNEL_URL"),
        "SUPPORT_URL": os.getenv("SUPPORT_URL"),
        "SUPPORT_URL_1": os.getenv("SUPPORT_URL_1"),
        "SUPPORT_URL_2": os.getenv("SUPPORT_URL_2"),
    }
