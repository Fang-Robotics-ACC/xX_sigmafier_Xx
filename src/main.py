from os import environ
from dotenv import load_dotenv 



def main():

    load_dotenv()
    token = environ['TOKEN']

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    client = SigmaClient(intents=intents)
    client.run(token)
# For the uninitiated, this a main guard
# It will only execute main if this file is the "entry point"
# If this file happens to be imported for some reason, main() will
# not be automatically executed
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do#419185

if __name__ == "__main__":
    main()
