[EN](#-en)  
[RU](#-ru)

# 🇬🇧 EN
## 📦 PromptBOX is Under Development  
[📈 Progress](#-progress)  
[🛠️ Tech Stack](#️-tech-stack)  
[🚀 Getting Started](#-getting-started) 

---

## 📈 Progress
**Backend**: 100%  
**Frontend**: 25%

## 🛠️ Tech Stack
### ⚙️ Backend
**Database**: PostgreSQL 🐘  
**Language**: Python 🐍  
**Framework**: FastAPI ⚡️  
**Containerization**: Docker 🐋  
**ORM**: SQLAlchemy ⚗️  
**Auth**: JWT (python-jose) 🔒  
**Package Manager**: Poetry 🎨  
**Templating**: Jinja2 ⛩️

### 🎆 Frontend  
**Language**: TypeScript ✨  
**Framework**: React ⚛️  
**Bundler**: Vite ⚡️

## 🚀 Getting Started
First, clone the repository:
```
git clone https://github.com/PixisProd/project-PB.git
cd project-PB
```
Prepare the `.env` file. For your convenience, a pre-filled `.env.example` is provided. Create a `.env` file and copy the contents of the `.env.example` into it.

### 🐋 Docker (Recommended)
From the project root, run:
```
docker-compose up
```
The project will be available at `http://your.ip.address:8000/docs`.

### 🧤 Manual Launch
Install all dependencies using Poetry:
```
pip install poetry
poetry install --no-root
```
Then run the project:
```
poetry run uvicorn server.src.main:app --reload
```
The API will be available at: `http://localhost:8000/docs`

# 🇷🇺 RU
## 📦 PromptBOX находится в разработке  
[📈 Прогресс](#-прогресс)  
[🛠️ Стек технологий](#️-стек-технологий)  
[🚀 Запуск](#-запуск) 

---

## 📈 Прогресс
**Backend**: 100%  
**Frontend**: 25%

## 🛠️ Стек технологий
### ⚙️ Backend
**База данных**: PostgreSQL 🐘  
**Язык**: Python 🐍  
**Фреймворк**: FastAPI ⚡️  
**Контейнеризация**: Docker 🐋  
**ORM**: SQLAlchemy ⚗️  
**Авторизация**: JWT (python-jose) 🔒  
**Пакетный менеджер**: Poetry 🎨  
**Другое**: Jinja2 ⛩️ 

### 🎆 Frontend  
**Язык**: TypeScript ✨   
**Фреймворк**: React ⚛️  
**Сборщик**: Vite ⚡️

## 🚀 Запуск
Для начала склонируйте репозиторий:
```
git clone https://github.com/PixisProd/project-PB.git
cd project-PB
```
Подготовьте `.env` файл, для удобства я заполнил `.env.example`. Для запуска по умолчанию достаточно создать `.env` в корне проекта и скопировать в него содержимое `.env.example`.

### 🐋 Docker (предпочтительный вариант)
Достаточно из корня проекта запустить команду:
```
docker-compose up
```
И проект запустится по адресу `http://your.ip.address:8000/docs`.

### 🧤 Запуск вручную
Нужно установить все зависимости (poetry):
```
pip install poetry
poetry install --no-root
```
После чего можно запускать проект:
```
poetry run uvicorn server.src.main:app --reload
```
API будет доступен по адресу `http://localhost:8000/docs`