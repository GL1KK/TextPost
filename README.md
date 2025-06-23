<div align="center" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 800px; margin: 0 auto; color: #333;">
  <h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">📝 FastAPI Блог с JWT и PostgreSQL</h1>
  
  <div style="display: flex; justify-content: center; gap: 15px; margin: 20px 0; flex-wrap: wrap;">
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
    <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens" alt="JWT">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white" alt="Poetry">
  </div>

  <div style="background-color: #f8f9fa; border-radius: 8px; padding: 20px; margin: 20px 0; text-align: left; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    <p>Учебный проект блога на FastAPI с аутентификацией через JWT токены и хранением данных в PostgreSQL. Позволяет создавать, редактировать и удалять текстовые посты, а также искать их по названию.</p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
    <div style="background: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
      <h3 style="margin-top: 0; color: #0d47a1;">🔐 Безопасность</h3>
      <ul style="padding-left: 20px;">
        <li>JWT аутентификация</li>
        <li>Хеширование паролей</li>
        <li>Защищенные маршруты</li>
      </ul>
    </div>
    
    <div style="background: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
      <h3 style="margin-top: 0; color: #1b5e20;">📝 Посты</h3>
      <ul style="padding-left: 20px;">
        <li>Создание/редактирование</li>
        <li>Поиск по названию</li>
        <li>Удаление своих постов</li>
        <li>Просмотр всех постов</li>
      </ul>
    </div>
    
    <div style="background: #f3e5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #9c27b0; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
      <h3 style="margin-top: 0; color: #4a148c;">💾 База данных</h3>
      <ul style="padding-left: 20px;">
        <li>PostgreSQL</li>
        <li>SQLAlchemy ORM</li>
        <li>Модели пользователей и постов</li>
        <li>Асинхронные запросы</li>
      </ul>
    </div>
  </div>

  <h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 5px; margin-top: 30px;">🚀 Быстрый старт (не забудьте настроить PostgreSQL перед этим)</h2>

  <div style="background-color: #2c3e50; color: white; border-radius: 8px; padding: 15px; text-align: left; margin: 20px 0; box-shadow: 0 3px 10px rgba(0,0,0,0.2);">
    <pre style="margin: 0; overflow-x: auto; font-family: 'Courier New', monospace; font-size: 14px;">
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
    </pre>
  </div>

  <div style="margin: 30px 0; text-align: center;">
    <a href="http://127.0.0.1:8000/docs" style="display: inline-block; background-color: #3498db; color: white; padding: 12px 25px; border-radius: 5px; text-decoration: none; margin: 0 10px; font-weight: bold; transition: all 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 5px 15px rgba(52, 152, 219, 0.4)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='none';">Swagger документация</a>
    <a href="http://127.0.0.1:8000/redoc" style="display: inline-block; background-color: #2c3e50; color: white; padding: 12px 25px; border-radius: 5px; text-decoration: none; margin: 0 10px; font-weight: bold; transition: all 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 5px 15px rgba(44, 62, 80, 0.4)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='none';">ReDoc документация</a>
  </div>

  <div style="background-color: #e8f4f8; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    <h3 style="margin-top: 0; color: #0d47a1;">ℹ️ Важная информация</h3>
    <p>Перед запуском убедитесь, что:</p>
    <ul style="padding-left: 20px;">
      <li>У вас установлен и запущен PostgreSQL сервер</li>
      <li>Вы создали базу данных с указанным в .env именем</li>
      <li>Пользователь из .env имеет права на доступ к базе</li>
      <li>Порт 5432 (или указанный вами) открыт для подключений</li>
    </ul>
  </div>

  <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; color: #7f8c8d; font-size: 14px;">
    <p>© 2024 FastAPI Блог | Учебный проект GL1KK | MIT License</p>
  </div>
</div>
