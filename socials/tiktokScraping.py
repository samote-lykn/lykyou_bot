#TikTok doesn’t allow public scraping easily, so use a service like RapidAPI’s TikTok API to fetch user videos:
#For better tracking, use the TikTok API via RapidAPI.
import requests


def get_tiktok_posts(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("TikTok profile fetched successfully!")
    else:
        print("Failed to fetch TikTok profile.")


get_tiktok_posts("tiktok_username")
