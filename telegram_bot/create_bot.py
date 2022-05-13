from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os


#Устанавливаем токен для подключения бота к API telegram из файла
TOKEN = open("tkn.tx",'r').read()

# Запускаем ботка с токеном и инициализируем диспетчера
bot = Bot(TOKEN)
dp = Dispatcher(bot)