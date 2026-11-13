#CoordiClimate v2.5.7

"""
🌍 CoordiClimate
This app is a handy tool to check the current temperature of cities and countries 
worldwide, as well as locate them effortlessly using latitude and longitude.🌍
If you like this project or find it useful, we would be thrilled if you could follow our GitHub channel!⭐

Tip✨ ==> We recommend you to have the "fonts" folder next to the main project because the application
needs the font "Bebas Neue" to run CORRECTLY! but if you have already installed the font, you dont need to
do that🎉

What's New in v2.5.7:
- Made our application modular✅
- Improved error handling and input validation✅
- Enhanced API response handling✅
- Minor code improvements and bug fixes✅

Current Version: v2.5.7

GitHub Channel: https://github.com/parsastr77

THANKS FOR USING! 🚀
"""

from tkinter import messagebox
from urllib.request import urlopen, Request
from urllib.parse import quote
from urllib.error import URLError
from tkinter import ttk
from operations import *
from models import *
import tkinter as tk
import json
import ctypes
import os

font_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "fonts",
    "BebasNeue-Regular.ttf"
)

FR_PRIVATE = 0x10
gdi32 = ctypes.windll.gdi32

font_loaded = False

if os.path.isfile(font_path):
    result = gdi32.AddFontResourceExW(
        font_path,
        FR_PRIVATE,
        0
    )

    font_loaded = result > 0

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

app = tk.Tk()

def close_app():
    if font_loaded:
        gdi32.RemoveFontResourceExW(
            font_path,
            FR_PRIVATE,
            0
        )

    app.destroy()

app.protocol("WM_DELETE_WINDOW", close_app)

MAIN_FONT = "Bebas Neue"

def country_finder():
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

# MAIN APP SETTINGS
app.geometry("600x700")
app.resizable(False,False)
app.config(bg="#1B365D")
app.title("CoordiClimate")

GUI(app, MAIN_FONT, country_finder, cities_status)


app.mainloop()