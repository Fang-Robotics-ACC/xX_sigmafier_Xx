import discord
from member_filters import is_fang_participant
from sillly_dialogue import SillyDialogue

class Sigmafier(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fang_participants = []
        self._silly_dialogue = SillyDialogue()
        self._commit_list = {}
        self._announcement_channel = None

    async def blast_all_participants(self, message_content):
        no_response_list = []
        for participant in self._fang_participants:
            try:
                await participant.send(message_content)
            except:
                no_response_list.append(participant)
                print(participant.name + " did not recieve message!!!")

    async def _solicict_commit_message(self):
        solicitation = "Hello! Please reply your weekly goal you will commit to! Your most recent reponse will be viewed as the commit!"
        await self.blast_all_participants(solicitation)

    async def on_ready(self):
        self.initialize_fang_participants()
        self._announcement_channel = discord.utils.get(self.get_fang_robotics_guild().text_channels, name="team-announcements")
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

    async def _announce_commits(self):
        channel = self._announcement_channel
        commit_announcement = "Weekly Commits\n"
        for participant, commit in self._commit_list.items():
            name = participant.name
            commit_announcement += f"{name}'s commit is: {commit}\n"
        await channel.send(commit_announcement)

        non_commit_participants = set(self._fang_participants) - set(self._commit_list.keys())

        lackers = "**Lacking Commits**\n"
        for participant in  non_commit_participants:
            id = participant.id
            lackers += f"<@{id}> has no commits\n"

        await channel.send(lackers)


    def initialize_fang_participants(self):
        fang_robotics_guild = self.get_fang_robotics_guild()

        for member in fang_robotics_guild.members:
            if(is_fang_participant(member)):
                self._fang_participants.append(member)


    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.channel.type == discord.ChannelType.private:
            self._commit_list[message.author] = message.content
        else:
            await self._silly_dialogue.on_message(message)

            if message.content == "!Announce":
                await self._announce_commits()
            elif message.content == "!Solicit Commits":
                await self._solicict_commit_message()
