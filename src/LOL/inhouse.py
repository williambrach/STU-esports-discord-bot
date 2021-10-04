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
        if player[0].upper() == "TOP":
            sortPlayers['TOP'].append(player_key)
        elif player[0].upper() == "JUNGLE":
            sortPlayers['JUNGLE'].append(player_key)
        elif player[0].upper() == "MID":
            sortPlayers['MID'].append(player_key)
        elif player[0].upper() == "ADC":
            sortPlayers['ADC'].append(player_key)
        elif player[0].upper() == "SUPPORT":
            sortPlayers['SUPPORT'].append(player_key)
        elif player[0].upper() == "FILL":
            sortPlayers['FILL'].append(player_key)

    playersPerRole = round(len(players)/5)

    positions = ["TOP", "JUNGLE", "MID", "ADC", "SUPPORT", "FILL"]
    for position in positions:
        print(position)
        if position.upper() == "FILL":
            continue
        if len(sortPlayers[position]) <=  playersPerRole:
            draftedPlayers[position].extend(sortPlayers[position][:len(sortPlayers[position])])
            for player in draftedPlayers[position]:
                popPlayer(player,playersQueue)
            if len(sortPlayers[position]) <  playersPerRole:
                if len(playersQueue) != 0:
                    draftedPlayers[position].append(getBestPlayer(playersQueue,position))                
                    pass
        else:
            random.shuffle(sortPlayers[position])
            draftedPlayers[position].extend(sortPlayers[position][:playersPerRole])
            for player in draftedPlayers[position]:
                popPlayer(player,playersQueue)
    return draftedPlayers, playersPerRole

def generateReport(players,numberofteams):

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
    for x in range(1,numberofteams+1, 2):
        if x+1 <= numberofteams:
            msg += f"Team {x} vs Team {x+1}\n"
        else:
            msg += f'**Team {x} no opponent.**'
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
