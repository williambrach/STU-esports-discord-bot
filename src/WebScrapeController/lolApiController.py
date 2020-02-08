from riotwatcher import RiotWatcher, ApiError
from Constants import tokens


def getSummonerRank(summonerName, region):
    watcher = RiotWatcher(tokens.lolapikey)
    summoner = watcher.summoner.by_name(region, summonerName)
    #my_ranked_stats = watcher.league.by_summoner(region, summoner['id'])
    #print(my_ranked_stats)
