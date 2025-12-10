import discord
from os import environ
from dotenv import load_dotenv 

load_dotenv()
token = environ['TOKEN']

def is_member_or_onboarding(member):
    for role in member.roles:
        if role.name == "Onboarding" or role.name == "Member":
            return True
    return False

class SigmaClient(discord.Client):
    async def on_ready(self):
        for guild in self.guilds:
            for member in guild.members:
                #print(member.roles)
                if(is_member_or_onboarding(member)):
                    print(member.name)
        print(f'Logged on as {self.user}!')



    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        author = message.author

        if message.content.startswith('!hello motto'):
            await message.reply('ur actually rlly cool, and you dont smell like pizza', mention_author=True)
            await author.send("Derp Motto")

        elif message.content.startswith('!hello'):
            await message.reply('still stinky', mention_author=True)
            await author.send("Derp")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = SigmaClient(intents=intents)
client.run(token)
