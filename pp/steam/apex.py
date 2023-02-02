import requests
from bs4 import BeautifulSoup

url = "https://www.playground.ru/apex_legends/news/updates"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print("last updates Apex: ",soup.find("time").text)
