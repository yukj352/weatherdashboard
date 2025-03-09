from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "46f1c46ccc8bac8036819f33e0bb6ff3"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city").strip()
        if city:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "name": data["name"],
                    "temp": data["main"]["temp"],
                    "description": data["weather"][0]["description"].capitalize(),
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"]
                }
            else:
                weather_data = {"error": "City not found. Please try again."}
    
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
