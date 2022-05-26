import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred:
    BOT_NAME = os.getenv("subtitlestranslater_bot")
    BOT_TOKEN = os.getenv("5338762282:AAFQHsEu-qZVz65bRFKlqr4t3garDMNaFfs")  # From botfather
    API_ID = os.getenv(
        "17545386"
    )  # "Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv(
        "f1d5ee6adccd34db0aab30115f4c30db"
    )  # "Get this value from my.telegram.org! Please do not steal"
    DB_URL = os.getenv("https://subtrans-37fa1-default-rtdb.firebaseio.com/")  # From Firebase database
