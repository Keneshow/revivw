class Cinema:
    def __init__(self, title, source, image):
        self.title = title
        self.source = source
        self.image = image

    def __str__(self):
        skip = "-----" * 25
        return (f'Название:       {self.title}'
                f'\nАфиша-URL:      {self.source}'
                f'\nФото-URL:       {self.image}'
                f'\n{skip}\n')

    @classmethod
    def from_selenium(cls, title, source, image):
        return cls(title, source, image)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://cinematica.kg/movies")

time.sleep(3)
# elements = driver.find_elements(By.CLASS_NAME, "movie-dummy")
# elements = driver.find_elements(By.TAG_NAME, "a")
elements = driver.find_elements(By.XPATH, "//a[@class='movie-dummy']")

for element in elements:
    source = element.get_attribute("href")
    title = element.find_element(By.XPATH, ".//div[@class='movie-title']").text
    image = element.find_element(By.XPATH, ".//img").get_attribute('src')

    print(title)
    print(source)
    print(image)
    print("----" * 20)

    a = Cinema.from_selenium(title, source,  image)

    with open("cinema.txt", "a", encoding='utf-8') as file:
        file.write(a.__str__())

driver.quit()