import discord
from discord.ext import commands, tasks
import asyncio
import sqlite3
import json
import os
from os import path

from .client import Client
from .config import Config
from .safebooru import Safebooru
from .user import User

bot = Client.bot
status = discord.Game("on Wired") #sets the game the bot is currently playing
esportsStatus = discord.Game("Fortnite with Bucky")

class Events:

	@bot.event
	async def on_ready(): #bot startup event

		if bot.user.id == 727537208235524178:
			print('Esports Club is ready to go!')
			bot.command_prefix = "b!"
			await bot.change_presence(status=discord.Status.online, activity=esportsStatus)
		else:
			print('Lain is online')
			await bot.change_presence(status=discord.Status.online, activity=status)

		for guild in bot.guilds:
			serverID = str(guild.id)
			serverName = str(guild.name)
			if path.exists(os.getcwd()+"/config/"+serverID+".json"):
				Config.cfgUpdate(serverID, "Name", serverName)
			else:
				with open(os.getcwd()+"/config/"+serverID+".json", "x") as server_json:
					json_data = {"Name": serverName}
					json.dump(json_data, server_json)

		for user in bot.users:
			userID = str(user.id)
			userName = str(user.name)
			if path.exists(os.getcwd()+"/user/"+userID+".json"):
				User.userUpdate(userID, "Name", userName)
			else:
				with open(os.getcwd()+"/user/"+userID+".json", "x") as user_json:
					json_data = {"Name": userName}
					json.dump(json_data, user_json)



	@bot.event
	async def on_member_join(member):
		if str(member) == 'UWMadisonRecWell#3245':
			for guild in bot.guilds:
				if str(guild.id) == '554770485079179264':
					role = discord.utils.get(guild.roles, name='RecWell')
					await discord.Member.add_roles(member, role)
					break
