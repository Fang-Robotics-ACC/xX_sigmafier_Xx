import discord
def is_fang_participant(member : discord.Member):
    """
    If someone is being active in fang robotics, they'll have this role
    """
    for role in member.roles:
        if (role.name == "Onboarding" or role.name == "Member") and not (role.name == "Faculty Advisor"):
            return True
    return False


