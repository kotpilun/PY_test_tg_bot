from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f

from keyboards import reply

user_privat_router = Router()

@user_privat_router.message(CommandStart())
async def start_cmd(message:types.Message):
    # await message.answer('Привет! Я виртуальный помощник', reply_markup=reply.start_kb)
    await message.answer('Привет! Я виртуальный помощник', 
                        reply_markup=reply.start_kb3.as_markup(
                            resize_keyboard=True,
                            input_field_placeholder='What do you want?'))

@user_privat_router.message(or_f(Command('menu'), (F.text.lower() == 'menu')))
async def menu_cmd(message:types.Message):
    await message.answer('Here is our menu:', reply_markup=reply.del_keyboard)

@user_privat_router.message(Command('about'))
async def about_cmd(message:types.Message):
    await message.answer('About section of this test bot')

@user_privat_router.message(Command('keyboard'))
async def about_cmd(message:types.Message):
    await message.answer('Please choose', reply_markup=reply.start_kb)

@user_privat_router.message(F.text)
async def about_cmd(message:types.Message):
    await message.answer(message.text)