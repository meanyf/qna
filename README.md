# Запуск проекта

## 1. Запуск базы данных
```bash
docker-compose -f docker-compose.yml up -d db
```

## 2. Запуск без Docker
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload

```

## 3. Запуск через Docker. Перейдите по адресу localhost:8000
```bash
docker-compose -f docker-compose.yml build app
docker-compose -f docker-compose.yml run --rm --service-ports app
```


## 4. Очистка ресурсов
```bash
# Удалить БД
docker-compose -f docker-compose.yml stop db
docker-compose -f docker-compose.yml rm -f db
docker volume rm vtb-2_postgres_data2

# Удалить приложение
docker-compose -f docker-compose.yml stop app
docker-compose -f docker-compose.yml rm -f app

# Удалить образ
docker rmi vtb-python-app
```