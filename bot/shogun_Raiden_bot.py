import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    print(f'¡{member} entro en Inazuma! ')


@client.command()
async def ping(ctx):
    print('We have logged in as {0.user}'.format(client))
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['SR kill'])
async def kill(ctx, message):
    responses = [
        "https://tenor.com/view/raiden-shogun-genshin-impact-gif-23667613"]
    await ctx.send(f'Kill {message} {random.choice(responses)}')


client.run('OTEzOTQxODc1NjYzMTk2MjAw.G5HxeF.So16ZqLIHj-n1_cCCb5Zi3guMd-RJDLuXuF_DM')
