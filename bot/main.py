import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!sr")

bot.add_cog(message_cog(bot))

bot.run(os.getenv("TOKEN"))
