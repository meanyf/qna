import docker


def is_container_running(container_name_or_id):
    try:
        # Создаем объект клиента Docker
        client = docker.from_env()

        # containers = client.containers.list(all=True)

        # if containers:
        #     print("Список всех контейнеров:")
        #     for container in containers:
        #         print(f"ID: {container.id}, Имя: {container.name}, Статус: {container.status}")
        # else:
        #     print("Контейнеры не найдены.")

        # Получаем контейнер по имени или ID
        container = client.containers.get(container_name_or_id)

        # Проверяем состояние контейнера
        if container.status == "running":
            print(f"{container_name_or_id} is running")
            return True
        else:
            print(f"{container_name_or_id} is closed")
            return False
    except docker.errors.NotFound:
        # Контейнер не найден
        print(f"{container_name_or_id} not found")
        return False
    except docker.errors.DockerException as e:
        # Ошибка при взаимодействии с Docker
        print(f"Ошибка при взаимодействии с Docker: {e}")
        return False


def docker_status(container_name_or_id):
    if is_container_running(container_name_or_id):
        print(f"Контейнер с именем или ID '{container_name_or_id}' запущен.")
    else:
        print(
            f"Контейнер с именем или ID '{container_name_or_id}' не найден или не запущен."
        )
