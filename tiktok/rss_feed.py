from feedgen.feed import FeedGenerator

def create_rss_feed(videos):
    # This initializes a new RSS feed generator
    fg = FeedGenerator() # fg is an instance of FeedGenerator(), which allows us to set metadata and add feed entries.
    fg.id('https://yourwebsite.com/tiktok-rss') # This sets a unique identifier for the RSS feed. It's usually the URL where the RSS feed is hosted.
    fg.title('TikTok RSS Feed') # This defines the title of the RSS feed. When a user subscribes, this is the name that appears in their feed reader.
    fg.link(href='https://tiktok.com', rel='alternate') # Adds a link to the original website
    fg.description('Latest TikTok videos') # Provides a short description of the RSS feed.

    # list of dictionaries, where each dictionary contains details of a TikTok video
    for video in videos:
        fe = fg.add_entry()
        fe.id(video["video_url"])
        fe.title(video["title"])
        fe.link(href=video["video_url"])
        fe.description(f'<img src="{video["thumbnail"]}" /><br>{video["title"]}')

    fg.rss_file('tiktok_feed.xml') # It contains all video entries formatted properly.

# example
# videos = [
#     {"title": "Funny Dance", "video_url": "https://tiktok.com/somevideo", "thumbnail": "https://example.com/image.jpg"},
#     {"title": "Cute Cat", "video_url": "https://tiktok.com/anothervideo", "thumbnail": "https://example.com/image2.jpg"}
# ]
# create_rss_feed(videos)



