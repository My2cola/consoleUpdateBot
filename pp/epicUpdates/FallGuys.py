import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/fall_guys_ultimate_knockout/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("last updates FallGys: ",soup.find("time").text)
