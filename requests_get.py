#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####

import requests


response = requests.get("https://steamcommunity.com")

print(response.content)

with open("response.txt", "w") as file:
    file.write(response.content.decode("utf-8"))