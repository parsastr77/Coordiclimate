# weatherapist app

import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen, Request
from urllib.parse import quote
import json

app = tk.Tk()

def open_temp():
    app.withdraw()
    page_temp = tk.Toplevel()

    def close_window():
        page_temp.destroy()
        app.deiconify()

    page_temp.protocol("WM_DELETE_WINDOW", close_window)

    page_temp.minsize(500,600)
    page_temp.resizable(False,False)
    page_temp.config(bg="black")
    page_temp.title("get temperature")

    ent = tk.Entry(
    master=page_temp,
    bg="#9929EA",
    fg="#FAEB92",
    font=["Bebas Neue", 21],
    width=30,
    border=4
    )
    ent.place(x=80,y=250)

    btn = tk.Button(
    master=page_temp,
    text="Enter city",
    bg="#CC66DA",
    fg="#FAEB92",
    font=["Bebas Neue", 16],
    width=20,
    height=1,
    command=lambda: get_temp_city(
        ent,
        lab,
        )
    )
    btn.place(x=160,y=330)

    lab = tk.Label(
    master=page_temp,
    text="",
    font=["Bebas Neue", 24],
    bg="black",
    fg="white"
    )
    lab.place(x=140,y=90)

    lab_weatherapist3 = tk.Label(
    master=page_temp,
    text="get temperature",
    font=["Bebas Neue", 35],
    bg="black",
    fg="#FAEB92"
    )
    lab_weatherapist3.place(x=110,y=9)

def open_getlatlong():
    app.withdraw()
    page_get_city = tk.Toplevel(app)

    def close_window():
        page_get_city.destroy()
        app.deiconify()

    page_get_city.protocol("WM_DELETE_WINDOW", close_window)

    page_get_city.minsize(500,600)
    page_get_city.resizable(False,False)
    page_get_city.config(bg="black")
    page_get_city.title("get lat/long")

    labtitude = tk.Label(
    master=page_get_city,
    text="latitude:",
    font=["Bebas Neue", 16],
    bg="black",
    fg="white"
    )
    labtitude.place(x=10,y=240)

    longlab = tk.Label(
    master=page_get_city,
    text="longtitude:",
    font=["Bebas Neue", 16],
    bg="black",
    fg="white"
    )
    longlab.place(x=10,y=290)

    lab_result_lat_long = tk.Label(
    master=page_get_city,
    text="",
    font=["Bebas Neue", 24],
    bg="black",
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
    font=["Bebas Neue", 35],
    bg="black",
    fg="#FAEB92"
    )
    lab_weatherapist2.place(x=150,y=9)

    ent_get_lat = tk.Entry(
    master=page_get_city,
    bg="#9929EA",
    fg="#FAEB92",
    font=["Bebas Neue", 17],
    width=30,
    border=4
    )
    ent_get_lat.place(x=110,y=240)

    ent_get_long = tk.Entry(
        master=page_get_city,
        bg="#9929EA",
        fg="#FAEB92",
        font=["Bebas Neue", 17],
        width=30,
        border=4
    )
    ent_get_long.place(x=110,y=290)

    btn_get_lat_long = tk.Button(
    master=page_get_city,
    text="Enter lat/long",
    bg="#CC66DA",
    fg="#FAEB92",
    font=["Bebas Neue", 16],
    width=20,
    height=1,
    command=lambda: get_lat_long(
        ent_get_lat,
        ent_get_long,
        lab_result_lat_long
        )
    )
    btn_get_lat_long.place(x=160,y=380)

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
            headers={"User-Agent": "Weatherapist/1.0"}
        )
        with urlopen(req1, timeout=10) as response:
            data = response.read().decode("utf-8")
            data = json.loads(data)
            if 'results' not in data or len(data['results']) == 0:
                raise ValueError("CityNotFound")
            location = data['results'][0]
            lat = location['latitude']
            long = location['longitude']

        url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        req2 = Request(
            url2,
            headers={"User-Agent": "Weatherapist/1.0"}
        )
        with urlopen(req2, timeout=10) as response2:
            data2 = response2.read().decode("utf-8")
            data2 = json.loads(data2)
            current = data2["current"]

        labt.config(
            text=f"temprature: {current['temperature_2m']} °C\nwind speed: {current['wind_speed_10m']}"
        )

    except ValueError as e:
        if str(e) == "CityNotFound":
            messagebox.showerror("Error", f"{city} could not be found!")
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
        if not -90 <= latit <= 90:
            raise ValueError("Invalid latitude!")
        if not -180 <= longit <= 180:
            raise ValueError("Invalid longitude!")
        url1 = f"https://nominatim.openstreetmap.org/reverse?lat={latit}&lon={longit}&format=jsonv2&addressdetails=1&accept-language=en"
        req = Request(
                url1,
                headers={"User-Agent": "Weatherapist/1.0"}
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
            messagebox.showerror("Error", "city could not be found!")
        else:
            messagebox.showerror("Error", f"an error occured while sending request to thr server: {f}")
    except Exception as f:
        messagebox.showerror("Error", f"failed to connect to the server: {f}")

app.minsize(500,600)
app.resizable(False,False)
app.config(bg="black")
app.title("Weatherapist")

cityfinderbtn = tk.Button(
    master=app,
    text="city finder",
    bg="#CC66DA",
    fg="#FAEB92",
    font=["Bebas Neue", 25],
    width=20,
    height=1,
    command=open_getlatlong
    )
cityfinderbtn.place(x=115,y=200)

gettempbtn = tk.Button(
    master=app,
    text="get temperature",
    bg="#CC66DA",
    fg="#FAEB92",
    font=["Bebas Neue", 25],
    width=20,
    height=1,
    command=open_temp
    )
gettempbtn.place(x=115,y=300)

lab_weatherapist1 = tk.Label(
    master=app,
    text="weatherapist",
    font=["Bebas Neue", 50],
    bg="black",
    fg="#FAEB92"
)
lab_weatherapist1.place(x=95,y=9)

app.mainloop()