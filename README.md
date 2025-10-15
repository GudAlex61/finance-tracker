# 💰 Finance Tracker API

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ffffff?style=for-the-badge&logo=sqlalchemy&logoColor=black)

</div>

## 📖 Описание

REST API для учета личных финансов с полным набором функций для управления доходами, расходами и категориями. Проект реализован на современном стеке технологий с использованием асинхронного подхода.

## 🚀 Возможности

- ✅ **JWT аутентификация** - безопасный вход и регистрация
- ✅ **CRUD операции** - полное управление транзакциями
- ✅ **Категории расходов** - гибкая система категоризации
- ✅ **Валидация данных** - надежная обработка входящих данных
- ✅ **Документация API** - автоматическая генерация Swagger/Redoc
- ✅ **Контейнеризация** - легкий запуск через Docker
- ✅ **Асинхронность** - высокая производительность

## 🛠 Технологии

- **Backend**: Python 3.11, FastAPI, SQLAlchemy, Pydantic
- **Database**: PostgreSQL, SQLAlchemy ORM
- **Auth**: JWT tokens, bcrypt
- **DevOps**: Docker, Docker Compose
- **Testing**: Pytest, pytest-asyncio

## 📦 Быстрый старт

### Предварительные требования
- Docker и Docker Compose

### Запуск проекта

```bash
# Клонирование репозитория
git clone https://github.com/GudAlex61/finance-tracker

# Запуск всех сервисов
docker-compose up --build
```

После запуска приложение будет доступно по адресам:
- 🚀 **API**: http://localhost:8000
- 📚 **Документация**: http://localhost:8000/docs
- 📖 **Альтернативная документация**: http://localhost:8000/redoc

## 🔧 API Endpoints

### Аутентификация
| Метод | URL | Описание |
|-------|-----|----------|
| `POST` | `/api/v1/auth/register` | Регистрация пользователя |
| `POST` | `/api/v1/auth/login` | Вход в систему |
| `POST` | `/api/v1/auth/refresh` | Обновление токена |

### Транзакции
| Метод | URL | Описание |
|-------|-----|----------|
| `GET` | `/api/v1/transactions` | Получить все транзакции |
| `POST` | `/api/v1/transactions` | Создать транзакцию |
| `GET` | `/api/v1/transactions/{id}` | Получить транзакцию по ID |
| `PUT` | `/api/v1/transactions/{id}` | Обновить транзакцию |
| `DELETE` | `/api/v1/transactions/{id}` | Удалить транзакцию |

### Категории
| Метод | URL | Описание |
|-------|-----|----------|
| `GET` | `/api/v1/categories` | Получить все категории |
| `POST` | `/api/v1/categories` | Создать категорию |

## 🗂 Структура проекта

```
finance-tracker/
├── app/
│   ├── api/           # API endpoints
│   ├── core/          # Конфигурация и утилиты
│   ├── models/        # SQLAlchemy модели
│   ├── schemas/       # Pydantic схемы
│   └── services/      # Бизнес-логика
├── tests/             # Тесты
├── requirements.txt   # Зависимости
├── Dockerfile        # Docker конфигурация
└── docker-compose.yml # Оркестрация
```

## 🧪 Тестирование

```bash
# Запуск тестов
docker-compose exec api pytest

# Запуск с покрытием
docker-compose exec api pytest --cov=app tests/
```

## 👨‍💻 Разработка

### Установка для разработки

```bash
# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Установка зависимостей
pip install -r requirements.txt

# Запуск в режиме разработки
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📊 Планы по развитию

- [ ] Добавить статистику и аналитику
- [ ] Реализовать экспорт данных в CSV/Excel
- [ ] Добавить бюджетирование и цели
- [ ] Интеграция с банковскими API
- [ ] Мобильное приложение


