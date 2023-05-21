from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile
from qr_gen import gen
from auth_data import token

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Генерация"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Для старта нажмите на кнопку генерация",  reply_markup=keyboard)

@dp.message_handler(Text(equals="Генерация"))
async def tasks_for_gen(message: types.Message):
    await message.answer("Пожалуйста скинь текст для генерации после команды /text")

@dp.message_handler(commands="text")
async def generate(message:types.Message):
    file_name = gen(message.get_args())
    image = InputFile(file_name)
    await message.answer_photo(image, caption="qr")

if __name__ == "__main__":
    executor.start_polling(dp)