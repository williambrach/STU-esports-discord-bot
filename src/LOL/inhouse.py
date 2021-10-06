import math
import random

def shufflePlayers(players):

    playersQueue = list(players.items())

    sortPlayers = {
        "TOP" : list(),
        "JUNGLE" : list(),
        "MID" : list(),
        "ADC" : list(),
        "SUPPORT" : list(),
        "FILL" : list()
    }

    draftedPlayers = {
        "TOP" : list(),
        "JUNGLE" : list(),
        "MID" : list(),
        "ADC" : list(),
        "SUPPORT" : list()
    }

    for player_key in players:
        player = players[player_key]
        sortPlayers[player[0].upper()].append(player_key)


    playersPerRole = math.floor(len(players)/5)
    print(playersPerRole)

    positions = ["TOP", "JUNGLE", "MID", "ADC", "SUPPORT", "FILL"]
    for position in positions:
        if position.upper() == "FILL":
            continue
        len_sort = len(sortPlayers[position])

        if len_sort <=  playersPerRole:
            draftedPlayers[position].extend(sortPlayers[position][:len_sort])
            for player in draftedPlayers[position]:
                popPlayer(player,playersQueue)
                popPlayerDic(player,sortPlayers)
                
        len_draft = len(draftedPlayers[position])
        for i in range(playersPerRole-len_draft):
            if len(playersQueue) != 0:
                player_to_add = getBestPlayer(playersQueue,position)
                popPlayerDic(player_to_add,sortPlayers)
                draftedPlayers[position].append(player_to_add)

    for key in draftedPlayers.keys():
        random.shuffle(draftedPlayers[key])
    return draftedPlayers, playersPerRole, playersQueue

def generateReport(players,numberofteams,queue):

    msg = ""
    
    for i in range(numberofteams):
        msg += f"**TEAM {i+1}**\n"
        msg += "```\n"
        try:
            top = players['TOP'][i]
        except:
            top = ""
        try:
            jungle = players['JUNGLE'][i]
        except:
            jungle = ""
        try:
            mid = players['MID'][i]
        except:
            mid = ""
        try:
            adc = players['ADC'][i]
        except:
            adc = ""
        try:
            supp = players['SUPPORT'][i]
        except:
            supp = ""
        msg += f'TOP:   \t{top}\nJUNGLE:\t{jungle}\nMID:   \t{mid}\nADC:   \t{adc}\nSUPP:  \t{supp}\n\n'
        msg += "```\n"

    teams = list(range(1,numberofteams+1))
    random.shuffle(teams)

    for x in range(0,numberofteams, 2):
        if x+1 < numberofteams:
            msg += f"Team {teams[x]} vs Team {teams[x+1]}\n\n"
        else:
            msg += f'**Team {teams[x]} no opponent.**\n\n'
    

    msg += "**UNLUCKY PLAYERS**"
    msg += "```"
    if len(queue) != 0:
        for player in queue:
            msg += f'{player[0]}\t'
    else:
        msg += f'None :)'
    msg += "\n```"
    
    return msg


def getBestPlayer(queue,pos):
    maxScore = -1;
    maxPlayer = None
    for player in queue:
        playerScore = getScore(player,pos)
        if playerScore > maxScore:
            maxScore = playerScore
            maxPlayer = player

    popPlayer(maxPlayer[0],queue)

    return maxPlayer[0]

def popPlayer(name, queue):    
    for index,player in enumerate(queue):
        if player[0] == name:
            del queue[index]
            return

def popPlayerDic(name,players):
    for lane in players.keys():
        for index,player in enumerate(players[lane]):
            if player == name:
                del players[lane][index]


def getScore(player,pos):
    main = player[1][0].upper()
    off = player[1][1].upper()
    score = 0 
    if main == "FILL":
        return 3
    if pos == main:
        return 9 if off == "FILL" else 10
    if pos == off:
        score += 5
    if off == "FILL":
        score += 1
    return score
