import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/genshin_impact/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print("last updates Genshin: ",soup.find("time").text)
