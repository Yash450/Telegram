import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "9333070")
    API_HASH = getenv("API_HASH", "511eb11eda4af78ec8f9a0a7de9e1241")
    TOKEN = getenv("TOKEN", "5560643905:AAGD61XBWVzGRCCEPLqRw38ARfYl5dEM1Lw")
    OWNER_ID = getenv("OWNER_ID", "5016109398")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOLABuyLuWvOMbiVUegS-ZI_PmlxrktkKQDatMV-Qm_mVeu5XnkgeZ_oOycw3uaFtsr48waqVPVU2g9_VoIOVknAfDZm9_NZeQG7-_HWN0OPVuH6HS4nR28hv7gJ9ctSRFeQrfYwXwZiDmYdvlGi40-8ipDGc58zq5s8lXuNKgUiimZFZM0Ja8-lLR6UttHCwPXIFTGAmtMmnVuPg08SG0fDGoGpB6KcA8KVr02RWhcFszOhDRnulhJ4FUe_jhy_S-cjckVkGkZanykBymWojsG1qX7J2TCsnJzYRDc4jPw5uctqCcQm8cTuJ_o-mqkeJ0Ch0GhmhgLU-nPGS-sdsKznmLuo=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Yash_608")
    DB_URI = getenv("DATABASE_URL", "mongodb+srv://Yashking1:Yashking1@cluster0.edtzwqc.mongodb.net/?retryWrites=true&w=majority")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001509525202")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001765798012")
    SYS_ADMIN = getenv("SYS_ADMIN", "5016109398")
    DEV_USERS = getenv("DEV_USERS", "5016109398")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "0iBcFRdvlI6eZ_vFA3acSUZ3OxgOEYuOwhKOH82hr4NptGDRXVcXVvN7fVAxUwP6")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5016109398").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "5016109398").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
