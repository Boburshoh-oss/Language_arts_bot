from aiogram import executor

# from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from aiogram.utils.executor import start_webhook
from loader import bot,dp
import os
from data.config import BOT_TOKEN
WEBHOOK_HOST = 'https://languageartsbot.herokuapp.com'
WEBHOOK_PATH = f"/setwebhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = 8000 

async def on_startup(dp):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dp)
    await bot.set_webhook(WEBHOOK_URL)


    # Bot ishga tushgani haqida adminga xabar berish
#     await on_startup_notify(dispatcher)


async def on_shutdown(dp):

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )



