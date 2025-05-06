# Sladkiy Parsing Bot

Telegram-бот для поиска вакансий разработчика с сайта [Habr Career](https://career.habr.com).

---

## Возможности

- `/search <запрос>` — парсит новые вакансии по ключевым словам и сохраняет их в базу
- `/recent` — выводит 5 случайных вакансий из базы
- `/count` — показывает общее количество вакансий
- `/grafic` — строит график по режимам работы (удалёнка, офис и т.д.)
- `/search_company` — поиск вакансий по названию компании
- `/search_vacancy` — поиск по названию вакансии

---

## Технологии

- **Язык**: Python
- **Библиотеки**: aiogram, Selenium, psycopg2, matplotlib
- **База данных**: PostgreSQL
- **Инфраструктура**: Docker, Docker Compose

---

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/sladkiy-parsing-bot.git
cd sladkiy-parsing-bot
