from Constants import tokens
from Bot import bot
from WebScrapeController import lolApiController

def main():

    client = bot.MyBot()
    client.run(tokens.token)


if __name__ == "__main__":
    main()