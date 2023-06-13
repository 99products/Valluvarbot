import telegram
from deta import App
from telegram.ext import Dispatcher, CallbackQueryHandler, CommandHandler
from queue import Queue
from fastapi import Request, FastAPI
import os
import requests

app = App(FastAPI())
TELEGRAM_TOKEN = os.getenv('telegram_token').strip()

bot = telegram.Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot, use_context=True, update_queue=Queue())


@app.get("/")
def hello_world():
    return "Working.."


@app.post("/")
async def process(request: Request):
    request_data = await request.json()
    print(request_data)
    update = telegram.Update.de_json(request_data, bot)
    dispatcher.process_update(update)
    if update.message and update.message.text:
        text = update.message.text.lower()
        response = search_hugging_face(text.lower())
        bot.sendMessage(chat_id=update.message.chat.id, text=response)
    return 'ok'


def search_hugging_face(text: str):
    response = requests.post("https://thiyagab-thamizh.hf.space/run/predict", json={
        "data": [
            text,
        ]}).json()

    data = response["data"]
    return data[0]
