import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/among_us/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print("last updates AmongUs: ",soup.find("time").text)

