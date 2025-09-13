import psycopg
from docker_utils import is_container_running

# Настройки для подключения к базе данных
dbname = "qna_db"
user = "postgres"
password = "postgres"
host = 'localhost'
port = 5435
connection = None  # Инициализируем переменную connection заранее
db_is_running = is_container_running("postgres15")
app_is_running = is_container_running("qna-fastapi")
if db_is_running and app_is_running:
    host = "postgres15"
elif db_is_running and not app_is_running:
    host = "localhost"
elif not db_is_running and app_is_running:
    host = "host.docker.internal" if host.lower() == 'localhost' else host
    
try:
    # Устанавливаем соединение с базой данных
    connection = psycopg.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )

    print("Успешное подключение к базе данных!")

except Exception as e:
    print(f"Ошибка при подключении к базе данных: {e}")

finally:
    # Закрываем соединение после выполнения операций
    if connection:
        connection.close()
        print("Соединение с базой данных закрыто.")
