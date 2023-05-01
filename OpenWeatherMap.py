#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####

import requests
import json
import tkinter as tk

def get_weather():
    city_name = entry_city.get()
    api_key = "7cdcfaa69a322e2c77fdf3043de45290&"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    temp_k = data['main']['temp']
    temp_c = round(temp_k - 273.15, 1)

    label_temp.config(text=f"Temperature: {temp_c} °C")
    label_humidity.config(text=f"Humidity: {data['main']['humidity']}%")
    label_pressure.config(text=f"Pressure: {data['main']['pressure']} hPa")

    with open('weather_data.json', 'w') as f:
        json.dump(data, f)

root = tk.Tk()
root.title("Weather App")

frame_city = tk.Frame(root)
frame_city.pack(padx=10, pady=10)

label_city = tk.Label(frame_city, text="Enter City Name:")
label_city.pack(side=tk.LEFT)

entry_city = tk.Entry(frame_city)
entry_city.pack(side=tk.LEFT, padx=10)

button_weather = tk.Button(root, text="Get Weather", command=get_weather)
button_weather.pack(pady=10)

frame_weather = tk.Frame(root)
frame_weather.pack()

label_temp = tk.Label(frame_weather, text="Temperature: ")
label_temp.pack(side=tk.LEFT)

label_humidity = tk.Label(frame_weather, text="Humidity: ")
label_humidity.pack(side=tk.LEFT, padx=10)

label_pressure = tk.Label(frame_weather, text="Pressure: ")
label_pressure.pack(side=tk.LEFT)

root.mainloop()
