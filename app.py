import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
import geonamescache
import requests
import pycountry
from countryinfo import CountryInfo
from datetime import datetime
from autocomplete import get_locations


app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")
GEO_CODER_URL = f"http://api.openweathermap.org/geo/1.0/direct"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast?daily=sunrise,sunset&hourly=temperature_2m,relative_humidity_2m&timezone=auto&forecast_days=7"

def get_humidity_avg(weather_data):
    '''a function that gets a list of humidity per hour values and returns an average for each day'''
    raw_humidity = weather_data["hourly"]["relative_humidity_2m"]
    daily_humidity = []
    for i in range(0, len(raw_humidity), 24):
        day = raw_humidity[i: i + 24]
        daily_humidity.append(round(sum(day) / 24, 1))
    
    return daily_humidity


def get_day_night_temp(weather_data):
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
    return render_template("index.html", title="Home", countries_list=get_locations())

#translate city name to longitute and latitude coordinates
@app.route("/search", methods=['GET'])
def result():
    user_query = request.args.get('q')
    all_countries = get_locations()

    if not user_query:
        return "please enter a search term!", 400
    
    if user_query not in all_countries:
        return render_template("index.html", error="Please choose a valid location from the suggestion list!", countries_list=all_countries)
        
    if any(char.isdigit() for char in user_query):
        return render_template("index.html", error="Location is either invalid, or there is a typo!", countries_list=all_countries)
    
    city_only = user_query.split(",")[0].strip()        #incase the user inputs a city only
    try:
        country_lookup = CountryInfo(user_query)
        capital_city = country_lookup.capital()
        search_query = f"{capital_city}, {user_query}"
    except Exception:
        search_query = user_query

    geo_coder_query_params = {
        "q": search_query,
        "appid": API_KEY,
        #"limit": 1
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

        forecast_query_params = {
            "lon" : longitude,
            "lat" : latitude,
            "appid": API_KEY
        }
        
        response_open_weather = requests.get(FORECAST_URL, params={"latitude": forecast_query_params["lat"], "longitude" : forecast_query_params["lon"]})

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
            humidity=humidity_list,
            countries_list=all_countries
        )


    else:
        return render_template("index.html", error="Location is either invalid, or there is a typo!", countries_list=get_locations())
    
@app.errorhandler(404)
def handle_invalid_urls(e):
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)