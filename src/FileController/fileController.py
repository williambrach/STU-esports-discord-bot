import io
import os


def loadLoginMsg():
    f = io.open(os.path.abspath("Data/txtFiles/welcomeMsg.txt"), mode="r", encoding="utf-8")
    return f.read()

def loadGamesMsg():
    f = io.open(os.path.abspath("Data/txtFiles/gameMsg.txt"), mode="r", encoding="utf-8")
    return f.read()

def loadCommands():
    f = io.open(os.path.abspath("Data/txtFiles/commands.txt"), mode="r", encoding="utf-8")
    return f.read()

def loadBotInfo():
    f = io.open(os.path.abspath("Data/txtFiles/botinfo.txt"), mode="r", encoding="utf-8")
    return f.read()
