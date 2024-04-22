from pyrogram import Client, filters

HKZ = Client(
    name="PyrogramBot",
    api_id="23050566",
    api_hash="25e954ccd4afb778eea69bd6754275ff",
    bot_token="7037015366:AAGsTNCQ4lwm_dcSuWauRrk6MWsnKRMzNtI"
   )

@HKZ.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Hello Sir")

print("Bot is running 🏃")

HKZ.run()
