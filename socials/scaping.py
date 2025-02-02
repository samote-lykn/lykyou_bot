#Instagram and TikTok do not provide RSS feeds, so we use APIs or Web Scraping.
#For real-time tracking, use the Instagram Graph API (requires authentication).

import requests
from bs4 import BeautifulSoup

def get_instagram_posts(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    scripts = soup.find_all("script", type="application/ld+json")
    for script in scripts:
        if "GraphImage" in script.string:
            print(script.string)

get_instagram_posts("instagram_username")
