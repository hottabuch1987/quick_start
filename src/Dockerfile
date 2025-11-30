
FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Базовые системные зависимости
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    # Устанавливаем зависимости для Postgre
    && apk add postgresql-dev gcc python3-dev musl-dev


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /usr/src/app/db
RUN mkdir -p /usr/src/app/logs

# Создаем пользователя
RUN adduser -D -u 1000 appuser
RUN chown -R appuser:appuser /usr/src/app
USER appuser

CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput"]