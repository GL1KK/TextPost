# 📝 FastAPI Блог с JWT и PostgreSQL

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)

Учебный проект блога на FastAPI с аутентификацией через JWT токены и хранением данных в PostgreSQL. Позволяет создавать, редактировать и удалять текстовые посты, а также искать их по названию.

## 🔐 Безопасность
- JWT аутентификация
- Хеширование паролей
- Защищенные маршруты

## 📝 Посты
- Создание/редактирование
- Поиск по названию
- Удаление своих постов
- Просмотр всех постов

## 💾 База данных
- PostgreSQL
- SQLAlchemy ORM
- Модели пользователей и постов
- Асинхронные запросы

## 🚀 Быстрый старт (не забудьте настроить PostgreSQL перед этим)

```bash
# Клонировать репозиторий
git clone https://github.com/GL1KK/TextPost.git
cd TextPost

# Установить Poetry (если ещё не установлен)
pip install --user poetry

# Установить зависимости
poetry install

# Настроить .env файл (замените значения на свои)
cat > .env <<EOL
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_username
DB_PASS=your_password
DB_NAME=your_dbname
SECRET_JWT_KEY=your_very_secret_key_here
EOL

# Активировать виртуальное окружение Poetry
poetry shell

# Запустить сервер
uvicorn main:app --reload
```

Swagger документация | ReDoc документация
ℹ️ Важная информация

Перед запуском убедитесь, что:

    У вас установлен и запущен PostgreSQL сервер

    Вы создали базу данных с указанным в .env именем

    Пользователь из .env имеет права на доступ к базе

    Порт 5432 (или указанный вами) открыт для подключений

2025 FastAPI Блог | Учебный проект GL1KK 
