import logging
import asyncio
import concurrent.futures
from aiogram import types
from db import connect_db
from parsing import parse_habr

async def run_parse_habr(query: str):
    loop = asyncio.get_event_loop()
    executor = concurrent.futures.ThreadPoolExecutor()
    await loop.run_in_executor(executor, parse_habr, query)

def register_search_handler(dp):
    @dp.message_handler(commands=['search'])
    async def search(message: types.Message):
        query = message.get_args()
        logging.info(f"Получен запрос для поиска: {query}")
        if not query:
            await message.reply('Пожалуйста, введите запрос после команды /search.')
            return

        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM vacancies;")
            initial_count = cur.fetchone()[0]
        conn.close()

        await message.reply(f'Ищу вакансии для: {query}')
        await run_parse_habr(query)
        await message.reply('Поиск завершен. Проверьте свою базу данных.')

        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute("SELECT company, vacancy, location, salary, skills, link FROM vacancies WHERE id > %s ORDER BY id LIMIT 5;", (initial_count,))
            rows = cur.fetchall()
        conn.close()

        if not rows:
            await message.reply('Новые вакансии не найдены.')
        else:
            await message.reply('Ниже представлены 5 новых вакансий:')
            for row in rows:
                await message.reply(f'Компания: {row[0]}\nВакансия: {row[1]}\nМестоположение: {row[2]}\nЗарплата: {row[3]}\nСкиллы: {row[4]}\nСсылка: {row[5]}')
