from riotwatcher import RiotWatcher, ApiError
from Constants import tokens


def getSummonerRank(summonerName, region):
    watcher = RiotWatcher(tokens.lolapikey)

    try:
        summoner = watcher.summoner.by_name(region, summonerName)
        print(summoner)
    except ApiError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('Summoner with that ridiculous name not found.')
        else:
            raise

    try:
        my_ranked_stats = watcher.league.by_summoner(region, summoner['id'])
        print(my_ranked_stats)
    except ApiError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('Summoner with that ridiculous name not found.')
        else:
            raise