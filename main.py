from pyrogram import Client, filters
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


PICS = [
 "https://telegra.ph/file/28f4c97f0d1248873d4bd.jpg"
]

START_BUTTONS = [[
        InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ 👨‍💻", url=f"https://t.me/MR_HKZ_TG"),
        InlineKeyboardButton("Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ 🔰", url="https://telegram.dog/HKZTG")
        ],[
        InlineKeyboardButton("Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 😎", url="https://github.com/Ns-AnoNymouS/animated-lamp")
        ],[
        InlineKeyboardButton("Hᴇʟᴘ 🛠", callback_data="help"),
        InlineKeyboardButton("Sᴇᴛᴛɪɴɢs ⚙", callback_data="set+settings")
        ],[
        InlineKeyboardButton("Cʟᴏsᴇ 📛", callback_data="close")
    ]] 

HKZ = Client(
    name="PyrogramBot",
    api_id="23050566",
    api_hash="25e954ccd4afb778eea69bd6754275ff",
    bot_token="7037015366:AAGsTNCQ4lwm_dcSuWauRrk6MWsnKRMzNtI"
)

@HKZ.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(random.choice(PICS), caption=f"""Hᴇʟʟᴏ {message.from_user.mention} 👋,

I'ᴍ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ sᴄʀᴇᴇɴsʜᴏᴛs ʏᴏᴜʀ ᴠɪᴅᴇᴏ ғɪʟᴇs. Fᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴄʜᴇᴄᴋ ʜᴇʟᴘ

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ: [ʜᴋᴢ ᴛɢ 🇮🇳](t.me/HKZTG)""", reply_markup=InlineKeyboardMarkup(START_BUTTOMS))

@HKZ.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("home"))
)
async def home_cb(c, m):
    await m.answer()
    await start(c, m, True)


@HKZ.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("close"))
)
async def close_cb(c, m):
    try:
        await m.message.delete()
        await m.message.reply_to_message.delete()
    except:
        pass


print("Bot is running 🏃")

HKZ.run()
