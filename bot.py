import logging
from aiogram import Bot, Dispatcher, executor, types
from bazasql import *
import os
from button import *
from chatgpt_API import OpenAIProcessor
from io import BytesIO

api_key = 'api_key'
# system_prompt = """
# Я буду тебе отправлять тебе диалог, переписки с девушками. Ты всегда парень и должен отвечать на сообщение девушки. В переписках слева будут текста от девушки, а справа твои. Ты - мастер флирта и обольщения. Твоя задача - давать короткие, уверенные и игривые ответы на русском языке, которые демонстрируют высокий уровень "риззa". Используй остроумие, легкие комплименты и намеки. Будь смелым, но не грубым. Ответы должны быть краткими, не более 1-2 предложений. Цель - вызвать интерес и желание продолжить общение. Например: "Возраст — это просто число. Давай лучше узнаем друг друга поближе """


processor = OpenAIProcessor(api_key)

API_TOKEN = 'API_Token'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user
    a = add_user(chatid = user.id, username = user.username)
    if a =="qo'shildi":
        await message.reply("Отправьте мне скриншот переписки с вашей девушкой и я вам скажу как ответить)\n")
    else:
        print(a)
        await message.reply("neto")

@dp.message_handler(content_types=['photo'])
async def get(message: types.Message):
    photo = message.photo[-1]
    bio = BytesIO()
    await photo.download(destination_file=bio)
    bio.seek(0)
    try:
        flirty_response = processor.process_image(bio.getvalue())
        await message.reply(f"Вариант ответа: {flirty_response}", reply_markup=boshqa_variant)
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        await message.reply("Извините, произошла ошибка при обработке вашего изображения.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    com.close()