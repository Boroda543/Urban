import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

logging.basicConfig(level=logging.INFO)

API_TOKEN = 'YOUR_BOT_TOKEN'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(types.KeyboardButton('Рассчитать'), types.KeyboardButton('Информация'))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Выбирите опцию:', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(types.InlineKeyboardButton('Рассчитать норму калорий', callback_data='colories'))
    inline_keyboard.add(types.InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'formules')
async def get_formulas(call: types.CallbackQuery):
    formula_message = ('Формула Миффлина-Сан Жеора: \nДля мужчин: Bmr = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) + 5\nДля женщин: ВMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) - 161')
    await call.message.answer(formula_message)

@dp.callback_query_handler(lambda call: call.data == 'colories')
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await UserState.age.set()
    await call.message.answer('Введите свой возраст:')

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer('Введите свой рост:')

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer('Введите свой вес:')

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories} калл.")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)