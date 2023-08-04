import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.tokopedia.com/search?st=product&q=macbook&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='
driver = webdriver.Chrome()
driver.get(url)


data = []
# for i in range(10):
for i in range(2):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
    time.sleep(2)

    for j in range(20):
        driver.execute_script("window.scrollBy(0, 250)")
        time.sleep(1)

    driver.execute_script("window.scrollBy(50, 0)")
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    # print(soup)

    for item in soup.findAll('div', class_='css-974ipl'):
        nama_produk = item.find(
            'div', class_='prd_link-product-name css-3um8ox').text
        harga = item.find(
            'div', class_="prd_link-product-price css-1ksb19c").text

        rtg = item.findAll('span', class_='css-t70v7i')
        if len(rtg) > 0:
            rating = item.find(
                'span', class_='css-t70v7i').text
        else:
            rating = ''

        tjl = item.findAll('span', class_='css-1duhs3e')
        if len(tjl) > 0:
            terjual = item.find(
                'span', class_='css-1duhs3e').text
        else:
            terjual = ''

        for item2 in item.findAll('div', class_='css-1rn0irl'):
            lokasi = item2.findAll(
                'span', class_='css-1kdc32b')[0].text
            toko = item2.findAll(
                'span', class_='css-1kdc32b')[1].text

            data.append((toko, lokasi, nama_produk, harga, terjual, rating))

    time.sleep(2)
    driver.find_element(
        By.CSS_SELECTOR, "button[aria-label='Laman berikutnya']").click()
    time.sleep(3)

df = pd.DataFrame(
    data, columns=['Toko', 'Lokasi', 'Nama_produk', 'Harga', 'Terjual', 'Rating'])
print(df)

df.to_excel("data_tokped.xlsx", index=False)
print('data berhasil disimpan')

driver.close()
