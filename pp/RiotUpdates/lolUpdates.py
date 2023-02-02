import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/league_of_legends/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print("last updates Lol: ",soup.find("time").text)
