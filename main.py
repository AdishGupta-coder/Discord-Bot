import discord
from discord.flags import Intents
import os
import random
from keep_alive import keep_alive

Intents = Intents.default()
Intents.message_content = True

client = discord.Client(intents=Intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

rps = ["r", "p", "s"]
spin = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
prime = ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29", "31", "37", "41", "43", "47", "53", "59", "61", "67", "71", "73", "79", "83", "89", "97"]


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "wittwin" in message.content.lower():
      await message.channel.send("Hello!")
    
    if "wittwin" and "spin" in message.content.lower():
      await message.channel.send("https://tenor.com/view/wheel-of-fortune-spin-the-price-is-right-gif-9848245")
      botspin = random.choice(spin)
      
      if botspin in prime:
        await message.channel.send("It is a prime number. Try to guess it!")
        guess = await client.wait_for('message', check=lambda m: m.author == message.author)

        if guess.content == botspin:
          await message.channel.send("You guessed it!")
        elif guess.content in spin and guess.content != botspin:
          await message.channel.send("You didn't guess it! It was " + str(botspin))

        else:
          await message.channel.send("Sorry, you entered an invalid number. Please type a number from 1 to 100 only next time. By the way it was " + str(botspin))

      else:
          hint = "even" if int(botspin) % 2 == 0 else "odd"
          await message.channel.send("Try to guess it! Hint: It is an " + hint + " number and not a prime number.")
          guess = await client.wait_for('message', check=lambda m: m.author == message.author)

          if guess.content == botspin:
            await message.channel.send("You guessed it!")
          elif guess.content in spin and guess.content != botspin:
            await message.channel.send("You didn't guess it! It was " + str(botspin))

          else:
            await message.channel.send("Sorry, you entered an invalid number. Please type a number from 1 to 100 only next time. By the way it was " + str(botspin))
          
      
    if "wittwin" and "rps" in message.content.lower():
      
      botchoice = random.choice(rps)
      
      if "rock" in message.content.lower():
        if botchoice == "r":
          await message.channel.send("It's a tie! I also chose rock.")
        elif botchoice == "p":
          await message.channel.send("You lost! I chose paper. Better luck next time!")
        elif botchoice == "s":
          await message.channel.send("Congratulations! You won! I chose scissors.")

      elif "paper" in message.content.lower():
        if botchoice == "p":
          await message.channel.send("It's a tie! I chose paper.")
        elif botchoice == "s":
          await message.channel.send("You lost! I chose scissors. Better luck next time!")
        elif botchoice == "r":
          await message.channel.send("Congratulations! You won! I chose rock.")

      elif "scissors" in message.content.lower():
        if botchoice == "s":
          await message.channel.send("It's a tie! I chose scissors.")
        elif botchoice == "r":
          await message.channel.send("You lost! I chose rock. Better luck next time!")
        elif botchoice == "p":
          await message.channel.send("Congratulations! You won! I chose paper.")

      else:
        await message.channel.send("Please type rock, papers, or scissors.")
        personchoice = await client.wait_for('message', check=lambda m: m.author == message.author)

        if "rock" in personchoice.content.lower():
          if botchoice == "r":
            await message.channel.send("It's a tie! I also chose rock.")
          elif botchoice == "p":
            await message.channel.send("You lost! I chose paper. Better luck next time!")
          elif botchoice == "s":
            await message.channel.send("Congratulations! You won! I chose scissors.")

        elif "paper" in personchoice.content.lower():
          if botchoice == "p":
            await message.channel.send("It's a tie! I chose paper.")
          elif botchoice == "s":
            await message.channel.send("You lost! I chose scissors. Better luck next time!")
          elif botchoice == "r":
            await message.channel.send("Congratulations! You won! I chose rock.")

        elif "scissors" in personchoice.content.lower():
          if botchoice == "s":
            await message.channel.send("It's a tie! I chose scissors.")
          elif botchoice == "r":
            await message.channel.send("You lost! I chose rock. Better luck next time!")
          elif botchoice == "p":
            await message.channel.send("Congratulations! You won! I chose paper.")

        else:
          await message.channel.send("Sorry, I did not understand what you chose. Try again next time.")
        

        
keep_alive()
client.run(os.environ['TOKEN'])
