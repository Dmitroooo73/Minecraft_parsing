from aiogram import types
from db import connect_db

def register_search_vacancy_handler(dp):
    @dp.message_handler(commands=['search_vacancy'])
    async def search_vacancy(message: types.Message):
        vacancy_title = message.get_args()
        if not vacancy_title:
            await message.reply('Пожалуйста, укажите название вакансии после команды /search_vacancy.')
            return

        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute("SELECT company, vacancy, location, salary, skills, link FROM vacancies WHERE vacancy ILIKE %s LIMIT 5;", (f'%{vacancy_title}%',))
            rows = cur.fetchall()
        conn.close()

        if not rows:
            await message.reply('Вакансии с таким названием не найдены.')
        else:
            await message.reply(f'Вот вакансии с названием "{vacancy_title}":')
            for row in rows:
                await message.reply(f'Компания: {row[0]}\nВакансия: {row[1]}\nМестоположение: {row[2]}\nЗарплата: {row[3]}\nСкиллы: {row[4]}\nСсылка: {row[5]}')
