from aiogram import types
from db import connect_db

def register_count_handler(dp):
    @dp.message_handler(commands=['count'])
    async def count(message: types.Message):
        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM vacancies;")
            count = cur.fetchone()[0]
        conn.close()

        await message.reply(f'В базе данных {count} вакансий.')
