import logging
from discord.ext import commands
from discord.ext.commands import has_permissions
logger = logging.getLogger(__name__)

from modules.config.config import Config

class Configuration(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.group()
	async def config(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('Invalid config command passed...')

	@config.command(pass_context=True)
	@has_permissions(administrator=True)
	async def channel(self, ctx):
		serverID = str(ctx.guild.id)
		channelID = str(ctx.channel.id)
		Config.cfgUpdate(serverID, "Bot Channel", channelID)
		await ctx.send("Bot channel successfully updated to here!")

	@config.command(pass_context=True)
	async def where(self, ctx):
		serverID = str(ctx.guild.id)
		try:
			result = Config.cfgRead(serverID, "Bot Channel")
			await ctx.send(Config.cfgRead(serverID, "Bot Channel"))
		except:
			await ctx.send("Error!")

	@config.command(pass_context=True)
	@has_permissions(administrator=True)
	async def welcome(self, ctx):
		try:
			if Config.cfgRead(str(ctx.guild.id), "welcomeChannel")==ctx.channel.id:
				Config.cfgUpdate(str(ctx.guild.id), "welcomeChannel", 0)
				Config.cfgUpdate(str(ctx.guild.id), "welcomeOn", False)
				await ctx.send("Disabled welcome messages in this channel!")
			elif Config.cfgRead(str(ctx.guild.id), "welcomeChannel")!=0:
				Config.cfgUpdate(str(ctx.guild.id), "welcomeChannel", ctx.channel.id)
				Config.cfgUpdate(str(ctx.guild.id), "welcomeOn", True)
				await ctx.send("Moved and enabled welcome messages to this channel!")
			else: #this is seperate just in case, i forgot why while coding
				Config.cfgUpdate(str(ctx.guild.id), "welcomeChannel", ctx.channel.id)
				Config.cfgUpdate(str(ctx.guild.id), "welcomeOn", True)
				await ctx.send("Enabled welcome messages in this channel!")
		except:
			await ctx.send("error! LOL!")

	@config.command(pass_context=True)
	@has_permissions(administrator=True)
	async def welcomemsg(self, ctx):
		msg = str(ctx.message.content)[(len(ctx.prefix) + len('config welcomemsg ')):]
		try:
			Config.cfgUpdate(str(ctx.guild.id), "welcomeMsg", msg)
			await ctx.send("Updated welcome message!")
		except:
			logger.exception("Error sending error message.")
			await ctx.send("Error!")
