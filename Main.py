import discord
from discord.ext import commands
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user}')

@bot.command
async def temp(ctx):
  etemp = #Температура Земли
  await ctx.send('Температура земли: ', etemp)

@bot.command
async def reas(ctx):
  await ctx.send('1.')
  time.wait(1)
  await ctx.send('2.')
  time.wait(1)
  await ctx.send('3.')
  time.wait(1)
  await ctx.send('4.')
  time.wait(1)
