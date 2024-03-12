import discord
from discord.flags import Intents
import os
import random

Intents = Intents.default()
Intents.message_content = True

client = discord.Client(intents=Intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

rps = ["r", "p", "s"]


@client.event
async def on_message(message):
    if message == client.user:
        return

    if  message.content.startswith("hi wittwin"):
      await message.channel.send("Hello!")

    if "wittwin" and "play" in message.content.lower():
      
      botchoice = random.choice(rps)
      
      if "rock" in message.content.lower():
        if botchoice == "r":
          await message.channel.send("It's a tie!")
        elif botchoice == "p":
          await message.channel.send("You lost! Better luck next time!")
        elif botchoice == "s":
          await message.channel.send("Congratulations! You won!")

      elif "paper" in message.content.lower():
        if botchoice == "p":
          await message.channel.send("It's a tie!")
        elif botchoice == "s":
          await message.channel.send("You lost! Better luck next time!")
        elif botchoice == "r":
          await message.channel.send("Congratulations! You won!")

      elif "scissor" in message.content.lower():
        if botchoice == "s":
          await message.channel.send("It's a tie!")
        elif botchoice == "r":
          await message.channel.send("You lost! Better luck next time!")
        elif botchoice == "p":
          await message.channel.send("Congratulations! You won!")
        
        

client.run(os.environ['TOKEN'])
