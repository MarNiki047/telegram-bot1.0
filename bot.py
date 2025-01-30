import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import os

TOKEN = os.getenv("TOKEN")  # Отримуємо токен з Railway
CHANNEL_ID = os.getenv("CHANNEL_ID")  # ID каналу

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привіт! Надішліть /sell, щоб додати товар.")

@dp.message_handler(commands=['sell'])
async def sell_start(message: types.Message):
    await message.answer("📸 Надішліть фото товару.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
