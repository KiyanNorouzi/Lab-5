#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####
#

import requests
import json
import tkinter as tk


api_key = "cQQPvtPmI89ygtlJn8mQndgc8IcVrypaaeKaeqST"

window = tk.Tk()
window.title("Steam User Info")

def get_user_data():
    steam_id = steam_id_entry.get()


    if not steam_id.isdigit():
        result_label.config(text="Invalid Steam ID")
        return

    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}"


    response = requests.get(url)
    data = json.loads(response.text)

    try:
        player_data = data["response"]["players"][0]
    except:
        result_label.config(text="User not found")
        return


    result_label.config(text=f"Name: {player_data['personaname']}\n"
                             f"Steam ID: {player_data['steamid']}\n"
                             f"Profile URL: {player_data['profileurl']}\n"
                             f"Game count: {player_data['game_count']}\n"
                             f"Total playtime: {player_data['total_playtime'] / 60:.2f} hours")

steam_id_label = tk.Label(window, text="Steam ID:")
steam_id_label.pack()
steam_id_entry = tk.Entry(window)
steam_id_entry.pack()
get_data_button = tk.Button(window, text="Get User Data", command=get_user_data)
get_data_button.pack()
result_label = tk.Label(window)
result_label.pack()
window.mainloop()