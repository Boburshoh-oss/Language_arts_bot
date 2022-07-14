from aiogram import executor, Dispatcher

from loader import dp
import middlewares, filters, handlers
# from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from data import config
from aiogram.utils.executor import set_webhook
from flask import Flask
import requests 

app = Flask(__name__)

@app.post('')
def process_webhook_post():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)

async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    await dp.bot.set_webhook('')
    # Bot ishga tushgani haqida adminga xabar berish
#     await on_startup_notify(dispatcher)

async def on_shutdown(dp: Dispatcher):
    await dp.bot.delete_webhook()
    
def main():
    
    
    set_webhook(
        dispatcher=dp,
        webhook_path='',
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        web_app=app,
    )
    
    app.run(debug=True, host='https://language-arts.herokuapp.com/', port='8000')
    # web.run_app(app, port=config.WEBAPP_PORT, host=config.WEBAPP_HOST)


if __name__ == "__main__":
    main()

# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup=on_startup)
