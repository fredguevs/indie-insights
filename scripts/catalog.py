import requests

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

        appid = f"{app_id}"

        if app_details[appid]['success'] != False:
            game_info = app_details[appid]["data"]

            game_price = 0

            game_date = ""

            if game_info["is_free"] == False and game_info["release_date"]["coming_soon"] == False:
                game_date = game_info["release_date"]["date"]
                game_price = game_info["price_overview"]["final"]

            print(game_price)
