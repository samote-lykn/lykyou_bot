from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
import undetected_chromedriver as uc  # SUPER stealth mode!

# Random User-Agent List (spoof different devices)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
]

# Proxy support (optional)
PROXY = "your_proxy:port"

def get_videos_from_tiktok_username(username: str):
    """Scrapes video URLs from a TikTok username with max stealth."""

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Hide bot signature
    chrome_options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")  # Random user agent
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")  # Make it look like a real user
    chrome_options.add_argument("--disable-popup-blocking")

    # Use proxy (optional)
    if PROXY:
        chrome_options.add_argument(f'--proxy-server={PROXY}')

    # Use undetected ChromeDriver (hides bot traces)
    driver = uc.Chrome(options=chrome_options)

    try:
        # Load TikTok Profile Page
        driver.get(f"https://www.tiktok.com/@{username}")
        time.sleep(random.uniform(3, 5))  # Randomized wait

        # Simulate human-like scrolling
        for _ in range(random.randint(3, 6)):  # Scroll multiple times
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 4))  # Random wait

        # Move mouse randomly to avoid detection
        action = ActionChains(driver)
        for _ in range(5):
            action.move_by_offset(random.randint(-200, 200), random.randint(-200, 200)).perform()
            time.sleep(random.uniform(0.5, 1.5))

        # Press a random key (to mimic user activity)
        action.send_keys(Keys.TAB).perform()
        time.sleep(random.uniform(1, 2))

        # Wait until videos load
        videos = driver.find_elements(By.CSS_SELECTOR, "div.tiktok-feed-item")

        video_urls = []
        for video in videos:
            try:
                url = video.find_element(By.TAG_NAME, "a").get_attribute("href")
                video_urls.append(url)
            except Exception as e:
                print(f"Error extracting video URL: {e}")

        print("\n📹 Scraped Video Links:")
        for url in video_urls:
            print(url)

        return video_urls

    finally:
        driver.quit()  # Close browser session