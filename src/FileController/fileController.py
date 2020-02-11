import io

def loadLoginMsg():
    f = io.open("./Data/txtFiles/welcomeMsg.txt", mode="r", encoding="utf-8")
    return f.read()

def loadGamesMsg():
    f = io.open("./Data/txtFiles/gameMsg.txt", mode="r", encoding="utf-8")
    return f.read()

def loadCommands():
    f = io.open("./Data/txtFiles/commands.txt", mode="r", encoding="utf-8")
    return f.read()

def loadBotInfo():
    f = io.open("./Data/txtFiles/botinfo.txt", mode="r", encoding="utf-8")
    return f.read()
