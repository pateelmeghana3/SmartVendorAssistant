from flask import Blueprint, render_template, request, redirect, session
from utils.config import API_KEY
import requests

weather_bp = Blueprint("weather", __name__)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ==========================================================
# GENERATE BUSINESS RECOMMENDATIONS
# ==========================================================

def get_recommendations(weather):

    recommendations = []

    condition = weather["condition"].lower()
    temp = weather["temp"]

    # Rain
    if "rain" in condition or "drizzle" in condition:
        recommendations.append("☔ Increase umbrella stock.")
        recommendations.append("🧥 Keep raincoats available.")
        recommendations.append("☕ Promote hot beverages.")

    # Hot Weather
    if temp >= 35:
        recommendations.append("🥤 Increase cold drinks inventory.")
        recommendations.append("🍦 Stock more ice cream.")
        recommendations.append("🧃 Promote juices and water bottles.")

    # Pleasant Weather
    if 25 <= temp < 35:
        recommendations.append("🥤 Normal demand expected.")
        recommendations.append("🛒 Maintain regular stock levels.")

    # Cold Weather
    if temp < 20:
        recommendations.append("☕ Increase tea and coffee stock.")
        recommendations.append("🧥 Winter clothing demand may rise.")

    # High Humidity
    if weather["humidity"] >= 80:
        recommendations.append("💧 Humid weather may increase cold drink sales.")

    if not recommendations:
        recommendations.append("✅ No special inventory recommendations today.")

    return recommendations


# ==========================================================
# WEATHER AI
# ==========================================================

@weather_bp.route("/weather_ai", methods=["GET", "POST"])
def weather_ai():

    if "user" not in session:
        return redirect("/login")

    weather_data = None
    recommendations = []
    message = None

    city = "Mumbai"

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if city == "":
            city = "Mumbai"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        with requests.Session() as s:

            response = s.get(
                BASE_URL,
                params=params,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

        weather_data = {

            "city": data["name"],
            "temp": round(data["main"]["temp"], 1),
            "feels_like": round(data["main"]["feels_like"], 1),
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind": data["wind"]["speed"],
            "condition": data["weather"][0]["main"],
            "description": data["weather"][0]["description"].title()

        }

        recommendations = get_recommendations(weather_data)

    except requests.exceptions.HTTPError:

        message = "❌ City not found. Please enter a valid city."

    except requests.exceptions.Timeout:

        message = "⏳ Weather service timed out."

    except requests.exceptions.ConnectionError:

        message = "🌐 Internet connection error."

    except Exception as e:

        print(e)
        message = "⚠️ Unexpected error occurred."

    return render_template(
        "weather_ai.html",
        weather=weather_data,
        recommendations=recommendations,
        message=message
    )