# ProjectAI — Веб-приложение проектной компании с ИИ (демо)

## Структура
- backend/ — FastAPI приложение
- frontend/ — React + Vite frontend
- docker-compose.yml — пример компоновки сервисов

## Быстрый запуск (локально)
### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Docker
```bash
docker-compose up --build
```

## Примечания
- В демо используется SQLite для удобства. Для продакшн-релиза переключите на PostgreSQL и настройте миграции.
- AI-модуль — демонстрационный и rule-based. Для производственных задач рекомендовано собрать данные и обучить модель.
