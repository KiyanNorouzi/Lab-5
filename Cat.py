#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####

import requests
from PIL import ImageTk, Image
import tkinter as tk


class RandomCatImageGenerator:
    def __init__(self, master):
        self.master = master
        self.image_url = ""
        self.load_image()
        self.setup_ui()

    def load_image(self):
        response = requests.get("https://aws.random.cat/meow")
        data = response.json()
        self.image_url = data['file']

    def setup_ui(self):
        self.image = Image.open(requests.get(self.image_url, stream=True).raw)
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(self.master, width=self.image.width, height=self.image.height)
        self.canvas.pack()

        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

        self.button = tk.Button(self.master, text="Next image", command=self.next_image)
        self.button.pack(pady=10)

    def next_image(self):
        self.load_image()
        self.image = Image.open(requests.get(self.image_url, stream=True).raw)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomCatImageGenerator(root)
    root.mainloop()
