import discord
import config 
import requests
from lyricsgenius import Genius

client = discord.Client()
token = config.token
genius_token = config.genius_token
genius_client = Genius(genius_token)

# Research point : await and async functions
# Idea for bot to handle multiple commands: Switch case


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def getSong(query):
    print("THIS WAS THE MESSAGE THAT WAS SENT\n")
    array = query.split() # Split the query into a list

    for word in array: 
        print(word)

def getSingleSong():
    artist = genius_client.search_artist("Andy Shauf", max_songs=3,sort="title")
    print(artist.songs)
            

# Handle messages
@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'): 
        sender = message.author.display_name # Get the display name of who sent the message
        await message.channel.send('Hello! ' + sender)

    elif message.content.startswith('!ping'):
        getSong(message.content)            # Get the actual message that was sent
        await message.channel.send('Pong!')
    
    elif message.content.startswith('!test'):
        getSingleSong()
        await message.channel.send('Sent test to terminal')

        
client.run(token)