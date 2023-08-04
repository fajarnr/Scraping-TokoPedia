from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('/opt/homebrew/Caskroom/chromedriver/113.0.5672.63/chromedriver')
# driver = webdriver.Chrome(service=servis, options=opsi)
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver = webdriver.Chrome()

# driver =  webdriver.Chrome("/opt/homebrew/Caskroom/chromedriver/113.0.5672.63/")

shopee_link = "hhttps://shopee.co.id/search?keyword=samsung"
driver.set_window_size(1300, 800)
driver.get(shopee_link)
# time.sleep(5)

driver.save_screenshot("home.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup(content, 'lxml')
# print(data)
# for area in data.find_all('div', class_="col-xs-2-4 shopee-search-item-result__item"):