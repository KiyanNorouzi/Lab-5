#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####

import requests
import tkinter as tk
from PIL import Image, ImageTk
import io

api_key = "cQQPvtPmI89ygtlJn8mQndgc8IcVrypaaeKaeqST"
account_id = "0a264738-dc05-429e-b2fd-2f1a45c33ce6"


url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&account_id={account_id}"
response = requests.get(url)
response_data = response.json()

if 'url' not in response_data:
    print("Error: Could not retrieve image URL from API")
else:
    image_url = response_data['url']
    image_title = response_data['title']

    window = tk.Tk()
    window.title("NASA APOD")
    response = requests.get(image_url)
    image_data = response.content
    image = Image.open(io.BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(window, image=photo)
    label.pack()
    title_label = tk.Label(window, text=image_title)
    title_label.pack()
    window.mainloop()
