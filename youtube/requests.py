import requests
import config
from utils import create_rss_youtube_url

# search for channel_id by username
def get_channel_id_by_username(username: str):
    response = requests.get(
        f'https://www.googleapis.com/youtube/v3/channels?part=id&forUsername={username}&key={config.API_KEY_YOUTUBE}')
    print(response.json())

# search for channel by channel_id
def get_channel_by_channel_id(channel_id: str):
    response = requests.get(
        f'https://www.googleapis.com/youtube/v3/channels?part=id&id={channel_id}&key={config.API_KEY_YOUTUBE}')
    print(response.json())

# search for channel snippet by channel_id
def get_channel_snippet_by_channel_id(channel_id: str):
    response = requests.get(
        f'https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={config.API_KEY_YOUTUBE}')
    print(response.json())

# search for channel feed videos by channel_id
def get_channel_feed_by_channel_id(channel_id: str):
    response = requests.get(create_rss_youtube_url(channel_id))
    print(response.json())