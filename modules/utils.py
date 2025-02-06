
def get_preview_image(url):
    """Manually define preview images based on domains."""
    if "tiktok.com" in url:
        return "https://example.com/tiktok-preview.jpg"
    elif "instagram.com" in url:
        return "https://example.com/instagram-preview.jpg"
    elif "twitter.com" in url:
        return "https://example.com/twitter-preview.jpg"
    return None