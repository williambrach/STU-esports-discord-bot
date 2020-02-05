import sys
import discord
from User import author
from FileController import fileController
from WebScrapeController import webController
from Constants import text_constants
from WebScrapeController import lolApiController

async def compareMsg(msgList, conMsg):
    found = False
    async for msg in msgList:
        if str(msg.content) == str(conMsg):
            found = True
            break
        else:
            continue
    return found


def shutDownProcess():
    sys.exit(0)


class MyBot(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print(self.get_guild(615866592902774793).roles)
        lolApiController.getSummonerRank('Isamashii podsem', 'EUN1')
        shutDownProcess()
    async def sendLoginMessage(self, message):
        sender = author.createAuthorFromMessage(message.author)
        loginMsg = fileController.loadLoginMsg()
        user = self.get_user(sender.id)
        await user.send(loginMsg)
        await user.send(text_constants.ENTER_NAME_TEXT)

    async def parseCommand(self, message):
        if str(message.content).lower() == "!login".lower():
            await self.sendLoginMessage(message)
        elif str(message.content).lower() == "!q".lower():
            shutDownProcess()

    async def on_message(self, message):
        if message.author == self.user:
            return
        elif str(message.content).startswith("!"):
            await self.parseCommand(message)
        elif await compareMsg(message.channel.history(limit=2), text_constants.ENTER_NAME_TEXT):
            if webController.isStubaPerson(message):
                print("Is stuba person")
            else:
                print("Not stuba person")

    async def on_member_join(self, member):
        ##migrate whole code here
        print('Joined')
