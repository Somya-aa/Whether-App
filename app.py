from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"

@app.route("/", methods=["GET","POST"])
def home():
    city = "" 
    temp = ""
    feels_like = ""
    humidity = ""
    wind_speed = ""
    country = ""

    if request.method=="POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        wind_speed = data["wind"]["speed"]
        country = data["sys"]["country"]


    return render_template(
        "index.html",
        city=city,
        temp=temp,
        feels_like=feels_like,
        humidity=humidity,
        wind_speed=wind_speed,
        country=country
    )
    
app.run(debug=True)    