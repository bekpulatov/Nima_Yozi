from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

boshqa_variant = ReplyKeyboardMarkup(
   keyboard=[
       [KeyboardButton('Другой вариант')],
        [KeyboardButton("Новый скриншот")],
   ],
    resize_keyboard=True,
)