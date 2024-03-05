from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_privat_router = Router()

@user_privat_router.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer('Привет! Я виртуальный помощник')

@user_privat_router.message(Command('menu'))
async def menu_cmd(message:types.Message):
    await message.answer('MENU')

@user_privat_router.message(Command('about'))
async def about_cmd(message:types.Message):
    await message.answer('About section of this test bot')

@user_privat_router.message(F.text)
async def about_cmd(message:types.Message):
    await message.answer('Text magic filter')