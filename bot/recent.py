from aiogram import types
from db import connect_db

def register_recent_handler(dp):
    @dp.message_handler(commands=['recent'])
    async def recent(message: types.Message):
        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute("SELECT company, vacancy, location, salary, skills, link FROM vacancies ORDER BY RANDOM() LIMIT 5;")
            rows = cur.fetchall()
        conn.close()

        if not rows:
            await message.reply('В базе данных пока нет вакансий.')
        else:
            await message.reply('Вот 5 случайных вакансий:')
            for row in rows:
                await message.reply(f'Компания: {row[0]}\nВакансия: {row[1]}\nМестоположение: {row[2]}\nЗарплата: {row[3]}\nСкиллы: {row[4]}\nСсылка: {row[5]}')
