import sys
from discord.ext import commands
from discord.utils import get
from discord import client
from Constants import text_constants
from Constants import discordConstants
from FileController import fileController
from User import author
from WebScrapeController import webController
from WebScrapeController import lolApiController


def createBot():
    bot = commands.Bot(command_prefix='!')

    def parseLolCommand(arg):
        server = "EUNE"
        if "#" in ' '.join(arg):
            userInput = ' '.join(arg).split("#")
            name = userInput[0]
            server = userInput[1]
        else:
            name = ' '.join(arg)
        return name, server

    async def getGuildMemberFromDM(guildId=discordConstants.BOTS_PROVING_GROUNDS_ID, message=None):
        guild = await bot.fetch_guild(guildId)
        member = ""
        async for x in guild.fetch_members():
            if str(x.name) in str(message.author):
                member = x
                break
        return member

    async def setRole(guildId=discordConstants.BOTS_PROVING_GROUNDS_ID, role="", ctx=None):
        guild = await bot.fetch_guild(guildId)
        member = await getGuildMemberFromDM(message=ctx)
        role = get(guild.roles, name=role)
        await member.add_roles(role)

    async def removeRole(guildId=discordConstants.BOTS_PROVING_GROUNDS_ID, role="", ctx=None):
        guild = await bot.fetch_guild(guildId)
        member = await getGuildMemberFromDM(message=ctx)
        role = get(guild.roles, name=role)
        await member.remove_roels(role)

    async def checkRole(guildId=discordConstants.BOTS_PROVING_GROUNDS_ID, role="", ctx=None):
        guild = await bot.fetch_guild(guildId)
        member = await getGuildMemberFromDM(message=ctx)
        role = get(guild.roles, name=role)
        if role in member.roles:
            return True
        else:
            return False

    ############# EVENTS ##############

    @bot.event
    async def on_ready():
        print('Im alive')

    @bot.event
    async def on_member_join():
        # migrate whole code here
        print('Joined')

    ############# Commands ##############

    @bot.command(pass_context=True)
    async def test(self, arg):
        pass

    @bot.command()
    async def ais(self, *arg):
        data = ' '.join(arg[0:])
        if data:
            if webController.isStubaPerson(data):
                await setRole(role='STU', ctx=self)
                await self.send(text_constants.AIS_CONFIRMED)
                await setRole(role='MegaHracik', ctx=self)
                await self.send(fileController.loadGamesMsg())
            else:
                await self.send(text_constants.AIS_DENIED.format(data))
        else:
            return

    @bot.command()
    async def q(self, *arg):
        # TODO check permission if person calling has admin permission
        sys.exit(0)

    @bot.command()
    async def login(self, *arg):
        sender = author.createAuthorFromMessage(self.author)
        loginMsg = fileController.loadLoginMsg()
        user = bot.get_user(sender.id)
        await user.send(loginMsg)
        await user.send(text_constants.ENTER_NAME_TEXT)

    @bot.command()
    async def lol(self, *arg):
        if await checkRole(role='STU', ctx=self):
            name, server = parseLolCommand(arg)
            rank = lolApiController.getSummonerRank(name, server)
            if rank == text_constants.NOT_FOUND:
                await self.send(text_constants.NOT_FOUND_MSG_LOL.format(name, server))
            else:
                if not rank:
                    await setRole(role="League of Legends", ctx=self)
                    return
                parsedRank = rank[0:1] + rank[1:].lower()
                await setRole(role="League of Legends", ctx=self)
                await setRole(role=parsedRank, ctx=self)
        else:
            await self.send(text_constants.PERMISSION_DENIED)

    @bot.command()
    async def lolrole(self, *arg):
        if await checkRole(role='League of Legends', ctx=self):
            if arg[0].upper() in lolApiController.rolesDict:
                await setRole(role=lolApiController.rolesDict[arg[0].upper()], ctx=self)
            else:
                # wrong role
                pass

    @bot.command()
    async def dota(self, *arg):
        # TODO check permission if person calling has admin permission
        sys.exit(0)

    @bot.command()
    async def csgo(self, *arg):
        # TODO check permission if person calling has admin permission
        sys.exit(0)

    return bot
