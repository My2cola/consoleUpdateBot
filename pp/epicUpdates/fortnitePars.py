import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/fortnite/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print("last updates Fortnite: ",soup.find("time").text)

