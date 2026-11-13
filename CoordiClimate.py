#CoordiClimate v2.7.1

"""
🌍 CoordiClimate
This app is a handy tool to check the current temperature of cities and countries 
worldwide, as well as locate them effortlessly using latitude and longitude.🌍
If you like this project or find it useful, we would be thrilled if you could follow our GitHub channel!⭐

Tip✨ ==> We recommend you to have the "fonts" folder next to the main project because the application
needs the font "Bebas Neue" to run CORRECTLY! but if you have already installed the font, you dont need to
do that🎉

What's New in v2.7.1:
- Added an icon image✅
- Organized code structure✅
- Improved error handling and input validation✅
- Enhanced API response handling✅
- Minor code improvements and bug fixes✅

Current Version: v2.7.1

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

# MAIN APP SETTINGS
app.geometry("600x700")
app.resizable(False,False)
app.config(bg="#1B365D")
app.title("CoordiClimate")
app.iconbitmap("Main_Icon.ico")

GUI(app, MAIN_FONT, country_finder, cities_status)

app.mainloop()