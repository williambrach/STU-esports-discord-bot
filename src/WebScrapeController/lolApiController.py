from riotwatcher import RiotWatcher, ApiError
from Constants import tokens
from Constants import text_constants

regionDict = {
    "EUNE": "EUN1",
    "EUW": "EUW1",
    "NA": "NA1",
    "RU": "RU",
    "KR": "KR",
    "BR": "BR1",
    "OC": "OC1",
    "JP": "JP1",
    "TR": "TR1",
    "LA": "LA1"
}

rolesDict = {
    "TOP": "Top",
    "JUNGLE": "Jungle",
    "MID": "Mid",
    "ADC": "Adc",
    "SUPP": "Supp"
}


def getSummonerRank(summonerName, region):
    server = regionDict[str(region).upper()]
    watcher = RiotWatcher(tokens.lolapikey)
    try:
        summoner = watcher.summoner.by_name(server, summonerName)
    except:
        return text_constants.NOT_FOUND
    my_ranked_stats = watcher.league.by_summoner(server, summoner['id'])
    for rank in my_ranked_stats:
        if rank['queueType'] == "RANKED_SOLO_5x5":
            return rank['tier']
