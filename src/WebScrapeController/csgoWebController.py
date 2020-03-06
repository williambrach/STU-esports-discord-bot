import requests
from Constants import text_constants


def getCsgoRank(name):
    url = "https://api.faceit.com/core/v1/nicknames/{}".format(name)
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, timeout=5)
    if response.status_code != 200:
        return False
    level = response.json()["payload"]["games"]["csgo"]["skill_level"]
    if level == -1:
        return text_constants.NOT_FOUND

    return level
