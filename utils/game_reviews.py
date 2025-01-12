# Retrieve reviews from each game
import requests

def process_reviews(app_id, app_name):
    appreviews_url = f"https://store.steampowered.com/appreviews/{app_id}?json=1"

    reviews_response = requests.get(appreviews_url).json()

    if reviews_response["success"] == 1:
        
        total_reviews = reviews_response["query_summary"]["total_reviews"]
        total_positive = reviews_response["query_summary"]["total_positive"]
        total_negative = reviews_response["query_summary"]["total_negative"]
        review_score = reviews_response["query_summary"]["review_score"]
        review_score_desc = reviews_response["query_summary"]["review_score_desc"]
    else:
        return

    print(f'Game: {app_name}, Total Reviews: {total_reviews}, Positive: {total_positive}, Negative: {total_negative}, Ratings: {review_score_desc}')
    



