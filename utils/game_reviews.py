# Retrieve reviews from each game
import requests

def process_reviews(app_id, app_name):
    appinfo_url = f"http://store.steampowered.com/appreviews/{app_id}"
    app_details = requests.get(appinfo_url).json()

    appid = str(app_id)

    
