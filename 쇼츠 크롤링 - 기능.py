import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def crawl_current_shorts_hashtags(num_shorts_to_crawl):
    url = 'https://www.youtube.com/feed/trending'

    driver = webdriver.Chrome()
    driver.get(url)

    driver.implicitly_wait(5)
    link = driver.find_element(By.CLASS_NAME, 'style-scope ytd-reel-item-renderer')
    link.click()

    hashtags = []
    
    def save_hashtags_to_csv(csv_file, hashtags_list):
        with open(csv_file, 'w', newline='', encoding='ANSI') as file:
            writer = csv.writer(file)
            for hashtag in hashtags_list:
                writer.writerow([hashtag])

    for _ in range(num_shorts_to_crawl):
        reel_html = driver.page_source

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(reel_html, 'html.parser')

        hashtag_elements = driver.find_elements(By.XPATH, '//*[@id="overlay"]/ytd-reel-player-header-renderer/h2/yt-formatted-string/a')

        for element in hashtag_elements:
            hashtag = element.text.strip()[1:] 
            hashtags.append(hashtag)
  
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.ARROW_DOWN)
        time.sleep(3) 

    csv_file = 'hashtags.csv'
    save_hashtags_to_csv(csv_file, hashtags)

    driver.quit()

print(crawl_current_shorts_hashtags(num_shorts_to_crawl=15))
