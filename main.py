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

 
# on ready ung ready prompt
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def split(query): # Split the query into strings
    print("THIS WAS THE MESSAGE THAT WAS SENT\n")
    array = query.split() # Split the query into a list

    return array

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

    elif message.content.startswith('!bitch'):
        await message.channel.send('Lasagna')
    
    elif message.content.startswith('!test'):
        getSingleSong()
        await message.channel.send('Sent test to terminal')
    
    elif message.content.startswith('!lyrics'):
        song_name = split(message.content)
        song = genius_client.search_song(song_name[1])
        await message.channel.send(song.lyrics)
        
client.run(token)