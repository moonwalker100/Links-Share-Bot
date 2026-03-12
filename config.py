# +++ Modified By [telegram username: @Codeflix_Bots
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "34567990")
APP_ID = int(os.environ.get("APP_ID", "27693340"))
API_HASH = os.environ.get("API_HASH", "1056193e68c138ee16edc02578c559e1")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "1718481517"))
PORT = os.environ.get("PORT", "8081")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://moonwalker1092:moonwalker1234@cluster0.svrznzr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "cluster0")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>⚡ Yoo, {mention}\n\nYᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @loading_cluster</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC = "https://graph.org/file/c22ccad28832aed94dbf1-49c96f1f7912938b86.jpg"
START_IMG = "https://graph.org/file/a617481d19aa04ace0c7c-ab1b60b42572ba17ae.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>⚡ Hᴇʏ, {mention} ~ \n\n<blockquote expandable>Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.</blockquote>\n\n‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/Here_remo'>Ꮢᴇᴍᴏ 🜲</a></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ 🜲</a>\n» Our Community: <a href=https://t.me/loading_cluster>ᴄʟᴜꜱᴛᴇʀ ʙᴏᴛꜱ</a>\n» Anime Channel: <a href=https://t.me/play_tamil_dubbed_series>ᴘʟᴀʏ ᴄᴏᴍᴍᴜɴɪᴛʏ</a>\n» Developer: <a href=https://t.me/Here_remo></a>Ꮢᴇᴍᴏ 🜲</b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by Ꮢᴇᴍᴏ (@Here_remo) to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>🤖 ᴍʏ ɴᴀᴍᴇ: {botname}
<b><blockquote expandable>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ 🜲</a>
» ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href=https://t.me/play_tamil_dubbed_series>ᴘʟᴀʏ ᴄᴏᴍᴍᴜɴɪᴛʏ</a>
» ʟᴀɴɢᴜᴀɢᴇ: <a href=https://docs.python.org/3/>Pʏᴛʜᴏɴ 3</a>
» ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org/>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
» ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ</a></blockquote></b>"""

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/play_tamil_dubbed_series'>ᴘʟᴀʏ ᴄᴏᴍᴍᴜɴɪᴛʏ</a>
<blockquote expandable>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/loading_cluster'>ᴄʟᴜꜱᴛᴇʀ ʙᴏᴛꜱ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/Here_remo>Ꮢᴇᴍᴏ</a></b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002413997036")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "6497757690").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
