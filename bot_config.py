from aiogram import Bot, Dispatcher
from database import Database
from dotenv import dotenv_values


token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
database = Database("db.sqlite3")