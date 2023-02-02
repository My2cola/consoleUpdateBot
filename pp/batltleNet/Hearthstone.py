import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/hearthstone/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("last updates Hearthstone: ",soup.find("time").text)
