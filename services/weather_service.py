import requests
from utils.config import API_KEY

def get_weather(city="Mumbai"):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=5)

        data = response.json()

        if str(data.get("cod")) != "200":
            return None

        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "wind": data["wind"]["speed"]
        }

    except Exception:
        return None