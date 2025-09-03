FROM python:3.12-slim

# Установка зависимостей и netcat
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Делаем entrypoint.sh исполняемым
RUN chmod +x /app/entrypoint.sh
RUN python manage.py collectstatic --noinput

CMD ["sh", "/app/entrypoint.sh"]
