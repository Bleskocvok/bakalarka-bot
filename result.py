#!/usr/bin/env python3

import dotenv
import discord
import os
from discord.ext import commands
from bakalarka import BakalarkaCog



# load discord token
dotenv.load_dotenv()
token = os.getenv('DISCORD_TOKEN')


client = commands.Bot(command_prefix='!')
client.add_cog(BakalarkaCog(client))
client.run(token)


