import config

def create_rss_youtube_url (channel_id: str):
    return f'https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}&key={config.API_KEY_YOUTUBE}'