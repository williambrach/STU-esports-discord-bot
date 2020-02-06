import sys
from discord.ext import commands
from discord.utils import get
from discord import client
from Constants import text_constants
from FileController import fileController
from User import author
from WebScrapeController import webController


def createBot():
    bot = commands.Bot(command_prefix='!')

    ############# EVENTS ##############

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

    @bot.command(pass_context=True)
    async def test(self, arg):
        guild = await bot.fetch_guild(615866592902774793)
        member = ""
        async for x in guild.fetch_members():
            if str(x.name) in str(self.message.author):
                member = x
                break
        print(member)
        role = get(guild.roles, name='MegaHracik')
        #member = guild.get_member(self.message.author)
        await member.add_roles(role)

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

    @bot.command()
    async def q(self, *arg):
        # TODO check permission if person calling has admin permission
        sys.exit(0)

    return bot
