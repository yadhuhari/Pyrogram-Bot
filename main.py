from pyrogram import Client, filters
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery


PICS = [
 "https://telegra.ph/file/28f4c97f0d1248873d4bd.jpg"
]

HKZ = Client(
    name="PyrogramBot",
    api_id="23050566",
    api_hash="25e954ccd4afb778eea69bd6754275ff",
    bot_token="7037015366:AAGsTNCQ4lwm_dcSuWauRrk6MWsnKRMzNtI"
)

@HKZ.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS), 
        caption=f"""Hᴇʟʟᴏ {message.from_user.mention} 👋,

I'ᴍ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ sᴄʀᴇᴇɴsʜᴏᴛs ʏᴏᴜʀ ᴠɪᴅᴇᴏ ғɪʟᴇs. Fᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴄʜᴇᴄᴋ ʜᴇʟᴘ

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ: [ʜᴋᴢ ᴛɢ 🇮🇳](t.me/HKZTG)""", 
        reply_markup=InlineKeyboardMarkup( [[
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
            )
    )

HELP_TEXT = """Hɪ {mention}. Wᴇʟᴄᴏᴍᴇ ᴛᴏ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴄʀᴇᴇɴsʜᴏᴛs. 

👉 I sᴜᴘᴘᴏʀᴛ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ ғɪʟᴇ (sᴛʀᴇᴀᴍɪɴɢ ᴠɪᴅᴇᴏ ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ ᴠɪᴅᴇᴏ ғɪʟᴇs) ᴘʀᴏᴠɪᴅᴇᴅ ɪᴛ ʜᴀs ᴘʀᴏᴘᴇʀ ᴍɪᴍᴇ-ᴛʏᴘᴇ ᴀɴᴅ ɪs ɴᴏᴛ ᴄᴏʀʀᴜᴘᴛᴇᴅ.
👉 I ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ Sᴛʀᴇᴀᴍɪɴɢ URLs. Tʜᴇ URL sʜᴏᴜʟᴅ ʙᴇ ᴀ sᴛʀᴇᴀᴍɪɴɢ URL, ɴᴏɴ IP sᴘᴇᴄɪғɪᴄ, ᴀɴᴅ sʜᴏᴜʟᴅ ʀᴇᴛᴜʀɴ ᴘʀᴏᴘᴇʀ ʀᴇsᴘᴏɴsᴇ ᴄᴏᴅᴇs.
Jᴜsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴏʀ ᴛʜᴇ sᴛʀᴇᴀᴍɪɴɢ URL.

Sᴇᴇ /settings ᴛᴏ ᴄᴏɴғɪɢᴜʀᴇ ʙᴏᴛ's ʙᴇʜᴀᴠɪᴏʀ.
Usᴇ /set_watermark ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴡᴀᴛᴇʀᴍᴀʀᴋs ᴛᴏ ʏᴏᴜʀ sᴄʀᴇᴇɴsʜᴏᴛs.

Gᴇɴᴇʀᴀʟ FAQ.

👉 Iғ ᴛʜᴇ ʙᴏᴛ ᴅᴏsᴇɴ'ᴛ ʀᴇsᴘᴏɴᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs ʏᴏᴜ ғᴏʀᴡᴀʀᴅ, ғɪʀsᴛ ᴄʜᴇᴄᴋ /sᴛᴀʀᴛ ᴀɴᴅ ᴄᴏɴғɪʀᴍ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ. Tʜᴇɴ ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴇ ғɪʟᴇ ɪs ᴀ ᴠɪᴅᴇᴏ ғɪʟᴇ ᴡʜɪᴄʜ sᴀᴛɪsғɪᴇs ᴀʙᴏᴠᴇ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄᴏɴᴅɪᴛɪᴏɴs.
👉 Iғ ʙᴏᴛ ʀᴇᴘʟɪᴇs 😟 Sᴏʀʀʏ! I ᴄᴀɴɴᴏᴛ ᴏᴘᴇɴ ᴛʜᴇ ғɪʟᴇ., ᴛʜᴇ ғɪʟᴇ ᴍɪɢʜᴛ ʙᴇ ᴄᴜʀʀᴜᴘᴛᴇᴅ ᴏʀ ɪs ᴍᴀʟғᴏʀᴍᴀᴛᴛᴇᴅ.

Iғ ɪssᴜᴇs ᴘᴇʀsɪsᴛs ᴄᴏɴᴛᴀᴄᴛ ᴍʏ Dᴇᴠᴇʟᴏᴘᴇʀ.
"""

@HKZ.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS), 
        caption=f"""Hɪ {message.from_user.mention}. Wᴇʟᴄᴏᴍᴇ ᴛᴏ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴄʀᴇᴇɴsʜᴏᴛs. 

👉 I sᴜᴘᴘᴏʀᴛ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ ғɪʟᴇ (sᴛʀᴇᴀᴍɪɴɢ ᴠɪᴅᴇᴏ ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ ᴠɪᴅᴇᴏ ғɪʟᴇs) ᴘʀᴏᴠɪᴅᴇᴅ ɪᴛ ʜᴀs ᴘʀᴏᴘᴇʀ ᴍɪᴍᴇ-ᴛʏᴘᴇ ᴀɴᴅ ɪs ɴᴏᴛ ᴄᴏʀʀᴜᴘᴛᴇᴅ.
👉 I ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ Sᴛʀᴇᴀᴍɪɴɢ URLs. Tʜᴇ URL sʜᴏᴜʟᴅ ʙᴇ ᴀ sᴛʀᴇᴀᴍɪɴɢ URL, ɴᴏɴ IP sᴘᴇᴄɪғɪᴄ, ᴀɴᴅ sʜᴏᴜʟᴅ ʀᴇᴛᴜʀɴ ᴘʀᴏᴘᴇʀ ʀᴇsᴘᴏɴsᴇ ᴄᴏᴅᴇs.
Jᴜsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴏʀ ᴛʜᴇ sᴛʀᴇᴀᴍɪɴɢ URL.

Sᴇᴇ /settings ᴛᴏ ᴄᴏɴғɪɢᴜʀᴇ ʙᴏᴛ's ʙᴇʜᴀᴠɪᴏʀ.
Usᴇ /set_watermark ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴡᴀᴛᴇʀᴍᴀʀᴋs ᴛᴏ ʏᴏᴜʀ sᴄʀᴇᴇɴsʜᴏᴛs.

Gᴇɴᴇʀᴀʟ FAQ.

👉 Iғ ᴛʜᴇ ʙᴏᴛ ᴅᴏsᴇɴ'ᴛ ʀᴇsᴘᴏɴᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs ʏᴏᴜ ғᴏʀᴡᴀʀᴅ, ғɪʀsᴛ ᴄʜᴇᴄᴋ /sᴛᴀʀᴛ ᴀɴᴅ ᴄᴏɴғɪʀᴍ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ. Tʜᴇɴ ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴇ ғɪʟᴇ ɪs ᴀ ᴠɪᴅᴇᴏ ғɪʟᴇ ᴡʜɪᴄʜ sᴀᴛɪsғɪᴇs ᴀʙᴏᴠᴇ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄᴏɴᴅɪᴛɪᴏɴs.
👉 Iғ ʙᴏᴛ ʀᴇᴘʟɪᴇs 😟 Sᴏʀʀʏ! I ᴄᴀɴɴᴏᴛ ᴏᴘᴇɴ ᴛʜᴇ ғɪʟᴇ., ᴛʜᴇ ғɪʟᴇ ᴍɪɢʜᴛ ʙᴇ ᴄᴜʀʀᴜᴘᴛᴇᴅ ᴏʀ ɪs ᴍᴀʟғᴏʀᴍᴀᴛᴛᴇᴅ.

Iғ ɪssᴜᴇs ᴘᴇʀsɪsᴛs ᴄᴏɴᴛᴀᴄᴛ ᴍʏ Dᴇᴠᴇʟᴏᴘᴇʀ.
""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Hᴇʟᴘ 🛠", callback_data="help"),
            InlineKeyboardButton("Sᴇᴛᴛɪɴɢs ⚙", callback_data="set+settings")
            ],[
            InlineKeyboardButton("Cʟᴏsᴇ 📛", callback_data="close")
            ]] 
            )
    )

@HKZ.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("help"))
)
async def help_cb(c, m):
    await message.answer()
    await message.message.edit(
        photo=random.choice(PICS), 
        caption=f"""Hɪ {message.from_user.mention}. Wᴇʟᴄᴏᴍᴇ ᴛᴏ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴄʀᴇᴇɴsʜᴏᴛs. 

