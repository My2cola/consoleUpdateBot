import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/warface/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print("last updates Warface: ",soup.find("time").text)
