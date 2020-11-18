import discord.ext.test as dpytest
import pytest
import unittest
import asyncio
import aiounittest
import sys
import io
import os
import pytest
sys.path.append('../src/')
from Bot import bot
from Constants import tokens
from Constants import text_constants
from FileController import fileController


@pytest.mark.asyncio
async def test_facebook():
    x = bot.createBot()
    dpytest.configure(x)
    await dpytest.message("!facebook")
    dpytest.verify_message(text_constants.FACEBOOK)

@pytest.mark.asyncio
async def test_instagram():
    x = bot.createBot()
    dpytest.configure(x)
    await dpytest.message("!instagram")
    dpytest.verify_message(text_constants.INSTAGRAM)

@pytest.mark.asyncio
async def test_twitch():
    x = bot.createBot()
    dpytest.configure(x)
    await dpytest.message("!twitch")
    dpytest.verify_message(text_constants.TWITCH)

@pytest.mark.asyncio
async def test_logo():
    x = bot.createBot()
    dpytest.configure(x)
    await dpytest.message("!logo")
    dpytest.verify_message(text_constants.LOGO)

@pytest.mark.asyncio
async def test_login():
    x = bot.createBot()
    dpytest.configure(x)
    loginMsg = fileController.loadLoginMsg()
    userMessage = loginMsg + "\n" + text_constants.ENTER_NAME_TEXT
        
    await dpytest.message("!login")
    dpytest.verify_message(userMessage)



