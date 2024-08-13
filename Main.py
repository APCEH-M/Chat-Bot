import asyncio
import config
import os

from aiogram import Router
router = Router()

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import logging
import random

import keyword
# from random_fox import fox

# Логирование действий
logging.basicConfig(level=logging.INFO)


# Объект бота и диспетчер
# bot = Bot(token=config.token_api, parse_mode='HTML')
# session = AiohttpSession(proxy="........................")
session = AiohttpSession(proxy=config.proxy_url)
bot = Bot(token=config.token_api, session=session)
dp = Dispatcher()

# Ожидание команды "/start"
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    # await message.answer("Привет 😊", reply_markup=keyword)

# Хэндлер на команду /info
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    number = random.randint(1, 7)
    info = await bot.get_me()
    await message.answer(f'Я тестовый бот - {info.first_name}')
    await message.answer(f'Твоё число {number}')

# Хэндлер на команду /user
@dp.message(Command("user"))
async def cmd_info(message: types.Message):
    user = await bot.get_me()
#    await message.answer(f'Проверка - {message.from_user.first_name} {message.from_user.last_name}')

    if message.from_user.first_name is None:
        First_Name = ''
    else:
        First_Name = message.from_user.first_name
    
    if message.from_user.last_name is None:
        Last_Name = ''
    else:
        Last_Name = message.from_user.last_name
    
    await message.answer(f'Вы представились как - {First_Name} {Last_Name}')
#    print(message)
#    print(message.from_user.first_name)

@dp.message(Command("stop"))
async def cmd_stop(message: types.Message):
    await dp.stop_polling()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())