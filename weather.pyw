import requests
from flask import Flask, jsonify

app = Flask(__name__)

weather_icons = {
    "clear sky": "",  
    "few clouds": "",  
    "scattered clouds": "", 
    "broken clouds": "",  
    "shower rain": "",  
    "rain": "",  
    "thunderstorm": "", 
    "snow": "",  
    "mist": "󰖑",  
    "overcast clouds": "",  
    "light rain": "",
    "moderate rain": "",
    "heavy intensity rain" : ""
}

@app.route('/weather')
def get_weather():
    api_key = "5e9b7582c77c6d73d1cbd353606dd94b"
    city = "Morshi" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    weather_description = data['weather'][0]['description']
    temp = int(data['main']['temp'])  

    weather_icon = weather_icons.get(weather_description, "🌈")

    weather_info = f"Current weather:{weather_description} {weather_icon}  {temp}°Cend1"

    return weather_info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089)