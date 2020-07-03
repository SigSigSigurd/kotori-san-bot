import os
from dotenv import load_dotenv

from modules.core.client import Client
from modules.core.command import Command
from modules.core.events import Events
#from modules.esportsclub import EsportsClub # for commands / features for UW-Madison Esports Club
#currently SMTP doesn't work

bot = Client.bot

class MainEsports:

	os.chdir(os.path.dirname(os.path.abspath(__file__))) #changes cwd to project root

	load_dotenv()
	TOKEN = os.getenv("ESPORTS_TOKEN")

	bot.run(TOKEN) #runs the Discord bot using one of the above tokens
