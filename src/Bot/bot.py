import sys
from discord.ext import commands
from Constants import text_constants
from FileController import fileController
from User import author
from WebScrapeController import webController


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


def createBot():
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print('Im alive')

    @bot.event
    async def sendLoginMessage(self, message):
        sender = author.createAuthorFromMessage(message.author)
        loginMsg = fileController.loadLoginMsg()
        user = self.get_user(sender.id)
        await user.send(loginMsg)
        await user.send(text_constants.ENTER_NAME_TEXT)

    @bot.event
    async def on_member_join():
        # migrate whole code here
        print('Joined')

    ############# Commands ##############

    @bot.command()
    async def test(self, arg):
        print(arg)
        # await self.send(arg)

    @bot.command()
    async def ais(self, *arg):
        data = ' '.join(arg[0:])
        if data:
            if webController.isStubaPerson(data):
                tmp = "Is stuba person"
            else:
                tmp = "Not stuba person"
            await self.send(tmp)
        else:
            return

    return bot
