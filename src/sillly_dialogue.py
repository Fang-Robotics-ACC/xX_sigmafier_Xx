import discord

class SillyDialogue:
    async def on_message(self, message):

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
