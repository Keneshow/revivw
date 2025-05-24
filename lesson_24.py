#
#
# class Product:
#     def __init__(self, name, price_som):
#         self.name = name
#         self.price_som = price_som
#
#
#     @classmethod
#     def to_som(cls, name):
#         price_som = price * 87.5
#         return cls(name, price_som)
#
#
# class User:
#     def __init__(self, username, avatar):
#         self.username = username
#         self.avatar = avatar
#
#
#     @classmethod
#     def from_dict(cls, data):
#         return cls(data['username'], ['data'])
#
#
# user = {
#     'username': 'user_1'
#     'avatar': 'user_avatar'
# }
#
# user_2 = 'user_2, user_avatar'
# user_1 = User.from_dict()


#############################  Technodom.kg

import requests
from bs4 import BeautifulSoup

url = "https://new.technodom.kg/category/fototehnika-i-kvadrokoptery"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

products = soup.find_all("div", class_="common__recommendations__list__item one-four")

for product in products:
    title = product.find("div", class_="common__recommendations__list__item__title").text
    price = product.find("div", class_="common__recommendations__list__item__price").text
    image = product.find("a")["data-background-image"]
    print(title)
    print(price)
    print(image)
    print("---"*20)



##############################  Tazabek.kg


import requests
from bs4 import BeautifulSoup

url = "https://www.tazabek.kg/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

news =soup.find_all("div", class_="lenta-row")

urls = []
for i in news:
    date = i.find("div", class_="lenta-row-date").text
    title = i.find('div', class_="lenta-row-title").text
    news_url = i.find("a")["href"]
    norm_url = url + news_url
    urls.append(norm_url)
    print(date)
    print(title)
    print(norm_url)

    print(f'{urls}\n')

for urls in url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    news = soup.find("h2", class_="title")
    if news:
        title = news.text
    else:
        continue


#############################################
#
# class Movie:
#     def __init__(self, title, genre, age, image):
#         self.title = title
#         self.genre = genre
#         self.age = age
#         self.image = image
#
#     def __str__(self):
#         propusk = "----" * 20
#         return f'{title}\n{genre}\n{age}\n{image}\n "-----"\n'
#
#     @classmethod
#     def from_parser(cls, title, genre, age, image):
#         return cls(title, genre, age, image)
#
#
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://manascinema.com"
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, "lxml")
#
# products = soup.find_all("a", class_="creation-time")

# for product in products:
#     age = product.find("div", class_="age").text
#     title = product.find("div", class_="creation-title").text
#     genre = product.find("div", class_="creation-info").text
#    # normal_genre = genre.replace()
#     image = product.find("img")["src"]
#
#     full_image_url = url + image
#     #
#     # print(age)
#     # print(title)
#     # print(genre)
#     # print(url + image)
#     #
#     p = Movie.from_parser(title, genre, age, image)
#
#     with open("for_info.txt", "a", encoding='utf-8') as file:
#         file.write(p.__str__(Movie))

import lxml

import requests

from bs4 import BeautifulSoup

for i in range (1, 140):
    url = f''


url = "https://store.steampowered.com/search/?term="

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml" )

names = soup.find_all("a")

for name in games:
    name = game.find("span", class_="title")
    if name is not None:
        print(name)