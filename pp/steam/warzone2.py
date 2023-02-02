import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/call_of_duty_warzone_20/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print("last updates Warzone 2.0: ",soup.find("time").text)