👉 I sᴜᴘᴘᴏʀᴛ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ ғɪʟᴇ (sᴛʀᴇᴀᴍɪɴɢ ᴠɪᴅᴇᴏ ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ ᴠɪᴅᴇᴏ ғɪʟᴇs) ᴘʀᴏᴠɪᴅᴇᴅ ɪᴛ ʜᴀs ᴘʀᴏᴘᴇʀ ᴍɪᴍᴇ-ᴛʏᴘᴇ ᴀɴᴅ ɪs ɴᴏᴛ ᴄᴏʀʀᴜᴘᴛᴇᴅ.
👉 I ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ Sᴛʀᴇᴀᴍɪɴɢ URLs. Tʜᴇ URL sʜᴏᴜʟᴅ ʙᴇ ᴀ sᴛʀᴇᴀᴍɪɴɢ URL, ɴᴏɴ IP sᴘᴇᴄɪғɪᴄ, ᴀɴᴅ sʜᴏᴜʟᴅ ʀᴇᴛᴜʀɴ ᴘʀᴏᴘᴇʀ ʀᴇsᴘᴏɴsᴇ ᴄᴏᴅᴇs.
Jᴜsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴏʀ ᴛʜᴇ sᴛʀᴇᴀᴍɪɴɢ URL.

Sᴇᴇ /settings ᴛᴏ ᴄᴏɴғɪɢᴜʀᴇ ʙᴏᴛ's ʙᴇʜᴀᴠɪᴏʀ.
Usᴇ /set_watermark ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴡᴀᴛᴇʀᴍᴀʀᴋs ᴛᴏ ʏᴏᴜʀ sᴄʀᴇᴇɴsʜᴏᴛs.

