import httpx
import os
from typing import Dict, Any

GOOGLE_PLACES_API_KEY = os.environ.get('GOOGLE_API_KEY')
OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')


class GooglePlacesOpenWeatherService:
    GOOGLE_BASE_URL = "https://maps.googleapis.com/maps/api/place/details/json"
    WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    async def get_place_with_weather(place_id: str) -> Dict[str, Any]:
        if not GOOGLE_PLACES_API_KEY or not OPEN_WEATHER_API_KEY:
            raise ValueError("API keys are not configured")

        async with httpx.AsyncClient() as client:
            try:
                place_res = await client.get(
                    GooglePlacesOpenWeatherService.GOOGLE_BASE_URL,
                    params={
                        "place_id": place_id,
                        "fields": "name,geometry,formatted_address,rating",
                        "key": GOOGLE_PLACES_API_KEY,
                    },
                )
                place_res.raise_for_status()
            except httpx.HTTPStatusError as e:
                raise ValueError(f"Google Places request failed: {e.response.status_code}")

            place_json = place_res.json()

            if place_json.get("status") != "OK":
                raise ValueError(f"Google API Error: {place_json.get('status')}")

            result = place_json["result"]
            loc = result["geometry"]["location"]
            lat, lng = loc["lat"], loc["lng"]

            try:
                weather_res = await client.get(
                    GooglePlacesOpenWeatherService.WEATHER_BASE_URL,
                    params={
                        "lat": lat,
                        "lon": lng,
                        "appid": OPEN_WEATHER_API_KEY,
                        "units": "metric",
                    },
                )
                weather_res.raise_for_status()
            except httpx.HTTPStatusError as e:
                raise ValueError(f"OpenWeather request failed: {e.response.status_code}")

            w_data = weather_res.json()

            return {
                "name": result.get("name"),
                "address": result.get("formatted_address"),
                "rating": result.get("rating"),
                "lat": lat,
                "lng": lng,
                "weather": {
                    "temp": w_data["main"]["temp"],
                    "feels_like": w_data["main"]["feels_like"],
                    "humidity": w_data["main"]["humidity"],
                    "description": w_data["weather"][0]["description"],
                }
            }