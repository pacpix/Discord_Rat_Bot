"""
Justin Stachofsky
Emoji_React.py
Created: 4/30/2018
Last Edit: 4/30/2018

Rat emoji reacts every post in the server.  Also responds to some commands. 
Written poorly on purpose I swear.
"""

import discord
import asyncio
import random

# Stores token information
import config

botToken = config.botToken

client = discord.Client()

r = random.SystemRandom()

@client.event
@asyncio.coroutine
def on_message(message):
    yield from client.add_reaction(message, "\U0001F400")
    if message.author == client.user:
        return
    if message.content.startswith('!everyone'):
        msg = '@everyone lmao'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!memecity'):
        msg = 'ok so i get that its a big ironic meme that died months ago but i actually dont dislike despacito as a song and its really been bugging me so if someone could fill me in on what all the hype is about that would be great like is something about it especially irritating or silly to everyone because in my opinion the worst thing about it is that its been way overplayed which isnt an anomaly when it comes to mainstream pop as im sure you all know for example something like tik tok by k$sha which was played all the time and still is sometimes like when i had a really bad experience at a subway a few years back a song like that kinda enrages me with obnoxious beats and insipid lyrics while i just dont have that same base reaction of disappointed disgust towards the soulless corruption of art that is the capitalist music industry god where did we go wrong i hope kim pushes the button anyway when i hear a despacito clip in passing like on my twitter im generally okay with it and i think the melody and vocal performances seem fine though i must admit i am far from a musical expert and basically have no interest in seeking it out for personal listening so what do you guys really think is it just an okay song that has been beaten to death by shitty radio stations catering to a lazy audience or is my taste objectively shit join the rat zone'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!fascists'):
        msg = 'Fuck the fascists'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!takerate'):
        rate = 'Q' + str(r.randint(1,4)) + ' Take'
        msg = rate.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!takematrix'):
        msg = 'Q1 = Hot and Right, Q2 = Hot and Wrong, Q3 = Cold and Wrong, Q4 = Cold and Right'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!thisi'):
        msg = 'This but, ironically'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!thisu'):
        msg = 'This but, unironically'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!child'):
        msg = 'Did a child write this?'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!model'):
        msg = "What's your model?".format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!failure'):
        msg = '{0.author.mention} is a market failure'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!balls'):
        msg = 'Do it no balls'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!trailer'):
        msg = 'https://www.youtube.com/watch?v=GDuOSJeZfTY'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!rat'):
        msg = '\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400\U0001F400'.format(message)
        yield from client.send_message(message.channel, msg)
    elif 'bitcoin' in message.content:
        msg = '>bitcoin. lmao nice meme'.format(message)
        yield from client.send_message(message.channel, msg)
    elif 'stupid' in message.content:
        msg = discord.Embed()
        msg.set_image(url="https://i.imgur.com/LFIi7yS.jpg")
        yield from client.send_message(message.channel, embed=msg)
    elif message.content.startswith('!god'):
        msg = discord.Embed()
        msg.set_image(url="https://i.imgur.com/pZi485H.jpg")
        yield from client.send_message(message.channel, embed=msg)
    elif message.content.startswith('!GOD'):
        msg = discord.Embed()
        msg.set_image(url="https://i.imgur.com/VKqSxBH.jpg")
        yield from client.send_message(message.channel, embed=msg)
    elif message.content.startswith('!dumbdumb'):
        msg = 'lol ur big dumb'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!specifictakerate'):
        msg = '(' + str(r.randint(0,999999999)) + ', ' + str(r.randint(0,999999999)) + ') Use !takerate for a more general take'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!census'):
        msg = 'https://www2.census.gov/library/publications/decennial/1860/population/1860a-31.pdf'
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!iconic'):
        msg = discord.Embed()
        msg.set_image(url="https://i.imgur.com/k7FjY1m.jpg")
        yield from client.send_message(message.channel, embed=msg)

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(botToken)

