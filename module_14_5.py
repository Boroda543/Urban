from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import KeyboardButton
from aiogram.utils import executor

from crud_functions import is_included, add_user
from modul_14_4 import main_menu_kb, dp


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


main_menu_kb.add(KeyboardButton('Регистрация'))


@dp.message_handler(lambda message: message.text == "Регистрация")
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if not is_included(username):
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя.")


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    data = await state.get_data()
    username = data.get('username')
    email = data.get('email')

    add_user(username, email, age)
    await message.answer("Регистрация завершена! Добро пожаловать!")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
