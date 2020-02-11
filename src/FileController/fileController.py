import io

def loadLoginMsg():
    f = io.open("./Data/txtFiles/welcomeMsg.txt", mode="r", encoding="utf-8")
    return f.read()

def loadGamesMsg():
    f = io.open("./Data/txtFiles/gameMsg.txt", mode="r", encoding="utf-8")
    return f.read()
