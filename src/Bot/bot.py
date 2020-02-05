import discord
from User import author
from FileController import fileController

class MyBot(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def processLogin(self, message):
        sender = author.createAuthorFromMessage(message.author)
        loginMsg = fileController.loadLoginMsg()
        user = self.get_user(sender.id)
        await user.send(loginMsg)
        # async for msg in message.channel.history(limit=3):
        #     print(msg.content)

    async def on_message(self, message):
        if str(message.content).lower() == "!login".lower():
            await self.processLogin(message)

        # user = self.get_user(sender.id)
        # await user.send('👀')
        # await message.author.send('👋')

    async def on_member_join(self, member):
        ##migrate whole code here
        print('Joined')
