<div align="center" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 800px; margin: 0 auto; color: #333;">
  <h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">📝 FastAPI Блог с JWT и PostgreSQL</h1>
  
  <div style="display: flex; justify-content: center; gap: 15px; margin: 20px 0;">
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
    <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens" alt="JWT">
  </div>

  <div style="background-color: #f8f9fa; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: left;">
    <p>Учебный проект блога на FastAPI с аутентификацией через JWT токены и хранением данных в PostgreSQL. Позволяет создавать, редактировать и удалять текстовые посты, а также искать их по названию.</p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
    <div style="background: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3;">
      <h3 style="margin-top: 0; color: #0d47a1;">🔐 Безопасность</h3>
      <ul style="padding-left: 20px;">
        <li>JWT аутентификация</li>
        <li>Хеширование паролей</li>
      </ul>
    </div>
    
    <div style="background: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
      <h3 style="margin-top: 0; color: #1b5e20;">📝 Посты</h3>
      <ul style="padding-left: 20px;">
        <li>Создание/редактирование</li>
        <li>Поиск по названию</li>
        <li>Удаление своих постов</li>
      </ul>
    </div>
    
    <div style="background: #f3e5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #9c27b0;">
      <h3 style="margin-top: 0; color: #4a148c;">💾 База данных</h3>
      <ul style="padding-left: 20px;">
        <li>PostgreSQL</li>
        <li>SQLAlchemy ORM</li>
        <li>Модели пользователей и постов</li>
      </ul>
    </div>
  </div>

  <h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 5px;">🚀 Быстрый старт(не забудьте настроить postgresql перед этим:))</h2>

  <div style="background-color: #2c3e50; color: white; border-radius: 8px; padding: 15px; text-align: left; margin: 20px 0;">
    <pre style="margin: 0; overflow-x: auto;">
# Клонировать репозиторий
git clone https://github.com/GL1KK/TextPost.git
cd TextPost

# Установить зависимости
pip install poetry
poetry install

# Настроить .env файл
echo "DB_HOST=localhost" > .env
echo "DB_PORT=5432" > .env
echo "DB_PASS=password" > .env
echo "DB_USER=user" > .env
echo "DB_NAME=name" > .env
echo "SECRET_JWT_KEY=ваш-секретный-ключ" >> .env

# Запустить сервер
uvicorn main:app --reload
    </pre>
  </div>

  <div style="margin: 30px 0; text-align: center;">
    <a href="http://127.0.0.1:8000/docs" style="display: inline-block; background-color: #3498db; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; margin: 0 10px;">Swagger документация</a>
    <a href="http://127.0.0.1:8000/redoc" style="display: inline-block; background-color: #2c3e50; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; margin: 0 10px;">ReDoc документация</a>
  </div>
  </div>

  <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee;">
    <p> 2025 FastAPI Блог | Учебный проект /p>
  </div>
</div>