from aiogram import types
from db import connect_db

def register_search_company_handler(dp):
    @dp.message_handler(commands=['search_company'])
    async def search_company(message: types.Message):
        company_name = message.get_args()
        if not company_name:
            await message.reply('Пожалуйста, укажите название компании после команды /search_company.')
            return

        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute("SELECT company, vacancy, location, salary, skills, link FROM vacancies WHERE company ILIKE %s LIMIT 5;", (f'%{company_name}%',))
            rows = cur.fetchall()
        conn.close()

        if not rows:
            await message.reply('Вакансии данной компании не найдены.')
        else:
            await message.reply(f'Вот вакансии компании "{company_name}":')
            for row in rows:
                await message.reply(f'Компания: {row[0]}\nВакансия: {row[1]}\nМестоположение: {row[2]}\nЗарплата: {row[3]}\nСкиллы: {row[4]}\nСсылка: {row[5]}')
