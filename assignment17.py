#Assignment 17 

#In this we have to take input from user and Print details of that city GUI based.

import tkinter as tk
from tkinter import messagebox
import requests



def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={paste_your_api_key_here}&units=metric" #for my safety purpose i remove my api key.So use your api key.

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()

        result = (
            f"City: {city_name}, {country}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Weather: {weather}"
        )

        result_label.config(text=result)
    else:
        messagebox.showerror("Error", data.get("message", "City not found!"))

    




# GUI Window

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")


title = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"))
title.pack(pady=10)


city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=10)
city_entry.focus()


search_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
search_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()