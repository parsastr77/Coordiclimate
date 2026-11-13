import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen, Request
from urllib.parse import quote
from urllib.error import URLError
import json

def country_finder(app, MAIN_FONT):
    app.withdraw()
    page_get_city = tk.Toplevel(app)

    def close_window():
        page_get_city.destroy()
        app.deiconify()

    page_get_city.protocol("WM_DELETE_WINDOW", close_window)

    page_get_city.geometry("500x600")
    page_get_city.resizable(False,False)
    page_get_city.config(bg="#1B365D")
    page_get_city.title("Country Finder")
    page_get_city.iconbitmap("Main_Icon.ico")

    labtitude = tk.Label(
    master=page_get_city,
    text="latitude:",
    font=(MAIN_FONT, 16),
    bg="#1B365D",
    fg="#60C1E5"
    )
    labtitude.place(
    relx=0.13,
    y=220,
    anchor="n"
    )

    longlab = tk.Label(
    master=page_get_city,
    text="longitude:",
    font=(MAIN_FONT, 16),
    bg="#1B365D",
    fg="#60C1E5"
    )
    longlab.place(
    relx=0.13,
    y=270,
    anchor="n"
    )

    lab_result_lat_long = tk.Label(
    master=page_get_city,
    text="",
    font=(MAIN_FONT, 24),
    bg="#1B365D",
    fg="white",
    width=35,
    wraplength=440,
    justify="center",
    anchor="center"
    )
    lab_result_lat_long.place(
    x=20,
    y=90,
    width=460
    )
    
    lab_weatherapist2 = tk.Label(
    master=page_get_city,
    text="city finder",
    font=(MAIN_FONT, 35),
    bg="#1B365D",
    fg="#60C1E5"
    )
    lab_weatherapist2.place(
    relx=0.5,
    y=9,
    anchor="n"
    )

    ent_get_lat = tk.Entry(
    master=page_get_city,
    bg="#60C1E5",
    fg="#005A9C",
    font=(MAIN_FONT, 17),
    width=30,
    border=4
    )
    ent_get_lat.place(
    relx=0.6,
    y=240,
    anchor="center"
    )

    ent_get_long = tk.Entry(
        master=page_get_city,
        bg="#60C1E5",
        fg="#005A9C",
        font=(MAIN_FONT, 17),
        width=30,
        border=4
    )
    ent_get_long.place(
    relx=0.6,
    y=290,
    anchor="center"
    )

    btn_get_lat_long = tk.Button(
    master=page_get_city,
    text="Enter",
    bg="#60C1E5",
    fg="#005A9C",
    font=(MAIN_FONT, 16),
    width=20,
    height=1,
    command=lambda: get_lat_long(
        ent_get_lat,
        ent_get_long,
        lab_result_lat_long
        )
    )
    btn_get_lat_long.place(
    relx=0.5,
    y=380,
    anchor="center"
    )


def cities_status(app, MAIN_FONT):
    app.withdraw()
    page_temp = tk.Toplevel(app)

    def close_window():
        page_temp.destroy()
        app.deiconify()

    page_temp.protocol("WM_DELETE_WINDOW", close_window)

    page_temp.geometry("500x600")
    page_temp.resizable(False,False)
    page_temp.config(bg="#1B365D")
    page_temp.title("cities")
    page_temp.iconbitmap("Main_Icon.ico")

    ent = tk.Entry(
    master=page_temp,
    bg="#60C1E5",
    fg="#005A9C",
    font=(MAIN_FONT, 21),
    width=30,
    border=4
    )
    ent.place(
    relx=0.5,
    y=350,
    anchor="n"
    )

    btn = tk.Button(
    master=page_temp,
    text="Enter city",
    bg="#60C1E5",
    fg="#005A9C",
    font=(MAIN_FONT, 16),
    width=20,
    height=1,
    command=lambda: get_temp_city(
        ent,
        lab,
        )
    )
    btn.place(
    relx=0.5,
    y=430,
    anchor="n"
    )

    lab = tk.Label(
    master=page_temp,
    text="",
    font=(MAIN_FONT, 24),
    bg="#1B365D",
    fg="white",
    justify="center",
    anchor="center"
    )
    lab.place(
    relx=0.5,
    y=200,
    anchor="center"
    )

    lab_weatherapist3 = tk.Label(
    master=page_temp,
    text="cities status",
    font=(MAIN_FONT, 35),
    bg="#1B365D",
    fg="#60C1E5"
    )
    lab_weatherapist3.place(
    relx=0.5,
    y=9,
    anchor="n"
    )

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