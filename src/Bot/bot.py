import discord
from User import author
from FileController import fileController
from WebScrapeController import webController
from Constants import constants


async def compareMsg(msgList, conMsg):
    found = False
    async for msg in msgList:
        if str(msg.content) == str(conMsg):
            found = True
            break
        else:
            continue
    return found


class MyBot(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def processLogin(self, message):
        sender = author.createAuthorFromMessage(message.author)
        loginMsg = fileController.loadLoginMsg()
        user = self.get_user(sender.id)
        await user.send(loginMsg)
        await user.send(constants.ENTER_NAME_TEXT)
        # async for msg in message.channel.history(limit=3):
        #     print(msg.content)

    async def on_message(self, message):

        if message.author == self.user:
            return

        if await compareMsg(message.channel.history(limit=2), constants.ENTER_NAME_TEXT):
            if webController.isStubaPerson(message):
                print("Is stuba person")
            else:
                print("Not stuba person")
        if str(message.content).lower() == "!login".lower():
            await self.processLogin(message)
       # else if str(message.content).lower == "!q".lower():


        # user = self.get_user(sender.id)
        # await user.send('👀')
        # await message.author.send('👋')

    async def on_member_join(self, member):
        ##migrate whole code here
        print('Joined')
