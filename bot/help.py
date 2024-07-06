from aiogram import types

def register_help_handler(dp):
    @dp.message_handler(commands=['help'])
    async def help(message: types.Message):
        await message.reply('Краткая сводка по командам\n/start - запуск/перезапуск бота\n/search <запрос> - поиск вакансий по запросу\n/recent - вывод 5 случайных вакансий\n/count - вывод общего кол-ва вакансий в бд\n/grafic - вывод на выбор режима раб. дня\n/search_company - поиск вакансий по компании из бд\n/search_vacancy - поиск вакансий по названию вакансии из бд')
