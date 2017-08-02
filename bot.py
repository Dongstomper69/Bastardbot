import discord
import requests
import json
import random
from xml.etree import ElementTree as ET
from discord.ext.commands import Bot
my_bot = Bot(command_prefix="!")
@my_bot.event
async def on_read():
    print("Client logged in")
@my_bot.command()
async def hello(*args):
    return await my_bot.say("Fuck You Bastard")
@my_bot.command()
async def prolife(*args):
    return await my_bot.say("http://i.imgur.com/dnnugfI.jpg")
@my_bot.command()
async def e6(*, tags: str):
    print(tags)
    #Replaces spaces with %20, to be compatible with e621's formatting
    tags.replace(" ", "%20")
    #Generates a random number and uses that to determine the post pulled
    seed = random.randint(1, 1200000)
    #gets a random post based on the number specified and the tags inputted
    search = requests.get("https://e621.net/post/index.json?limit=1&before_id=" + str(seed) + "&tags=" + tags)
    #Converts the GET requests to JSON
    postid = search.json()
    print(search.content)
    #gets the ID from the request
    parameter = {"id": postid[0]['id']}
    #i dont actually have to do this i can just get the image url directly from postid but im too lazy to change it
    porn = requests.get("https://e621.net/post/show.json", params=parameter)
    post = porn.json()
    #posts the file url
    return await my_bot.say(post['file_url'])
    print(seed.text)
    print(porn.status_code)
my_bot.run("MzQxMTMzNDQ0MDM1OTAzNDg4.DF8phg.d_aLBWk9H1b_dkSJavAI40tFWiw")