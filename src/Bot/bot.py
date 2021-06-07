import sys
import discord
from discord.ext import commands
from discord.utils import get
from Constants import discordConstants
from Constants import text_constants
from FileController import fileController
from User import author
from WebScrapeController import lolApiController
from WebScrapeController import webController
from WebScrapeController.dotaWebController import getDotaRank
from WebScrapeController.csgoWebController import getCsgoRank
from discord_components import DiscordComponents, Button

def createBot():
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix='!',intents=intents)

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
        await member.remove_roles(role)

    async def checkRole(guildId=discordConstants.BOTS_PROVING_GROUNDS_ID, role="", ctx=None):
        guild = await bot.fetch_guild(guildId)
        member = await getGuildMemberFromDM(message=ctx)
        role = get(guild.roles, name=role)
        if role in member.roles:
            return True
        else:
            return False

    ########### EVENTS

    @bot.event
    async def on_ready():
        DiscordComponents(bot)
        print('Im alive.')

    # @bot.command()
    # async def button(ctx):
    #     await ctx.send(
    #         "Hello, World!",
    #         components = [
    #             Button(label = "WOW button!")
    #         ]
    #     )

    #     interaction = await bot.wait_for("button_click", check = lambda i: i.component.label.startswith("WOW"))
    #     await interaction.respond(content = "Button clicked!")



    # Toto sa spravi ked sa niekto pripoji na nas Discord. 
    @bot.event
    async def on_member_join(member):
        loginMsg = fileController.loadLoginMsg()
        await member.send(loginMsg)
        
    ########### COMMANDS 

    # !ais, prikaz ktory prejde ais a zisti ci je clovek na stu.
    @bot.command(encoding='utf-8', name='ais')
    async def ais(self, *arg):
        "Skontroluje či si z STU."
        if len(arg) == 0:
            await self.send(text_constants.ERROR_ARGS.format("!ais"))
            return
        data = ' '.join(arg[0:])
        if data:
            if webController.isStubaPerson(arg):
                sender = author.createAuthorFromMessage(self.author)
                user = bot.get_user(sender.id)
                await setRole(role='STU', ctx=self)
                await self.send(text_constants.AIS_CONFIRMED)
                await user.send(fileController.loadGamesMsg())
            else:
                await self.send(text_constants.AIS_DENIED.format(data))
        else:
            return

    # @bot.command()
    # async def q(self, *arg):
    #     if await checkRole(role='Discord Admin', ctx=self):
    #         sys.exit(0)


    # !facebook - posle sa link na nas facebook
    @bot.command(name='facebook')
    async def facebook(self, *arg,):
        "Pošle ti link na náš facebook."
        area = self.message.channel
        await area.send(text_constants.FACEBOOK)

    # !instagram - posle sa link na nas instagram
    @bot.command( name="instagram")
    async def instagram(self, *arg):
        "Pošle ti link na náš instagram."
        area = self.message.channel
        await area.send(text_constants.INSTAGRAM)


    # !twitch - posle sa link na nas twitch
    @bot.command(name="twitch")
    async def twitch(self, *arg):
        "Pošle ti link na náš Twitch."
        area = self.message.channel        
        await area.send(text_constants.TWITCH)

    # !logo - posle sa link na google drive v ktorom mame vsetky loga
    @bot.command(name="logo")
    async def logo(self, *arg):
        "Pošle ti naše logo."
        area = self.message.channel
        await area.send(text_constants.LOGO)


    # !login - sprava ktora pride pouzivatelovi ked sa pripoji na server
    @bot.command(name="login")
    async def login(self, *arg):
        "Uvítacia správa."
        sender = author.createAuthorFromMessage(self.author)
        loginMsg = fileController.loadLoginMsg()
        user = bot.get_user(sender.id)
        await user.send(loginMsg)


    # !pog - posle sa do chatu obrazok pogchamp, ktory sa po 30 sec zmaze. Taktiez sa zmaze command !pog
    @bot.command( name="pog")
    async def pog(self, *arg):
        "Pog!!"
        area = self.message.channel
        await self.message.delete()
        await area.send('https://i0.wp.com/nerdschalk.com/wp-content/uploads/2020/08/pogger.png?resize=311%2C307&ssl=1',delete_after=30)

    
    # !lol, priradi pouzivatelovi rolu lol 
    @bot.command(encoding='utf-8', name="lol")
    async def lol(self, *arg):
        "Prida ti League of Legends rolu + tvoj rank."
        if len(arg) == 0:
            await self.send(text_constants.ERROR_ARGS.format("!lol"))
            return
        if await checkRole(role='STU', ctx=self):
            name, server = parseLolCommand(arg)
            rank = lolApiController.getSummonerRank(name, server)
            if rank == text_constants.NOT_FOUND:
                await self.send(text_constants.NOT_FOUND_MSG_LOL.format(name, server))
            else:
                if not rank:
                    await setRole(role="League of Legends", ctx=self)
                    await self.send(text_constants.LOL_SUCCEED)
                    return
                parsedRank = rank[0:1] + rank[1:].lower()
                await setRole(role="League of Legends", ctx=self)
                await setRole(role=parsedRank, ctx=self)
                await self.send(text_constants.LOL_SUCCEED_RANK.format(parsedRank))
        else:
            await self.send(text_constants.NEED_ROLE.format("STU", "!lol", "!ais"))

    # !lolrole, prideli ti rolu podla vstupu
    @bot.command(name="lolrole")
    async def lolrole(self, *arg):
        "Prida ti tvoju poziciu v League of Legends."
        if len(arg) == 0:
            await self.send(text_constants.ERROR_ARGS.format("!lolrole"))
            return
        if await checkRole(role='League of Legends', ctx=self) and await checkRole(role='STU', ctx=self):
            if arg[0].upper() in lolApiController.rolesDict:
                if await checkRole(role=lolApiController.rolesDict[arg[0].upper()], ctx=self):
                    await removeRole(role=lolApiController.rolesDict[arg[0].upper()], ctx=self)
                    await self.send(text_constants.LOL_REMOVE_ROLE.format(lolApiController.rolesDict[arg[0].upper()]))
                else:
                    await setRole(role=lolApiController.rolesDict[arg[0].upper()], ctx=self)
                    await self.send(text_constants.LOL_ADD_ROLE.format(lolApiController.rolesDict[arg[0].upper()]))
            else:
                await self.send(text_constants.ROLE_NOT_FOUND.format(arg[0]))
        else:
            await self.send(text_constants.NEED_ROLE.format("League of legends a STU", "!lolrole", "!ais a !lol"))

    # !dotarole, prideli ti rolu podla vstupu
    @bot.command(name="dotarole")
    async def dotarole(self, *arg):
        "Prida ti tvoju poziciu v dote."
        if len(arg) == 0:
            await self.send(text_constants.ERROR_ARGS.format("!dotarole"))
            return
        if await checkRole(role='Dota', ctx=self) and await checkRole(role='STU', ctx=self):
            roleinput = ' '.join(arg[0:]).upper()
            if roleinput in lolApiController.dotaDic:
                if await checkRole(role=lolApiController.dotaDic[roleinput], ctx=self):
                    await removeRole(role=lolApiController.dotaDic[roleinput], ctx=self)
                    await self.send(text_constants.DOTA_REMOVE_ROLE.format(lolApiController.dotaDic[roleinput]))
                else:
                    await setRole(role=lolApiController.dotaDic[roleinput], ctx=self)
                    await self.send(text_constants.DOTA_ADD_ROLE.format(lolApiController.dotaDic[roleinput]))
            else:
                await self.send(text_constants.ROLE_NOT_FOUND.format(roleinput))
        else:
            await self.send(text_constants.NEED_ROLE.format("Dota a STU", "!dotarole", "!ais a !dota"))

    # !dota
    @bot.command(name="dota")
    async def dota(self, *arg):
        "Prida ti rolu Dota"
        if len(arg) == 0:
            await self.send(text_constants.ERROR_ARGS.format("!dota"))
            return
        if await checkRole(role='STU', ctx=self):
            rank = getDotaRank(arg[0])
            if rank == text_constants.NOT_FOUND:
                await setRole(role="Dota", ctx=self)
                await self.send(text_constants.DOTA_SUCCEED)
            else:
                await setRole(role="Dota", ctx=self)
                await setRole(role=rank, ctx=self)
                await self.send(text_constants.DOTA_SUCCEED_RANK.format(rank))
        else:
            await self.send(text_constants.NEED_ROLE.format("STU", "!dota", "!ais"))

    # !valorant
    @bot.command(name="valorant")
    async def valorant(self, *arg):
        "Prida ti rolu Valorant"
        if len(arg) == 0:
            await self.send(text_constants.ERROR_ARGS.format("!valorant"))
            return
        if await checkRole(role='STU', ctx=self):
            userInput = ' '.join(arg).split("#")
            gameName = userInput[0]
            tagline = userInput[1]

            ## TODO WHEN VALO API
            #rank = lolApiController.getValoRank(gameName, tagline)
            rank = text_constants.NOT_FOUND
            if rank == text_constants.NOT_FOUND:
                await setRole(role="Valorant", ctx=self)
                await self.send(text_constants.VALO_SUCCEED)
            else:
                await setRole(role="Valorant", ctx=self)
                await self.send(text_constants.VALO_SUCCEED_RANK.format(rank))
        else:
            await self.send(text_constants.NEED_ROLE.format("STU", "!valorant", "!ais"))

    # !cmd
    @bot.command(name="cmd")
    async def cmd(self, *arg):
        "Vypise ti detailnejšie ako sa pouzivaju jednotlive prikazy."
        sender = author.createAuthorFromMessage(self.author)
        bot_commands = fileController.loadCommands()
        user = bot.get_user(sender.id)
        await user.send(bot_commands)
        #await user.send("TODO, treba to fixnut...")

    # !botinfo
    @bot.command()
    async def botinfo(self, *arg):
        "Informacie ohladom bota."
        bot_commands = fileController.loadBotInfo()
        sender = author.createAuthorFromMessage(self.author)
        user = bot.get_user(sender.id)
        await user.send(bot_commands)

    # !notstu
    @bot.command(name="notstu")
    async def notstu(self, *arg):
        "Pridá ti rolu notstu."
        if await checkRole(role='STU', ctx=self):
            await self.send("Už máš rolu STU... Nemôžeš mať aj rolu NOT-STU.")
            return 
        else:
            await setRole(role="NOT-STU", ctx=self)
            await self.send("Bola ti pridelená rola - NOT-STU.")
        
    # !csgo        
    @bot.command(name="csgo")
    async def csgo(self, *arg):
        "Prida ti rolu CSGO + tvoj faceit rank."
        if len(arg) == 0:
            await self.send(text_constants.ERROR_ARGS.format("!csgo"))
            return
        if await checkRole(role='STU', ctx=self):
            level = getCsgoRank(arg[0])
            if level == text_constants.NOT_FOUND:
                await setRole(role="CSGO", ctx=self)
                await self.send(text_constants.CSGO_SUCCEED)
            else:
                role = "Faceit " + str(level)
                await setRole(role="CSGO", ctx=self)
                await setRole(role=role, ctx=self)
                await self.send(text_constants.CSGO_SUCCEED_RANK.format(role))
        else:
            await self.send(text_constants.NEED_ROLE.format("STU", "!csgo", "!ais"))

    return bot
