# BT

Проект реализует API для расчёта стоимости страховых полисов, создания заявок и управления пользователями с использованием Django REST Framework и JWT-аутентификацией.

---

## 🔹 Основные возможности

### Пользователи
- Регистрация (`POST auth/register/`)
- Логин (`POST auth/login/`) с JWT
- Логаут (`POST auth/logout/`) с блокировкой refresh-токена

### Страховые расчёты (`Quotes`)
- `POST quotes/` — расчёт стоимости полиса по параметрам:
  - `tariff`: тариф (`econom`, `standart`, `premium`)
  - `age`: возраст водителя
  - `experience`: стаж вождения
  - `car_type`: тип автомобиля (`car`, `truck`, `moto`)
- `GET quotes/{id}/` — просмотр ранее рассчитанного полиса
- `price` — рассчитывается автоматически на основе коэффициентов
- Валидация данных:
  - `age >= 18`
  - `experience >= 0`
  - `experience <= age`
  - `car_type` только из допустимого списка

### Заявки (`Applications`)
- `POST applications/` — создать заявку на полис:
  - `full_name`
  - `phone` (формат `+992XXXXXXXXX`)
  - `email`
  - `tariff`
  - `quote_id` (ID расчёта)
- `GET applications/{id}/` — просмотр заявки авторизованным пользователем
- Валидация данных и единый формат ошибок

---

### Коэффициенты расчёта
- Параметр	Значение
- Тариф	
- econom	1.0
- standart	1.2
- premium	1.5
- Тип авто	
- car	    1.0
- truck	    1.5
- moto	    1.3
- Возраст водителя	
- < 25	×1.3
- Стаж водителя	
- > 5	×0.9
- Базовая цена	10000

---

## 🔹 Технологии
- Python 3.12
- Django 5
- Django REST Framework
- JWT-аутентификация (`djangorestframework-simplejwt`)
- PostgreSQL (Docker)
- Redis (Docker, для блокировки refresh-токенов)
- Swagger / drf-yasg для документации API

---

## 🔹 Запуск проекта с Docker

```bash
docker-compose up -d
