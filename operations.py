import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen, Request
from urllib.parse import quote
from urllib.error import URLError
import json

def check_internet(label):
    try:
        urlopen("https://google.com", timeout=3)
        return True
    except URLError as u:
        label.config(
            text="⚠ internet is not connected ⚠"
        )
        return False

def get_temp_city(entr, labt, event=None):
    city = entr.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city or country! ")
        return

    try:
        encoded_city = quote(city)
        url1 = f"https://geocoding-api.open-meteo.com/v1/search?name={encoded_city}&count=1&language=en"
        req1 = Request(
            url1,
            headers={"User-Agent": "CoordiClimate/2.0"}
        )
        with urlopen(req1, timeout=10) as response:
            data = response.read().decode("utf-8")
            data = json.loads(data)
            if 'results' not in data or len(data['results']) == 0:
                raise ValueError("CityNotFound")
            location = data['results'][0]
            lat = location['latitude']
            long = location['longitude']

        url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m,weather_code&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"        
        req2 = Request(
        url2,
        headers={"User-Agent": "CoordiClimate/2.0"}
        )
        with urlopen(req2, timeout=10) as response2:
            data2 = response2.read().decode("utf-8")
            data2 = json.loads(data2)
            current = data2["current"]

        labt.config(
            text=f"Temperature: {current['temperature_2m']} °C\n"
            f"Wind speed: {current['wind_speed_10m']} km/h\n"
            f"Latitude: {data2['latitude']}\n"
            f"Longitude: {data2['longitude']}"
        )

    except ValueError as e:
        if str(e) == "CityNotFound":
            messagebox.showerror("Error", f"{city} could not be found or not exists!")
        else:
            messagebox.showerror("Error", f"an error occured while sending request to thr server: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"failed to connect to the server: {e}")

def get_lat_long(entlat, entlong, resulabel):
    if not entlat.get().strip() or not entlong.get().strip():
        messagebox.showerror("Error", "Please enter both coordinates!")
        return
    try:
        latit = float(entlat.get().strip())
        longit = float(entlong.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Co-ordinates must be numbers!")
        return
    try:
        if not -90 <= latit <= 90:
            messagebox.showerror("Error", "Invalid latitude!")
            return
        if not -180 <= longit <= 180:
            messagebox.showerror("Error", "Invalid longitude!")
            return
        url1 = f"https://nominatim.openstreetmap.org/reverse?lat={latit}&lon={longit}&format=jsonv2&addressdetails=1&accept-language=en"
        req = Request(
                url1,
                headers={"User-Agent": "CoordiClimate/2.0"}
            )
        with urlopen(req, timeout=10) as response:
            data3 = response.read().decode("utf-8")
            data3 = json.loads(data3)
            if 'address' not in data3 or len(data3['address']) == 0:
                    raise ValueError("CityNotFound")
            country = data3["address"]["country"]
            country_code = data3["address"]["country_code"]

        resulabel.config(
            text=f"country name: {country}\ncountry code: {country_code}"
        )

    except ValueError as f:
        if str(f) == "CityNotFound":
            messagebox.showerror("Error", "city could not be found or entered co-ordinates are not correct!")
        else:
            messagebox.showerror("Error", f"an error occured while sending request to thr server: {f}")
    except Exception as f:
        messagebox.showerror("Error", f"failed to connect to the server: {f}")