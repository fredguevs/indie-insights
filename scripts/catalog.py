import requests


def get_catalog():
    catalog_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(catalog_url)

    print(response.text)
