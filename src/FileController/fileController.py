import io
import os


def loadLoginMsg():
    f = io.open(os.path.abspath("Data/txtFiles/welcomeMsg.txt"), mode="r", encoding="utf-8")
    text = f.read()
    f.close()
    return text

def loadGamesMsg():
    f = io.open(os.path.abspath("Data/txtFiles/gameMsg.txt"), mode="r", encoding="utf-8")
    text = f.read()
    f.close()
    return text

def loadCommands():
    f = io.open(os.path.abspath("Data/txtFiles/commands.txt"), mode="r", encoding="utf-8")
    text = f.read()
    f.close()
    return text

def loadBotInfo():
    f = io.open(os.path.abspath("Data/txtFiles/botinfo.txt"), mode="r", encoding="utf-8")
    text = f.read()
    f.close()
    return text
