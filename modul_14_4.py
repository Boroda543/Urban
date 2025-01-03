import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

from crud_functions import initiate_db, get_all_products

API_TOKEN = 'YOUR_API_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_kb.add(KeyboardButton('Рассчитать'), KeyboardButton('Информация'), KeyboardButton('Купить'))

buying_menu_kb = InlineKeyboardMarkup()
buying_menu_kb.add(
    InlineKeyboardButton("Product1", callback_data="product_buying"),
    InlineKeyboardButton("Product2", callback_data="product_buying"),
    InlineKeyboardButton("Product3", callback_data="product_buying"),
    InlineKeyboardButton("Product4", callback_data="product_buying"),
)

initiate_db()


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await message.answer("Добро пожаловать! Выберите опцию:", reply_markup=main_menu_kb)


@dp.message_handler(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    products = get_all_products()

    for product in products:
        id, title, description, price = product
        await message.answer(f"Название: {title} | Описание: {description} | Цена: {price}")

    await bot.send_photo(message.chat.id, 'image_url')

    await message.answer('Выберите продукт для покупки:', reply_markup=buying_menu_kb)


@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer("Вы успешно приобрели продукт!")
    await bot.send_message(call.from_user.id, "Спасибо за покупку!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
