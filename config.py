# (©) @RknDeveloper ❣️
import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "20652787")
    API_HASH = os.environ.get("API_HASH", "5dea928561e4d2eb77a371edf8b2eb2a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6380339169:AAH5vkzcx8Y2ZaRhJURV4eEcah332uAjO0c") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","DP_BOTZ")     
    DB_URL = os.environ.get("DB_URL","mongodb+srv://Aloneboy:Aloneboytg@cluster0.nmeelsr.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME = time.time()
    RKN_PIC = os.environ.get("RKN_PIC", "https://te.legra.ph/file/ba16b6f4c78879c5d5527.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1242556540').split()]
    FORCE_SUB = os.environ.get("FORCE_SUB", "-1002008853384") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class rkn(object):
    # part of text configuration
    START_TXT = """<b>𝐇𝐞𝐲, {}👋

𝐈𝐀𝐦 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 & 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥𝐥 𝐅𝐢𝐥𝐞 𝐑𝐞𝐧𝐚𝐦𝐞 𝐁𝐨𝐭 . 
𝐘𝐨𝐮 𝐂𝐚𝐧 𝐑𝐞𝐧𝐚𝐦𝐞 𝐅𝐢𝐥𝐞 𝐀𝐧𝐝 𝐅𝐢𝐥𝐞 𝐓𝐨 𝐯𝐢𝐝𝐞𝐨 𝐂𝐨𝐧𝐯𝐞𝐫𝐭𝐞𝐫 
𝐀𝐧𝐝 𝐜𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐀𝐧𝐝 𝐂𝐮𝐬𝐭𝐨𝐦 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 . 
𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐜𝐫𝐞𝐚𝐭𝐞 𝐁𝐲 : 💙 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 💙 <a href=https://t.me/DP_BOTZ</a></b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/DP_BOTZ>DP_BOTZ</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/All_Tamil_movies_request/DPDeveloper>DP_BOTZ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├📊 ᴠᴇʀsɪᴏɴ: <a href=https://t.me/DP_BOTZ/DP-rename-bot-V3>𝟸.𝟶.𝟶</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>
<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}
✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ ɴᴀᴍᴇ \nAɴᴅ sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/All_Tamil_movies_request>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @DP_BOTZ🙏🥲
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://t.me/DP_BOTZ/DP-rename-bot-V3>DP_BOTZ</a>
• ❣️ <a href=https://t.me/MERSAL_DHINESH>⚡ 𝐨𝐰𝐧𝐞𝐫 ⚡</a>
• ❣️ <a href=https://t.me/dpowner_bot>© 𝐀𝐝𝐦𝐢𝐧 ©</a> """

    RKN_PROGRESS = """<b>\n
╭━━━━❰DP PROCESSING...❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""