Gᴇɴᴇʀᴀʟ FAQ.

👉 Iғ ᴛʜᴇ ʙᴏᴛ ᴅᴏsᴇɴ'ᴛ ʀᴇsᴘᴏɴᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs ʏᴏᴜ ғᴏʀᴡᴀʀᴅ, ғɪʀsᴛ ᴄʜᴇᴄᴋ /sᴛᴀʀᴛ ᴀɴᴅ ᴄᴏɴғɪʀᴍ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ. Tʜᴇɴ ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴇ ғɪʟᴇ ɪs ᴀ ᴠɪᴅᴇᴏ ғɪʟᴇ ᴡʜɪᴄʜ sᴀᴛɪsғɪᴇs ᴀʙᴏᴠᴇ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄᴏɴᴅɪᴛɪᴏɴs.
👉 Iғ ʙᴏᴛ ʀᴇᴘʟɪᴇs 😟 Sᴏʀʀʏ! I ᴄᴀɴɴᴏᴛ ᴏᴘᴇɴ ᴛʜᴇ ғɪʟᴇ., ᴛʜᴇ ғɪʟᴇ ᴍɪɢʜᴛ ʙᴇ ᴄᴜʀʀᴜᴘᴛᴇᴅ ᴏʀ ɪs ᴍᴀʟғᴏʀᴍᴀᴛᴛᴇᴅ.

Iғ ɪssᴜᴇs ᴘᴇʀsɪsᴛs ᴄᴏɴᴛᴀᴄᴛ ᴍʏ Dᴇᴠᴇʟᴏᴘᴇʀ.
""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Hᴇʟᴘ 🛠", callback_data="help"),
            InlineKeyboardButton("Sᴇᴛᴛɪɴɢs ⚙", callback_data="set+settings")
            ],[
            InlineKeyboardButton("Cʟᴏsᴇ 📛", callback_data="close")
            ]]
            )
    )


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
