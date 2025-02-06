from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_videos_from_tiktok_username(username:str):
    driver = webdriver.Chrome()
    driver.get(f"https://www.tiktok.com/@{username}")

    time.sleep(5)

    videos = driver.find_elements(By.CSS_SELECTOR, "div.tiktok-feed-item")
    for video in videos:
        url = video.find_element(By.TAG_NAME, "a").get_attribute("href")
        print(url)

    driver.quit()
