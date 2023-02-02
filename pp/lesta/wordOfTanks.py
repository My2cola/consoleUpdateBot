import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/world_of_tanks/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print("last updates Word Of Tanks: ",soup.find("time").text)
