[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=quick+start )](https://git.io/typing-svg)

## Документация по развертыванию проекта 


### Шаги по развертыванию с помощью docker

1. Клонируйте репозиторий

2. Создайте файл `.env` в корневой директории проекта 
    ```
    # ===== DJANGO НАСТРОЙКИ =====
    DEBUG=0
    ALLOWED_HOSTS=localhost
    SECRET_KEY=django-insecure-6s+g7%cdw%g#)n)_380$sz-l$0laa)c)jr2vtdb17&l)fg16s7
    IN_DOCKER=true

    # ===== БАЗА ДАННЫХ =====
    POSTGRES_DB=db_87
    POSTGRES_USER=user_87
    POSTGRES_PASSWORD=password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

    # ===== CELERY НАСТРОЙКИ =====
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    ```

3. Соберите и запустите контейнеры:
   ```
   docker-compose up --build
   ```
4. Создайте суперпользователя для доступа к админпанели
   ```
   docker-compose exec app sh
   ```
   ```
   python manage.py createsuperuser
   ```

## После успешного запуска, приложение будет доступно по адресу:
   - Nginx: http://localhost
   

### Шаги по развертыванию локально для разработки

1. Клонируйте репозиторий

2. Создайте и активируйте виртальное окружение
    ```
    python3 -m venv venv
    ```
    ```
    source venv/bin/activate
    ```
3. Перейдите в дирректорию  src  и установите зависимости
    ```
    cd src
    ```
    ```
    pip install -r requirements.txt
    ```
4. Сделайте миграции для sqlite
    ```
    python manage.py migrate
    ```
5. Запустите сервер
    ```
    DJANGO_SETTINGS_MODULE=config.dev_settings python manage.py runserver
    ```
6. Запустите redis
    ```
    redis-server
    ```
7. В директории src  запустите celery
    ```
    celery -A celery_app worker -l INFO
    ```
8. В директории src  запустите flower
    ```
    celery -A celery_app flower --port=5555
    ```
## После успешного запуска, приложение будет доступно по адресу:
   - Django: http://localhost:8000

# quick_start
