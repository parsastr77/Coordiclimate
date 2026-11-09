import tkinter as tk
from tkinter import *
from operations import *

def GUI(app, MAIN_FONT, country_finder, cities_status):
    cityfinderbtn = tk.Button(
        master=app,
        text="country finder",
        bg="#60C1E5",
        fg="#005A9C",
        font=(MAIN_FONT, 25),
        width=20,
        height=1,
        command=country_finder
        )
    cityfinderbtn.place(
        relx=0.5,
        y=300,
        anchor="center"
    )

    gettempbtn = tk.Button(
        master=app,
        text="city status",
        bg="#60C1E5",
        fg="#005A9C",
        font=(MAIN_FONT, 25),
        width=20,
        height=1,
        command=cities_status
        )
    gettempbtn.place(
        relx=0.5,
        y=400,
        anchor="center"
    )

    lab_weatherapist1 = tk.Label(
        master=app,
        text="coordiclimate",
        font=(MAIN_FONT, 50),
        bg="#1B365D",
        fg="#60C1E5"
    )
    lab_weatherapist1.place(
        relx=0.5,
        y=9,
        anchor="n"
    )

    lab_internet = tk.Label(
        master=app,
        text="",
        font=(MAIN_FONT, 25),
        bg="#1B365D",
        fg="yellow"
    )

    lab_internet.place(
        relx=0.5,
        y=550,
        anchor="center"
    )

    check_internet(lab_internet)