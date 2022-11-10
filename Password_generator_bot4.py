import random
import time
from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Hello, how many symbols of password do you want?")

@dp.message_handler()
async def get_password(message: types.Message):
    passlength = message.text
    try:
        passlength = int(passlength)
        if passlength > 15 or passlength < 5:
            await message.reply("Inappropriate length of password")
        else:
            a = "abcdefghijklmnopqrstuvwxyz"
            b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            с = "0123456789"
            d = "{}[]()?!*,-_"
            all = a + b + с + d
            password = "".join(random.sample(all, passlength))
            await message.answer(f"Your password: {password}")
    except Exception as ex2:
        print(ex2)
        await message.answer("Enter the number of symbols from 5 to 15")
if __name__=="__main__":
    executor.start_polling(dp)