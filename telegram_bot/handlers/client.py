from aiogram import types, Dispatcher
from create_bot import dp,bot
from keyboards import kb_client

import random as rd


# @dp.message_handler(commands=['pidr', 'пидр'])
async def check_pidr(message : types.Message):
	min_pidr = 60
	if message.from_user.username == "FireFlovveR":
		await message.reply("Ты " + str(message.from_user.full_name) + " пидр на "+ str(rd.randint(0,100)+min_pidr)+"%", reply_markup=kb_client)
	else:
		await message.reply("Ты " + str(message.from_user.full_name) + " пидр на "+ str(rd.randint(0,100))+"%", reply_markup=kb_client)

# @dp.message_handler(commands=['separ', 'сепар'])
async def check_separ(message : types.Message):
	min_separ = 60
	separ_pers = rd.randint(0,100)
	sl = ""
	if separ_pers < 30:
		sl = " Слава Украние!"
	elif separ_pers > 70:
		sl = " Слышу ZоV, ебать AZOV!" 
	if message.from_user.username == "Djossss":
		await message.reply("Ты " + str(message.from_user.full_name) + " сепар на "+ str(separ_pers+min_separ)+"%"+" Слава ВЛАДИМИРУ ВЛАДИМИРОВИЧУ!", reply_markup=kb_client)
	else:
		await message.reply("Ты " + str(message.from_user.full_name) + " сепар на "+ str(separ_pers)+"%"+sl, reply_markup=kb_client)


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(check_pidr, commands=['pidr', 'пидр'])
	dp.register_message_handler(check_separ, commands=['separ', 'сепар'])
