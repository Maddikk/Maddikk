from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Создаем экземпляр класса MemoryStorage для хранения данных передаваемых боту в памяти
storage = MemoryStorage()

#Устанавливаем токен для подключения бота к API telegram из файла
TOKEN = open("tkn.tx",'r').read().strip()


# Запускаем ботка с токеном и инициализируем диспетчера
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)