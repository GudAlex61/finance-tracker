# 💰 Finance Tracker API

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ffffff?style=for-the-badge&logo=sqlalchemy&logoColor=black)
![Pydantic](https://img.shields.io/badge/Pydantic-ffffff?style=for-the-badge&logo=pydantic&logoColor=black)

</div>

## 📖 Описание

REST API для учета личных финансов с полной системой аутентификации и управления транзакциями. Проект реализован на FastAPI с использованием SQLite базы данных и SQLAlchemy ORM.

## 🚀 Возможности

- ✅ **Аутентификация пользователей** - HTTP Basic Auth для защиты API
- ✅ **Управление транзакциями** - полный CRUD для финансовых операций
- ✅ **SQLite база данных** - легковесное хранение данных
- ✅ **SQLAlchemy ORM** - объектно-реляционное отображение
- ✅ **Валидация данных** - надежная обработка входящих данных с Pydantic
- ✅ **Документация API** - автоматическая генерация Swagger/Redoc
- ✅ **CORS поддержка** - интеграция с фронтенд приложениями
- ✅ **Логирование** - детальное логирование операций

## 🛠 Технологии

- **Backend**: Python 3.8+, FastAPI, SQLAlchemy, Pydantic
- **Authentication**: HTTP Basic Auth, bcrypt для хеширования паролей
- **Database**: SQLite с возможностью миграции на PostgreSQL
- **ORM**: SQLAlchemy 2.0
- **API Documentation**: автоматическая генерация через FastAPI
- **Testing**: Pytest, TestClient

## 📦 Быстрый старт

### Предварительные требования
- Python 3.8+
- pip (менеджер пакетов Python)

### Установка и запуск

```bash
# Клонирование репозитория
git clone <your-repo-url>
cd server

# Создание виртуального окружения (рекомендуется)
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
# myenv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt

# Запуск приложения
uvicorn app.main:app --reload
```

После запуска приложение будет доступно по адресам:
- 🚀 **API**: http://localhost:8000
- 📚 **Документация Swagger**: http://localhost:8000/docs
- 📖 **Документация ReDoc**: http://localhost:8000/redoc

## 🔐 Аутентификация

API использует HTTP Basic Authentication. Для доступа к защищенным эндпоинтам необходимо:

1. Зарегистрировать пользователя через `/register`
2. Использовать username и password для Basic Auth

Пример заголовка авторизации:
```
Authorization: Basic dGVzdHVzZXI6dGVzdHBhc3N3b3Jk
```

## 🔧 API Endpoints

### Аутентификация и пользователи
| Метод | URL | Описание | Аутентификация |
|-------|-----|----------|----------------|
| `POST` | `/register` | Регистрация нового пользователя | ❌ |
| `POST` | `/login` | Вход в систему (Basic Auth) | ❌ |
| `GET` | `/users/me` | Получить информацию о текущем пользователе | ✅ |

### Управление транзакциями
| Метод | URL | Описание | Аутентификация |
|-------|-----|----------|----------------|
| `GET` | `/transactions/` | Получить все транзакции пользователя | ✅ |
| `POST` | `/transactions/` | Создать новую транзакцию | ✅ |
| `DELETE` | `/transactions/{id}` | Удалить транзакцию по ID | ✅ |

### Системные endpoints
| Метод | URL | Описание |
|-------|-----|----------|
| `GET` | `/` | Стартовая страница API |
| `GET` | `/health` | Проверка здоровья приложения |

## 📝 Примеры использования

### Регистрация пользователя
```bash
curl -X POST "http://localhost:8000/register" \
-H "Content-Type: application/json" \
-d '{
  "username": "alex",
  "email": "alex@example.com",
  "password": "securepassword"
}'
```

### Создание транзакции (с аутентификацией)
```bash
curl -X POST "http://localhost:8000/transactions/" \
-H "Content-Type: application/json" \
-H "Authorization: Basic $(echo -n 'alex:securepassword' | base64)" \
-d '{
  "amount": 1500.50,
  "description": "Покупка продуктов",
  "category": "food",
  "type": "expense",
  "date": "2024-01-15T10:30:00"
}'
```

### Получение транзакций пользователя
```bash
curl -X GET "http://localhost:8000/transactions/" \
-H "Authorization: Basic $(echo -n 'alex:securepassword' | base64)"
```

## 🗂 Структура проекта

```
server/
├── app/
│   ├── __init__.py
│   ├── main.py              # Основное приложение FastAPI
│   ├── database.py          # Настройка базы данных и подключения
│   ├── models.py            # SQLAlchemy модели (User, Transactions)
│   ├── schemas.py           # Pydantic схемы для валидации
│   ├── crud.py              # CRUD операции с базой данных
│   └── auth.py              # Аутентификация и хеширование паролей
├── tests/
│   ├── conftest.py          # Фикстуры для тестирования
│   ├── test_main.py         # Тесты основных endpoints
│   ├── test_auth.py         # Тесты аутентификации
│   ├── test_crud.py         # Тесты CRUD операций
│   ├── test_database.py     # Тесты базы данных
│   └── test_models.py       # Тесты моделей
├── requirements.txt         # Зависимости проекта
└── README.md               # Документация
```

## 🧪 Тестирование

Проект включает полный набор тестов:

```bash
# Запуск всех тестов
pytest tests/

# Запуск с подробным выводом
pytest tests/ -v

# Запуск конкретного модуля тестов
pytest tests/test_auth.py -v

# Запуск с покрытием кода
pytest --cov=app --cov-report=html
```

## 🔧 Модели данных

### Пользователь (User)
- `id` - уникальный идентификатор
- `username` - имя пользователя (уникальное)
- `email` - email адрес (уникальный)
- `hashed_password` - хешированный пароль

### Транзакция (Transactions)
- `id` - уникальный идентификатор
- `amount` - сумма транзакции
- `description` - описание транзакции
- `category` - категория транзакции
- `type` - тип транзакции (income/expense)
- `date` - дата транзакции
- `user_id` - ID пользователя (внешний ключ)

## 🚀 Планы по развитию

- [ ] Добавить JWT аутентификацию
- [ ] Реализовать категории транзакций
- [ ] Добавить финансовую аналитику и отчеты
- [ ] Реализовать экспорт данных в CSV/Excel
- [ ] Добавить систему бюджетов и целей
- [ ] Реализовать Docker контейнеризацию
- [ ] Добавить миграции базы данных с Alembic
- [ ] Интегрировать кэширование с Redis
- [ ] Добавить фоновые задачи для аналитики

## 👨‍💻 Разработка

### Установка для разработки

```bash
# Активация виртуального окружения
source myenv/bin/activate  # Linux/Mac
# myenv\Scripts\activate  # Windows

# Установка зависимостей разработки
pip install -r requirements.txt

# Запуск в режиме разработки
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Основные зависимости
- `fastapi` - современный веб-фреймворк
- `sqlalchemy` - ORM для работы с базой данных
- `uvicorn` - ASGI сервер для запуска приложения
- `pydantic` - валидация данных и схемы
- `python-jose` - JWT токены (для будущего развития)
- `passlib` - хеширование паролей
- `pytest` - фреймворк для тестирования
