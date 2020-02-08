import requests


def getDotaRank(steamId):
    acc_id = int(steamId)

    url = "https://www.dotabuff.com/search?utf8=%E2%9C%93&q={0}&commit=Search".format(acc_id)
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, timeout=5)

    if response.status_code != 200:
        return False

    rankHead = 'title="Rank:'

    rankPos = response.text.find(rankHead)
    if rankPos == -1:
        return 'anonym'

    rankText = response.text[rankPos + len(rankHead) + 1:]
    rankText = rankText[:rankText.find('"')]
    if rankText.find(' '):
        rankText = rankText[:rankText.find(' ')]

    return rankText
