import requests
import time

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
        
        appinfo_url = f"http://store.steampowered.com/api/appdetails?appids={app_id}"

        app_details = requests.get(appinfo_url).json()

        appid = str(app_id)

        if app_details[appid]['success'] != False:
            game_info = app_details[appid]["data"]

            game_price = 0

            game_date = ""

            if not game_info["is_free"] and not game_info["release_date"]["coming_soon"]:
                game_date = game_info["release_date"]["date"]

                # Safely check for price_overview key
                if "price_overview" in game_info:
                    # Convert cents to dollars
                    game_price = game_info["price_overview"]["final"] / 100.0
                else:
                    continue

                print(f"App ID: {appid}, Name: {app_name}, Release Date: {
                      game_date}, Price: {game_price}")
                
    
        
        time.sleep(0.1)

            # print(game_price)
