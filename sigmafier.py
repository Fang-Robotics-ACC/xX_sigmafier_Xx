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
        await self.ask_weekly_commit()
       

    async def ask_weekly_commit(self):
        await self.blast_all_participants("Whats your weekly commit")


    async def get_commits(self,message_content):
        for participant in self._fang_participants:
            try:
                await participant.send(message_content)
            except:
                print(participant.name + " did not recieve message!!!")

        # await self.blast_all_participants("Whats your weekly commit")




    async def on_message(self, message):
        ##lists for checking in message
        ##----stupid lists
        gyat_list=["gyat maxxing","Gyat maxxing","Gyatt maxxing","gyatt maxxing"]
        alex_pizaa_list=["Hi im alex", "my names alex","my name is alex","My names alex, My name is alex"]
        leahs_awesome_list=["leah sucks","Leah sux","leah sux","leah suxs","Leah sucks"]
        ##----useful lists
        commit_responses=["My commit this week is"]

        # checks that the message is not from the bot itself (message.author)
        if message.author.id == self.user.id:
            return
        author = message.author

        ## commit message section ##
        commits_dict={}
        if message.content in commit_responses:
            commits_dict[self.user.id] = message.content
            await message.reply("place holder")

        ### stupid stuff ###
        elif message.content.startswith('!hello motto'):
            await message.reply('ur actually rlly cool, and you dont smell like pizza', mention_author=True)
            await author.send("Derp Motto")
        elif message.content.startswith('!hello'):
            await message.reply('still stinky', mention_author=True)
            await author.send("Derp")
        elif message.content in alex_pizaa_list:
            await message.reply("you smell like pizza")
        elif  message.content in gyat_list:
            await message.reply("Jake twerks a lot")
        elif message.content in leahs_awesome_list:
            await message.reply("You're not a sigma")


        


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = SigmaClient(intents=intents)
client.run(token)
