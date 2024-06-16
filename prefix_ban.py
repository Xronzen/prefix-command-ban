import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print("I'm ready!")

#!ban <user name> <reason>
@bot.command()
async def ban(ctx, member:discord.Member, *args, reason="None"):
  await member.ban(reason=reason)

#My mail, write !xronzen
@bot.command()
async def xronzen(ctx):
  await ctx.send("```yaml\nxronzen@proton.me\n```")


#Paste your own token where it writing "YOUR TOKEN"
bot.run("YOUR TOKEN")
