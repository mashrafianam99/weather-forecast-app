from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "5323a773103fd44598326c3a932942ef"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        print(response.url)  # DEBUG
        print(response.text)  # DEBUG
        data = response.json()

        if data.get("cod") == 200:
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "condition": data["weather"][0]["main"],
                "icon": data["weather"][0]["icon"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
        else:
            error = "City not found!"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run()
