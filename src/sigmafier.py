import discord
from member_filters import is_fang_participant
from sillly_dialogue import SillyDialogue

class Sigmafier(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fang_participants = []
        self._silly_dialogue = SillyDialogue()

    async def blast_all_participants(self, message_content):
        for participant in self._fang_participants:
            try:
                await participant.send(message_content)
            except:
                print(participant.name + " did not recieve message!!!")

    async def on_ready(self):
        self.initialize_fang_participants();
        print(f'Logged on as {self.user}!')
        # await self.blast_all_participants("This is a mass dm test from Fang Robotics... yay!!!!")

    def get_fang_robotics_guild(self):
        """
        WARNING: THIS IS SLIGHTLY UNSECURE
        THIS ASSUMES THE BOT IS ONLY 
        JOINING FANG ROBOTICS OR SOME OTHER
        SET OF SERVERS WHERE THE ONLY FANG ROBOTICS
        SERVER IS NAMED FANG ROBOTICS
        """
        for guild in self.guilds:
            if guild.name == "Fang Robotics" :
                return guild


    def initialize_fang_participants(self):
        fang_robotics_guild = self.get_fang_robotics_guild()

        for member in fang_robotics_guild.members:
            if(is_fang_participant(member)):
                self._fang_participants.append(member)


    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        await self._silly_dialogue.on_message(message)

