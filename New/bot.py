import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.types.web_app_info import WebAppInfo

from db import BotDB


# from flask import Flask, request

import pickle

# from main import record
class V:
    def __init__(self):
        self.user = Message.message.from_user.id

    @property
    def user_id(self):
        print(self.user)
        return self.user


BotDB = BotDB('account.db')

bot = Bot(token='7355824060:AAHuyPfFtANlBCWSrQT4gCGf-3oXL4nzdBs')
dp = Dispatcher()



@dp.message(CommandStart())
async def start(message: Message):
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Кликер🌸цветочек', web_app=WebAppInfo(url='https://9980-188-168-152-214.ngrok-free.app'))],
        [KeyboardButton(text='Бонусы')]], resize_keyboard=True)

    with open("data.pkl", "wb") as f:
        pickle.dump(message.from_user.id, f)

    # Добавление пользователя
    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(message.from_user.id)

    await message.answer('Добро пожаловать!', reply_markup=markup)


@dp.message(F.text == 'Бонусы')
async def result(message: Message):
    # global user
    # user = message.from_user.id

    # with open("data.pkl", "rb") as f:
    #     record = pickle.load(f)
    #
    # print(record)
    #
    # if record != 0:
    #     record += BotDB.get_record(message.from_user.id)
    #     BotDB.up_record(message.from_user.id, record)

    res = "Ваши бонусные рубли: " + str(BotDB.get_record(message.from_user.id))

    await message.answer(res)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
