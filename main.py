from pyrogram import Client, filters
import random

PICS = [
 "https://telegra.ph/file/28f4c97f0d1248873d4bd.jpg"
]

START_BUTTONS = [[
        InlineKeyboardButton("My Father 🧔", url=f"https://t.me/{username}"),
        InlineKeyboardButton("Updates Channel 🔰", url="https://telegram.dog/NsBotsOfficial")
        ],[
        InlineKeyboardButton("Source code 😎", url="https://github.com/Ns-AnoNymouS/animated-lamp")
        ],[
        InlineKeyboardButton("Help ⁉️", callback_data="help"),
        InlineKeyboardButton("Settings ⚙", callback_data="set+settings")
        ],[
        InlineKeyboardButton("Close 📛", callback_data="close")
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

print("Bot is running 🏃")

HKZ.run()
