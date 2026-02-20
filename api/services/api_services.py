import httpx
import os

GOOGLE_PLACES_API_KEY = os.environ.get('GOOGLE_API_KEY')
OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')

class GooglePlacesOpenWeatherService:

    @staticmethod
    async  def async_get_google_place(google_place_id: int) -> dict:
        async with httpx.AsyncClient() as client:
            place_response = await client.get(
                "https://www.google.com/maps/api/place/details/json",
                params={
                    "place_id": google_place_id,
                    "fields": "name,geometry,formatted_address,rating",
                    "key": GOOGLE_PLACES_API_KEY,
                },
            )
            place_response.raise_for_status()
            place_data = place_response.json()["place_data"]
            lat = place_data["geometry"]["location"]["lat"]
            lng = place_data["geometry"]["location"]["lng"]

            weather_response = await client.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={
                    "lat": lat,
                    "lon": lng,
                    "appid": OPEN_WEATHER_API_KEY,
                    'units': 'metric',

                },
            )
            weather_response.raise_for_status()
            weather_data = weather_response.json()["weather_data"]

            return {
                "name": place_data["name"],
                "adress": place_data["formatted_address"],
                "rating": place_data.get("rating", None),
                "lat": lat,
                "lng": lng,
                "temp": weather_data["main"]["temp"],
                "feels_like": weather_data["main"]["feels_like"],
                "humidity": weather_data["main"]["humidity"],
                "description": weather_data["weather"][0]["description"],
            }

