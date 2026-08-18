import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather():
    country = country_entry.get().strip()
    city = city_entry.get().strip()

    if not country or not city:
        messagebox.showwarning(
            "Warning",
            "Please enter both country and city."
        )
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city},{country}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if str(data.get("cod")) != "200":
            result_label.config(
                text=f"Error:\n{data.get('message', 'Location not found')}"
            )
            return

        city_name = data["name"]
        country_code = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        result_label.config(
            text=
            f"Country: {country_code}\n"
            f"City: {city_name}\n"
            f"Temperature: {temp}°C\n"
            f"Feels Like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Condition: {weather.title()}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main Window
root = tk.Tk()
root.title("Weather App")
root.geometry("500x450")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 22, "bold")
)
title.pack(pady=15)

# Country
country_label = tk.Label(
    root,
    text="Country",
    font=("Arial", 12)
)
country_label.pack()

country_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)
country_entry.pack(pady=5)

# City
city_label = tk.Label(
    root,
    text="City",
    font=("Arial", 12)
)
city_label.pack()

city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)
city_entry.pack(pady=5)

# Button
search_btn = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    command=get_weather
)
search_btn.pack(pady=15)

# Result Area
result_label = tk.Label(
    root,
    text="Enter country and city",
    font=("Arial", 12),
    justify="left"
)
result_label.pack(pady=20)

root.mainloop()