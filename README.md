API Endpoints

| Метод | URL | Опис |
|-------|-----|------|
| GET | `/api/projects/` | Список проектів |
| POST | `/api/projects/` | Створити проект |
| GET | `/api/projects/{id}/` | Деталі проекту |
| PUT | `/api/projects/{id}/` | Оновити проект |
| DELETE | `/api/projects/{id}/` | Видалити проект |
| GET | `/api/places/` | Список місць |
| POST | `/api/places/` | Додати місце |
| PATCH | `/api/places/{id}/` | Оновити місце |

Технології

Django 6.0.2
djangorestframework 3.16.1
drf-yasg 1.21.14

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Потім 
http://localhost:8000/swagger/