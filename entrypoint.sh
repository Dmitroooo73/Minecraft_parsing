#!/bin/bash

# Запуск миграции базы данных
python migrate_vacancies.py

# Запуск бота
python main.py
