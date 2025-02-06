import requests

def get_videos_from_tiktok_username(username:str, tiktok_api:str, tiktok_api_key:str):
    api_url = f"https://{tiktok_api}/user/{username}/videos"

    response = requests.get(api_url, headers={"Authorization": f"Bearer {tiktok_api_key}"})
    data = response.json()

    for video in data["videos"]:
        print(video["title"], video["video_url"])
