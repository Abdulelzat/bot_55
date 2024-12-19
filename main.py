import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Отсутствует токен бота. Убедитесь, что он указан в файле .env под ключом BOT_TOKEN.")

bot = Bot(token=TOKEN)
dp = Dispatcher()

NAMES = ["Алексей", "Мария", "Дмитрий", "Екатерина", "Иван", "Ольга"]

@dp.message(Command("start"))
async def start_command_handler(message: Message):
    user_name = message.from_user.first_name or "друг"
    await message.answer(f"Привет, {user_name}! Добро пожаловать в бота!")

@dp.message(Command("myinfo"))
async def myinfo_command_handler(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name or "Не указано"
    username = message.from_user.username or "Не указано"
    await message.answer(
        f"Ваши данные:\n"
        f"ID: {user_id}\n"
        f"Имя: {first_name}\n"
        f"Username: {username}"
    )

@dp.message(Command("random"))
async def random_command_handler(message: Message):
    random_name = random.choice(NAMES)
    await message.answer(f"Случайное имя: {random_name}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
