from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text="About"),
        ],
        [
            KeyboardButton(text="Payment"),
            KeyboardButton(text="Shipping"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='What do you want?'
)

del_keyboard = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="Menu"),
    KeyboardButton(text="About"),
    KeyboardButton(text="Payment"),
    KeyboardButton(text="Shipping"),
)
start_kb2.adjust(2, 2)

start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text="Contact"))
