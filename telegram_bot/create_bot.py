from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

TOKEN = open("tkn.tx",'r').read()

print("TOKEN = ", TOKEN)

bot = Bot(TOKEN)
dp = Dispatcher(bot)