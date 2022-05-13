from aiogram.utils import executor	
from create_bot import dp



async def on_startup(_):
	print("Тест на гомосека включен")

from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)


	
	# await message.answer(message.text)
	# await message.reply(message.text+" = "+str((message.from_user.username)))
	# await message.send_message(message.from_user.id, message.text)
	# await message.reply((dir(message.from_user)))

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


