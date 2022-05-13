from aiogram import types, Dispatcher
from create_bot import dp
import os, string, json


# @dp.message_handler()
async def echo_send(message : types.Message):
	if (message.from_user.username != "FireFlovveR") and ({i.lower().translate(str.maketrans('','', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('words.json'))))) and ("Кто" in message.text or "кто" in message.text):
		await message.answer("Всем понятно кто, конечно же Игорь @FireFlovveR!")
	elif message.text == "tst":
		await message.answer("TEST"+str(dir(message.from_user)))


def register_handlers_other(dp : Dispatcher):
	dp.register_message_handler(echo_send)
	
