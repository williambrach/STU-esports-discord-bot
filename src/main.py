from Bot import bot
from Constants import tokens


def main():

    client = bot.createBot()
    client.run(tokens.token)


if __name__ == "__main__":
    main()
