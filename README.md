# Book Catalog API

REST API для управления пользователями, книгами и авторами на FastAPI + SQLAlchemy + SQLite.

### 🚀 Быстрый старт
>
> 1. Клонируйте репозиторий и перейдите в папку проекта:
>    
>    ```python
>    git clone <>
>    ```
>    ```python
>    cd book_catalog
>    ```

> 2. Создайте и активируйте виртуальное окружение (рекомендуется):
>    
>    ```python
>    python -m venv venv
>    ```
>    * Для Windows:
>    ```python
>    venv\Scripts\activate
>    ```
>    * Для Linux/Mac:
>    ```python
>    source venv/bin/activate
>    ```
>
> 3. Установите зависимости:
>    
>    ```python
>    pip install -r requirements.txt
>    ```
>    Если файла requirements.txt нет, установите вручную:
>    ```python
>    pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose pydantic
>    ```

>
> 4. Запустите приложение:
>    
>    ```python
>    uvicorn app.main:app --reload
>    ```
>    Приложение будет доступно по адресу: http://127.0.0.1:8000/
>
> 5. Документация API:
>    
>    Swagger UI: http://127.0.0.1:8000/docs  <br> ReDoc: http://127.0.0.1:8000/redoc
>  
>    
>
>## 🧪 Запуск тестов
>    ```python
>    pytest
>    ```
>## 📂 Структура проекта
>book_catalog/<br>
>│<br>
>├── app/<br>
>│   ├── main.py<br>
>│   ├── models.py<br>
>│   ├── schemas.py<br>
>│   ├── crud.py<br>
>│   ├── database.py<br>
>│   ├── security.py<br>
>│   └── routers/<br>
>│       ├── users.py<br>
>│       ├── authors.py<br>
>│       ├── books.py<br>
>│       └── business.py<br>
>│<br>
>├── tests/<br>
>│   └── test_main.py<br>
>│<br>
>├── books.db<br>
>└── README.md<br>
>## ⚙️ Основные возможности
>* Регистрация и аутентификация пользователей (JWT)
>
>* CRUD для авторов и книг
>
>* Связь книг с авторами
>
>* Документированное API
>
>## 💡 Примечания
>* По умолчанию используется SQLite (books.db).

>* Все данные хранятся локально, база создаётся автоматически при первом запуске.

>* Для доступа к защищённым эндпоинтам требуется JWT-токен (получается при логине).
>## 🛠️ Частые команды
>* Запуск сервера:
>    ```python
>    uvicorn app.main:app --reload
>    ```
>* Запуск тестов:
>    ```python
>    pytest
>    ```
>## 📝 Автор
> <b> Кульпин Николай Романович

