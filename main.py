from pyrogram import Client, filters
import random

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
    await message.reply(photo=random.choice(PICS), caption="Hello Sir")

print("Bot is running 🏃")

HKZ.run()
