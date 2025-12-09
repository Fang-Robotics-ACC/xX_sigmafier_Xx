import discord
from os import environ
from dotenv import load_dotenv 

load_dotenv()
token = environ['TOKEN']


class SigmaClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello motto'):
            await message.reply('ur actually rlly cool, and you dont smell like pizza', mention_author=True)
        elif message.content.startswith('!hello'):
            await message.reply('still stinky', mention_author=True)

intents = discord.Intents.default()
intents.message_content = True

client = SigmaClient(intents=intents)
client.run(token)
