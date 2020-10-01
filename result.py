#!/usr/bin/env python3

import os
import discord
import dotenv
import random
import asyncio
from discord.ext import commands


lock = asyncio.Lock()


# load discord token
dotenv.load_dotenv()
token = os.getenv('DISCORD_TOKEN')


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('{} (command BOT) connected'.format(client.user.name), flush=True)


@client.command(name='mirek', help='Takes a number and makes the thing')
async def mirek(ctx, size: int=20):
    async with lock:
        if size < 4:
            await ctx.send('```too low```')
            return
        if size > 150:
            await ctx.send('```too high```')
            return
        os.system('./generate.sh {}'.format(size))
        files = os.listdir('graphs')
        if len(files) == 0:
            await ctx.send('something broke')
            return
        selected = random.choice(files)
        # drag has a bug, reeeeeee
        # (target 'cycl' doesn't compile)
        # os.system('./cycl -i graphs/')
        os.system('./draw {} out.svg'.format('graphs/' + selected))
        # uses imagemagik
        os.system('convert out.svg out.png')
        await ctx.send(file=discord.File('out.png'))


@client.command(name='graph', help='Graaaph!')
async def graph(ctx, params : str):
    with open('tmp.gv', 'w') as f:
        f.write(params)
    os.system('./draw {} out.svg'.format('tmp.gv'))
    # uses imagemagik
    os.system('convert out.svg out.png')
    await ctx.send(file=discord.File('out.png'))


@client.event
async def on_command_error(ctx, error):
    pass


client.run(token)


