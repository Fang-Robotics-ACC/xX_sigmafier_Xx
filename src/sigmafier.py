import discord
from os import environ
from dotenv import load_dotenv 

load_dotenv()
token = environ['TOKEN']

def is_member_or_onboarding(member):
    for role in member.roles:
        if (role.name == "Onboarding" or role.name == "Member") and not (role.name == "Faculty Advisor"):
            return True
    return False

class SigmaClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fang_participants = []

    async def blast_all_participants(self, message_content):
        for participant in self._fang_participants:
            try:
                await participant.send(message_content)
            except:
                print(participant.name + " did not recieve message!!!")

    async def on_ready(self):
        for guild in self.guilds:
            for member in guild.members:
                #print(member.roles)
                if(is_member_or_onboarding(member)):
                    self._fang_participants.append(member)
        print(f'Logged on as {self.user}!')
        await self.blast_all_participants("This is a mass dm test from Fang Robotics... yay!!!!")




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

        if message.channel.type == discord.ChannelType.private:
            print("Message is in dm")
            print(message.content)
        else:
            print("Message is not in dm")
            print(message.content)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = SigmaClient(intents=intents)
client.run(token)
