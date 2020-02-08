def loadLoginMsg():
    f = open("./Data/txtFiles/welcomeMsg.txt", "r")
    return str(f.read())

def loadGamesMsg():
    f = open("./Data/txtFiles/gameMsg.txt", "r")
    return str(f.read())
