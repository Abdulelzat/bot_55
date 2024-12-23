from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_command_handler(message: types.Message):
    user_name = message.from_user.first_name or "друг"
    await message.answer(f"Привет, {user_name}! Добро пожаловать в бота!")