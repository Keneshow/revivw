import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


USD_to_KGS = 88.7

class Steam:
    def __init__(self, title, date_time, price_usd, price_kgs, source):
        self.title = title
        self.date_time = date_time
        self.price_usd = price_usd
        self.price_kgs = price_kgs
        self.source = source

    def __str__(self):
        skip = "-----" * 20
        return (f'Название:     {self.title}'
                f'\nДата-выхода:  {self.date_time}'
                f'\nЦена->USD:    {self.price_usd}'
                f'\nЦена->KGS:    {self.price_kgs}'
                f'\nСсылка->URL:  {self.source}'
                f'\n{skip}\n')

    @classmethod
    def from_steam(cls, title, date_time, price_raw, source):
        match = re.search(r"\$([\d.,]+)", price_raw)
        if match:
            price_usd = match.group(1).replace(",", "")
            price_float = float(price_usd)
            price_kgs = round(price_float * USD_to_KGS, 2)
            price_kgs_str = f"{price_kgs} сом"
            price_usd_str = f"${price_usd}"
        else:
            price_usd_str = price_raw
            price_kgs_str = "Бесплатно / Не указано"
        return cls(title, date_time, price_usd_str, price_kgs_str, source)



options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://store.steampowered.com/search/?term=")

time.sleep(3)



last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'search_result_row')]")

for element in elements:
    source = element.get_attribute("href")
    title = element.find_element(By.XPATH, ".//span[@class='title']").text
    try:
        date_time = element.find_element(By.XPATH, ".//div[contains(@class, 'search_released')]").text
    except:
        date_time = "Дата не найдена"

    try:
        price = element.find_element(By.XPATH, ".//div[contains(@class, 'search_price')]").text.strip()
        if not price:
            price = "Бесплатно"
    except:
        price = "Цена не найдена"

    s = Steam.from_steam(title, date_time, price, source)
    print(s)

    with open("steam.txt", 'a', encoding='utf-8') as file:
        file.write(s.__str__())

driver.quit()