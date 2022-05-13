from	aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('/сепар')
b2 = KeyboardButton('/пидр')
b3 = KeyboardButton('/Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b1, b2)