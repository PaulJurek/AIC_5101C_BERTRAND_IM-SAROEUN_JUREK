import os
from dotenv import load_dotenv
load_dotenv()

# Initialiser le modèle
from transformers import pipeline
classifier = pipeline("text-classification", model="Ju1es/discord_classification2")

# Initialiser le bot
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

# Commande simple : !bonjour
@bot.command(name="bonjour")
async def bonjour(ctx):
    await ctx.send("Hello World !")

message_count = {}
message_log = {}

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if not message.content.strip():
        return
    
    channel_name = message.channel.name

    if channel_name not in message_count:
        message_count[channel_name] = 0
        message_log[channel_name] = []

    message_log[channel_name].append(message.content)
    message_count[channel_name] += 1

    if message_count[channel_name] == 10:
        control = []
        for msg in message_log[channel_name]:
            result = classifier(msg)
            print(f"Message : {msg} -> Classification : {result[0]['label']} ({result[0]['score']:.2f})")
            if result[0]['score'] > 0.6:
                control.append(result[0]['label'])
        
        message_count[channel_name] = 0
        message_log[channel_name] = []
        print(control)

        element_le_plus_present = max(set(control), key=control.count)
        if not element_le_plus_present == channel_name:
            await message.channel.send(f"You're off-topic. Please go to channel {element_le_plus_present}")
    
    return

# Lancer le bot
bot.run(os.getenv("DISCORD_TOKEN"))
