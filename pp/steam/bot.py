import requests
from datetime import datetime


def get_latest_update_date(appid, game_name=None):
    api_key = "<A36ACEEB1E3FB775F95949A5B8F608BC>"
    url = f"http://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={appid}&count=1&maxlength=300&format=json&key={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                updates = data["appnews"]["newsitems"]
                update = updates[0]
                update_date = datetime.fromtimestamp(int(update['date'])).strftime("%Y-%m-%d")
                return f"The latest update for {game_name if game_name else appid} was released on {update_date}"
            except (KeyError, TypeError, ValueError) as e:
                return "Error occured while parsing response data: " + str(e)
        else:
            return None
    except requests.exceptions.RequestException as e:
        return "Error occured while retrieving updates:" + str(e)

# сюда указываем id игры стима по которой нужно получить обновление 
games = {
570: "Dota 2",
730: "CS:GO",
578080: "PUBG",
271590: "GTA V",
444090: "Paladins",
252490: "Rust",
230410: "Warframe",
218620: "Payday 2",
221100: "DayZ",
550: "Left 4 Dead 2"
}
# выводим результат обновлений в консоль
for appid, game_name in games.items():
    result = get_latest_update_date(appid, game_name)
    if result:
        print(result)
