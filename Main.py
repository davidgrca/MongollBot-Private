import discord
from discord.ext import commands, tasks
from itertools import cycle
import datetime

client = commands.Bot(command_prefix=".")
status = cycle(["Los Servidores de MongollLand", ".help"])
TOKEN = "ODMyMzc3Mzg0MTQxMDYyMTc0.YHi52Q.bh0Gql5l90fCTdRQ3YC_YD4DLYs"

# Startup
@client.event
async def on_ready():
    change_status.start()
    print("Bot ready!")

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(next(status))))

# Capcha

# Public
# info
@client.command()
async def info(ctx):
    embed = discord.Embed(title=f"**{ctx.guild.name}**", description=f"**Miembros:** {ctx.guild.member_count}"
                                                                     f"\n**Veteranos:** 13\n**Staff:** 2\n",
                          timestamp=datetime.datetime.utcnow(), color=discord.Colour.green())
    embed.set_footer(text=".help para todos los comandos")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/762689124855447572/6766e912c05dbc60db79e8437727edd5.webp?size=128")
    await ctx.send(embed=embed)

# help
# ppt
# sugerencia
# random
# repetidor



# Mod
# tell
# sorteo
# warn
# ban, unban
# kick, unkick
# mute, unmute
# poll
# dm
# clear


# Music
# BackUp


client.run(TOKEN)
