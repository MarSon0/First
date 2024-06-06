from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Кликер🌸цветочек', web_app=WebAppInfo(url='https://2b13-176-59-142-162.ngrok-free.app'))],
                                     [KeyboardButton(text='Бонусы')]], resize_keyboard=True)
