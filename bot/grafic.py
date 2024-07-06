from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from db import connect_db

def register_grafic_handler(dp):
    @dp.message_handler(commands=['grafic'])
    async def grafic(message: types.Message):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [
            KeyboardButton(text="Неполный рабочий день"),
            KeyboardButton(text="Полный рабочий день")
        ]
        keyboard.add(*buttons)
        await message.reply("Выберите график работы:", reply_markup=keyboard)

    @dp.message_handler(lambda message: message.text in ["Неполный рабочий день", "Полный рабочий день"])
    async def grafic_selection(message: types.Message):
        query_data = 'part_time' if message.text == "Неполный рабочий день" else 'full_time'

        conn = connect_db()
        with conn.cursor() as cur:
            if query_data == 'part_time':
                cur.execute("SELECT COUNT(*) FROM vacancies WHERE location ILIKE '%Неполный рабочий день%';")
            elif query_data == 'full_time':
                cur.execute("SELECT COUNT(*) FROM vacancies WHERE location ILIKE '%Полный рабочий день%';")
            count = cur.fetchone()[0]
        conn.close()

        await message.reply(f'Количество вакансий с графиком "{message.text}": {count}')
