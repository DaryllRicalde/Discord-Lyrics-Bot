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

def getSong(song_name):     # Return the Song object
    full_song_name = ""

    for i in range(1, len(song_name)):
        full_song_name += song_name[i] + " "

    songObj = genius_client.search_song(full_song_name)

    return songObj

def getArtist(artist_name):     # Return the Artist object
    full_artist_name = ""

    for i in range(1, len(artist_name)):
        full_artist_name += artist_name[i] + " "

    artistObj = genius_client.search_artist(full_artist_name)

    return artistObj

# Handle messages
@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'): 
        sender = message.author.display_name # Get the display name of who sent the message
        await message.channel.send('Hello! ' + sender)

    elif message.content.startswith('!ping'):
        await message.channel.send('Pong!')

    elif message.content.startswith('!bitch'):
        await message.channel.send('Lasagna')

    elif message.content.startswith('!lyrics'):

        song_name = split(message.content)
        songObject = getSong(song_name)
        
        if(len(songObject.lyrics) >= 2000):
            await message.channel.send("Oops! That lyrics of this song exceeds Discord's character limit :( Here's the link to the song lyrics courtesy of Genius " + songObject.url)

        await message.channel.send(songObject.lyrics)

    elif message.content.startswith('!artist'):     # Return top 5 songs of this artist

        artist_name = split(message.content)
        artist_object = getArtist(artist_name)
        top_songs = artist_object.songs                    #Returns a list

        for i in range (1,5):
            await message.channel.send(top_songs[i])
        
client.run(token)