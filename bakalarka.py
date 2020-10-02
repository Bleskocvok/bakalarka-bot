
import os
import discord
import random
import asyncio
from discord.ext import commands


class BakalarkaCog(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.lock = asyncio.Lock()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot \'{}\' loaded cog \'{}\''.format(self.bot.user.name, 'BakalarkaCog'), flush=True)

    @commands.command(help='Takes a number and makes the thing')
    async def mirek(self, ctx, size: int=20):
        async with self.lock:
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

    @commands.command(help='Graaaph!')
    async def graph(self, ctx, params : str):
        with open('tmp.gv', 'w') as f:
            f.write(params)
        os.system('./draw {} out.svg'.format('tmp.gv'))
        # uses imagemagik
        os.system('convert out.svg out.png')
        await ctx.send(file=discord.File('out.png'))

    @commands.Cog.listener()
    async def on_message(self, msg):
        text = msg.content
        if 'digraph' not in text:
            return
        if '{' not in text:
            return
        if '}' not in text:
            return
        ctx = await self.bot.get_context(msg)
        await self.graph(ctx, text)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print('ERROR: {}'.format(str(error)))




