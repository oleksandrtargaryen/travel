# Travel Planner API

A simple REST API for planning and tracking travel projects. Add places you want to visit, mark them as visited, and get real-time weather for any saved location.

## Stack

- Python / Django REST Framework
- Google Places API
- OpenWeather API

## Features

- Create and manage travel projects
- Add places via Google Place ID
- Mark places as visited / planning
- Search projects by name or description
- Get current weather for any saved place

## Setup

1. Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
GOOGLE_API_KEY=your_google_api_key
OPEN_WEATHER_API_KEY=your_openweather_api_key
```

3. Run migrations and start the server:
```bash
python manage.py migrate
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET / POST | `/api/projects/` | List / create projects |
| GET / PUT / DELETE | `/api/projects/{id}/` | Project details |
| GET | `/api/projects/search/?q=` | Search projects |
| GET / POST | `/api/places/` | List / create places |
| GET | `/api/places/?project={id}` | Filter places by project |
| GET / PUT / DELETE | `/api/places/{id}/` | Place details |
| PATCH | `/api/places/{id}/` | Mark as visited |
| GET | `/api/places/{id}/get_weather/` | Get weather for place |
