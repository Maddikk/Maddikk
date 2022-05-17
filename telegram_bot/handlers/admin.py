from aiogram.dispatcher import FSMContext 
from aiogram.dispatcher.filters.state import State, StateGroup
from aiogram import types


class FSMAdmin(StateGroup):
	# 4 пункта последовательных вопросов
	photo = State() # Картинка для ответов 
	name = State() # Ключевое слово для ответа
	description - State() # Описание картинки
	count = State() # Вес прикола

# Базовый хендлер для загрузки первого пункта меню
@dp.message_handler(commands='Запомнить пользователя', state=None)
async def cm_start(message: type.Message):
	await FSMAdmin.photo.set()
	await message.reply('Загрузи картинку')


# Ждем картинку от пользователя
@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['photo'] = message.photo[0].file_id
	await FSMAdmin.next()
	await message.reply('Теперь укажи название')

# 6 серия 13:40