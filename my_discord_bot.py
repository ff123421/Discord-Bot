# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
# 👍
import discord
import sys
import os
import time
import random
from discord.ext import commands
from discord.utils import get
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()
bot = Bot(command_prefix='$')
bot.prefix = "$"
# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
 # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
 guild_count = 0
 # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
 for guild in bot.guilds:
  # PRINT THE SERVER'S ID AND NAME.
  print("- {guild.id} (name: {guild.name})")
  # INCREMENTS THE GUILD COUNTER.
  guild_count = guild_count + 1
  # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
  print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
print("bot is online")
@bot.event
async def on_message(message):
 # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
 if message.content == bot.prefix + "verify":
  await message.delete()
  embedVar = discord.Embed(title = "Verify Me? :", description="React to this with 👍 x2 times to become verified." + " Verifications are open from 8:00am - 3:00pm UTC-8", color=0x00ff00)
  embedVar.set_author(name=message.author.display_name, url="https://github.com/BV0205", icon_url=message.author.avatar_url)
  await message.channel.send(embed=embedVar)
  message_id_1 = message.id
  @bot.event
  async def on_reaction_add(reaction, user):
      Channel = bot.get_channel("some#'s")
      member = user
      if reaction.emoji == "👍":  
       @bot.event
       async def on_raw_reaction_add(payload):
           message_id = payload.message_id
           if message_id_1 == message_id_1:
               print("5")
               time.sleep(1)
               print("4")
               time.sleep(1)
               print("3")
               time.sleep(1)
               print("2")
               time.sleep(1)
               print("1")
               time.sleep(1)
               print("0")
               user_id = member
               msg_id = payload.message_id
               guild_id = payload.guild_id
               server = bot.get_guild(guild_id)
               role = discord.utils.get(server.roles, id=int("some#'s"))
               member10 = server.get_member(user_id)
               print(member)
               await member.add_roles(role)
               print("role added")
 if message.content == bot.prefix + "spin-wheel":
  await message.delete()
  print(message.author)
  user = message.author
  n = random.randint(9, 9)
  print(n)
  if n == 9:
   reward = "1 Great White Shark Card!"     
  print("spinning")
  embedVar = discord.Embed(title = "Spinning", color=0x00ff00)
  z = await message.channel.send(embed=embedVar)
  for i in range(1, 5):
   embedVar = discord.Embed(title = "Spinning.", color=0x00ff00)
   await z.edit(embed=embedVar)
   time.sleep(int(1))
   embedVar = discord.Embed(title = "Spinning..", color=0x00ff00)
   await z.edit(embed=embedVar)
   time.sleep(int(1))
   embedVar = discord.Embed(title = "Spinning...", color=0x00ff00)
   await z.edit(embed=embedVar)
   time.sleep(int(1))
   embedVar = discord.Embed(title = "Spinning", color=0x00ff00)
   await z.edit(embed=embedVar)
   time.sleep(int(1))
  await z.delete()
  embedVar = discord.Embed(title = f"{user} has won {reward}", color=0x00ff00)
  z = await message.channel.send(embed=embedVar)
  ## 1 hour time.sleep(3600)  
bot.run(token)
