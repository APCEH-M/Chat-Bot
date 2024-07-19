import asyncio
import config

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
session = AiohttpSession(proxy="http://proxy.halykbank.nb:8080")
bot = Bot(token=config.token_api, session=session)
#bot = Bot(token = config.token_api)
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))

async def cmd_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    # await message.answer("Привет 😊", reply_markup=keyword)

# Хэндлер на команду /info
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    number = random.randint(1, 7)
    await message.answer('Я тестовый бот')
    await message.answer('Твоё число {number}')
    # print(message)
    # print(message.from_user.first_name)

# @dp.message(Command("stop"))
    

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())