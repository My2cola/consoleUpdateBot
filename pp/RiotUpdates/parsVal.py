import requests
from bs4 import BeautifulSoup
import datetime

url = "https://валорант.рф/patch/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    elements = soup.find_all("p", class_="post-date")

    latest_update = None

    for element in elements:
        date_string = element.text
        date_object = datetime.datetime.strptime(date_string, '\n%d.%m.%Y\n')
        if latest_update is None or date_object > latest_update:
            latest_update = date_object

    print("Latest Update Valorant:", latest_update.strftime("%d %B %Y"))
else:
    print(f"Request failed with status code: {response.status_code}")
