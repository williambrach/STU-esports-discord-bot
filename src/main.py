from Constants import tokens
from Bot import bot
from WebScrapeController import lolApiController

def main():

    client = bot.createBot()
    client.run(tokens.token)


if __name__ == "__main__":
    main()