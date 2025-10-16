# 💰 Finance Tracker API

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ffffff?style=for-the-badge&logo=sqlalchemy&logoColor=black)

</div>

## 📖 Описание

REST API для учета личных финансов с полным набором функций для управления доходами и расходами. Проект реализован на FastAPI с использованием SQLite базы данных.

## 🚀 Возможности

- ✅ **CRUD операции** - полное управление финансовыми операциями
- ✅ **SQLite база данных** - легковесное хранение данных
- ✅ **SQLAlchemy ORM** - объектно-реляционное отображение
- ✅ **Валидация данных** - надежная обработка входящих данных
- ✅ **Документация API** - автоматическая генерация Swagger/Redoc
- ✅ **Асинхронность** - высокая производительность

## 🛠 Технологии

- **Backend**: Python 3.11, FastAPI, SQLAlchemy, Pydantic
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **API Documentation**: автоматическая генерация через FastAPI

## 📦 Быстрый старт

### Предварительные требования
- Python 3.8+
- pip (менеджер пакетов Python)

### Установка и запуск

```bash
# Клонирование репозитория
git clone https://github.com/GudAlex61/finance-tracker.git
cd finance-tracker

# Установка зависимостей
pip install -r requirements.txt

# Запуск приложения
uvicorn app.main:app --reload
```

После запуска приложение будет доступно по адресам:
- 🚀 **API**: http://localhost:8000
- 📚 **Документация Swagger**: http://localhost:8000/docs
- 📖 **Документация ReDoc**: http://localhost:8000/redoc

## 🔧 API Endpoints

### Финансовые операции
| Метод | URL | Описание |
|-------|-----|----------|
| `GET` | `/operations` | Получить все операции |
| `POST` | `/operations` | Создать новую операцию |
| `GET` | `/operations/{id}` | Получить операцию по ID |
| `PUT` | `/operations/{id}` | Обновить операцию |
| `DELETE` | `/operations/{id}` | Удалить операцию |

### Примеры запросов

**Создание операции:**
```bash
curl -X POST "http://localhost:8000/operations" \
-H "Content-Type: application/json" \
-d '{
  "amount": 1500.50,
  "category": "products",
  "type": "expense",
  "date": "2024-01-15",
  "description": "Покупка продуктов"
}'
```

**Получение всех операций:**
```bash
curl -X GET "http://localhost:8000/operations"
```

## 🗂 Структура проекта

```
finance-tracker/
├── app/
│   ├── __init__.py
│   ├── main.py              # Основной файл приложения
│   ├── database.py          # Настройка базы данных
│   ├── models.py            # SQLAlchemy модели
│   ├── schemas.py           # Pydantic схемы
│   └── crud.py              # CRUD операции
├── requirements.txt         # Зависимости проекта
└── README.md               # Документация
```

## 🧪 Тестирование

Для тестирования API вы можете использовать:

1. **Swagger UI** (http://localhost:8000/docs) - интерактивная документация
2. **curl** команды (примеры выше)
3. **Postman** или аналогичные инструменты

## 👨‍💻 Разработка

### Установка для разработки

```bash
# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск в режиме разработки
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Основные зависимости
- `fastapi` - современный веб-фреймворк
- `sqlalchemy` - ORM для работы с базой данных
- `uvicorn` - ASGI сервер для запуска приложения

## 📊 Модель данных

### Операция (Operation)
- `id` - уникальный идентификатор
- `amount` - сумма операции
- `category` - категория операции
- `type` - тип операции (income/expense)
- `date` - дата операции
- `description` - описание операции

## 🚀 Планы по развитию

- [ ] Добавить аутентификацию пользователей
- [ ] Реализовать категории операций
- [ ] Добавить статистику и аналитику
- [ ] Реализовать экспорт данных в CSV
- [ ] Добавить систему бюджетирования
- [ ] Реализовать Docker контейнеризацию
