# API call to retrieve all games and process its details (app_id, name, date, price, reviews)
import requests
import time

from utils.game_details import process_details

# data should look like:
# {
#     "applist": {
#         "apps": [
#             { "appid": 5, "name": "Dedicated Server" },
#             { "appid": 7, "name": "Steam Client" },
#             ...
#         ]
#     }
# }

def get_catalog():
    catalog_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(catalog_url)
    catalog_data = response.json()

    for app in catalog_data["applist"]["apps"]:
        app_id = app["appid"]
        app_name = app["name"]

        # Retrieve and store app_id, name, date, price
        process_details(app_id, app_name)
        
        time.sleep(0.1)


