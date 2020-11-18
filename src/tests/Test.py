import unittest
import asyncio
import aiounittest
import sys
import io
import os

sys.path.append('../src/')
from WebScrapeController import lolApiController
from WebScrapeController import csgoWebController
from WebScrapeController import dotaWebController
from WebScrapeController import webController
from Constants import text_constants
from FileController import fileController
from Bot import bot

class TestRiotApi(aiounittest.AsyncTestCase):

    async def test_getSummonerRank(self):
        summonerName = "isamashii podsem"
        server = "eune"
        rank = lolApiController.getSummonerRank(summonerName,server)
        self.assertTrue(True if rank in lolApiController.rankArray else False )

    async def test_getSummonerRankNoName(self):
        summonerName = ""
        server = "eune"
        rank = lolApiController.getSummonerRank(summonerName,server)
        self.assertTrue(True if rank == text_constants.NOT_FOUND else False)


class TestCSGOApi(aiounittest.AsyncTestCase):

    async def test_getCsgoRank(self):
        name = "DIVIX"
        level = csgoWebController.getCsgoRank(name)
        self.assertTrue(True if level in range(0,11) else False )

    async def test_getCsgoRankNoName(self):
        name = ""
        level = csgoWebController.getCsgoRank(name)
        self.assertFalse(level)


class TestDotaApi(aiounittest.AsyncTestCase):

    async def test_getDotaRank(self):
        name = "93680381"
        rank = dotaWebController.getDotaRank(name)
        self.assertTrue(True if rank in dotaWebController.dotaRanks else False )

    async def test_getDotaRankBadName(self):
        name = "3680381"
        rank = dotaWebController.getDotaRank(name)
        self.assertFalse(True if rank == text_constants.NOT_FOUND else False)


class TestAIS(aiounittest.AsyncTestCase):

    async def test_isStubaPerson(self):
        name = ('William', 'Brach')
        rank = webController.isStubaPerson(name)
        self.assertTrue(rank)

    async def test_isStubaPersonTitle(self):
        name = ('Bc.','William', 'Brach')
        rank = webController.isStubaPerson(name)
        self.assertTrue(rank)    

    async def test_isStubaPersonNoSTU(self):
        name = ('Urcite','Niesom ', 'STU')
        rank = webController.isStubaPerson(name)
        self.assertFalse(rank)

class TestFileController(aiounittest.AsyncTestCase):

    async def test_loadLoginMsg(self):
        f = io.open(os.path.abspath("Data/txtFiles/welcomeMsg.txt"), mode="r", encoding="utf-8")
        loadText = f.read()
        f.close()
        text = fileController.loadLoginMsg()
        self.assertEqual(loadText,text)

    async def test_loadGamesMsg(self):
        f = io.open(os.path.abspath("Data/txtFiles/gameMsg.txt"), mode="r", encoding="utf-8")
        loadText = f.read()
        f.close()
        text = fileController.loadGamesMsg()
        self.assertEqual(loadText,text)  

    async def test_loadCommands(self):
        f = io.open(os.path.abspath("Data/txtFiles/commands.txt"), mode="r", encoding="utf-8")
        loadText = f.read()
        f.close()
        text = fileController.loadCommands()
        self.assertEqual(loadText,text)

    async def test_loadBotInfo(self):
        f = io.open(os.path.abspath("Data/txtFiles/botinfo.txt"), mode="r", encoding="utf-8")
        loadText = f.read()
        f.close()
        text = fileController.loadBotInfo()
        self.assertEqual(loadText,text)

if __name__ == '__main__':
    unittest.main()
