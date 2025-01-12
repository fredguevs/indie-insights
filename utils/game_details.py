# Helper func for processing each app
import requests

def process_details(app_id, app_name):
    appinfo_url = f"http://store.steampowered.com/api/appdetails?appids={app_id}"
    app_details = requests.get(appinfo_url).json()

    appid = str(app_id)

    if app_details[appid]['success'] != False:
        game_info = app_details[appid]["data"]
        game_price = 0
        game_date = ""

        if not game_info["is_free"] and not game_info["release_date"]["coming_soon"]:
            game_date = game_info["release_date"]["date"]

        if "price_overview" in game_info:
            game_price = game_info["price_overview"]["final"]
        else: 
            return

        print(f"App ID: {appid}, Name: {app_name}, Release Date: {
            game_date}, Price: {game_price}")
