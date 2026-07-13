import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import pycountry
from countryinfo import CountryInfo
from datetime import datetime
from autocomplete import get_locations, search_locations

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")
GEO_CODER_URL = "http://api.openweathermap.org/geo/1.0/direct"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast?daily=sunrise,sunset&hourly=temperature_2m,relative_humidity_2m&timezone=auto&forecast_days=7"

def get_humidity_avg(weather_data):
    '''a function that calculates average humidty per day instead of per hour'''
    raw_humidity = weather_data["hourly"]["relative_humidity_2m"]
    daily_humidity = []
    for i in range(0, len(raw_humidity), 24):
        day = raw_humidity[i: i + 24]
        daily_humidity.append(round(sum(day) / 24, 1))
    return daily_humidity

def get_day_night_temp(weather_data):
    '''a function that calculates average temperatures in day and night while following sunset and sunrise'''
    hourly_times = weather_data["hourly"]["time"]
    hourly_temps = weather_data["hourly"]["temperature_2m"]
    daily_sunrise = weather_data["daily"]["sunrise"] 
    daily_sunset = weather_data["daily"]["sunset"]

    day_avg = []
    night_avg = []

    for day_index in range(7):
        sunrise_dt = datetime.fromisoformat(daily_sunrise[day_index])
        sunset_dt = datetime.fromisoformat(daily_sunset[day_index])
        sunrise_hour_index = day_index * 24
        sunset_hour_index = sunrise_hour_index + 24
        
        day_temps_list = []
        night_temps_list = []

        for hour_index in range(sunrise_hour_index, sunset_hour_index):
            current_hour_dt = datetime.fromisoformat(hourly_times[hour_index])
            current_temp = hourly_temps[hour_index]

            if sunrise_dt <= current_hour_dt <= sunset_dt:
                day_temps_list.append(current_temp)
            else:
                night_temps_list.append(current_temp)

        if day_temps_list:
            day_avg.append(round(sum(day_temps_list) / len(day_temps_list), 1))
        else:
            day_avg.append(0.0)
        
        if night_temps_list:
            night_avg.append(round(sum(night_temps_list) / len(night_temps_list), 1))
        else:
            night_avg.append(0.0)
    
    return day_avg, night_avg

@app.route("/")
def index():
    '''a function that renders the home page'''
    return render_template("index.html", title="Home")

@app.route("/api/autocomplete", methods=['GET'])
def autocomplete():
    """a function to handle asynchronous search requests"""
    query = request.args.get('term', '') #jQuery UI autocomplete passes term by default
    suggestions = search_locations(query, limit=15)
    return jsonify(suggestions) #jsonify converts python data structures into json formatted HTTP response object

@app.route("/search", methods=['GET'])
def result():
    '''a function that renders the search result page'''
    user_query = request.args.get('q')
    all_countries = get_locations() #used only for fast in-memory validation block

    if not user_query:
        return "please enter a search term!", 400
    
    if user_query not in all_countries:
        return render_template("index.html", error="Please choose a valid location from the suggestion list!")
        
    if any(char.isdigit() for char in user_query):
        return render_template("index.html", error="Location is either invalid, or there is a typo!")
    
    try:
        country_lookup = CountryInfo(user_query)
        capital_city = country_lookup.capital()
        search_query = f"{capital_city}, {user_query}"
    except Exception:
        search_query = user_query

    geo_coder_query_params = {
        "q": search_query,
        "appid": API_KEY,
    }
    response_geo_coder = requests.get(GEO_CODER_URL, params=geo_coder_query_params)
    geo_data = response_geo_coder.json()

    if geo_data:
        result = geo_data[0]
        longitude = result["lon"]
        latitude = result["lat"]
        display_city = result["name"]
        raw_country = result["country"]
        try:
            full_country_name = pycountry.countries.get(alpha_2=raw_country).name
        except AttributeError:
            full_country_name = raw_country

        response_open_weather = requests.get(FORECAST_URL, params={"latitude": latitude, "longitude" : longitude})

        weather_data = response_open_weather.json()
        humidity_list = get_humidity_avg(weather_data)
        day_temps_list, night_temps_list = get_day_night_temp(weather_data)
        date_list = weather_data["daily"]["time"]

        return render_template(
            "index.html",
            city=display_city,
            country=full_country_name,
            dates=date_list,
            day_temps=day_temps_list,    
            night_temps=night_temps_list, 
            humidity=humidity_list
        )
    else:
        return render_template("index.html", error="Location is either invalid, or there is a typo!")
    
@app.errorhandler(404)
def handle_invalid_urls(e):
    '''a function that handles invalid urls and redirects back to home page'''
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
