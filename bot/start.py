from aiogram import types

def register_start_handler(dp):
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await message.reply('Используйте /search <запрос>, чтобы искать вакансии.\nДля остального функционала можно задействовать /help')
