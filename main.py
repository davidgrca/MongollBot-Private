import asyncio
import random
import discord
import datetime
from discord.ext import commands, tasks
from itertools import cycle
from keep_alive import keep_alive
import os

client = commands.Bot(command_prefix=".")
status = cycle(["Los Servidores de MongollLand", ".help"])

client.remove_command("help")
foot = "\".help\" para todos los comandos"
no_staff = ":x: No dispones del rol de staff!"
staff = 762690679984881686
admin = 762690677153857556
muted = 762731134147756032
integrante = 762690683755823104
wellcome_chn = 762690706753191986
captcha_chn = 765645737941663775
commands_chn = 762690703167062027


# Startup
@client.event
async def on_ready():
    change_status.start()
    print("Bot ready!")


@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=(next(status))))


# Captcha
@client.command()
@commands.has_role(staff)
async def captcha(
    ctx,
    member: discord.Member,
):
    wellcome_channel = client.get_channel(wellcome_chn)
    intg = discord.utils.get(ctx.guild.roles, id=integrante)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="𝘽𝙄𝙀𝙉𝙑𝙀𝙉𝙄𝘿𝙊!!!",
                          description=f"{member.mention}\n",
                          color=discord.Colour.random(),
                          timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(
        url="https://cdn.iconscout.com/icon/free/png-512/confetti-87-729044.png"
    )
    embed.set_footer(text="Pásatelo bien || Escribe “.help” para más ayuda")
    embed.add_field(name=" ‎",
                    value=f"**Ya somos {ctx.guild.member_count} miembros.**",
                    inline=False)
    embed.set_image(
        url=
        "https://images-ext-2.discordapp.net/external/Xnylclguuy26QeP8LKBBXsezkxijoFezCG5KQs6hXiY/https/media.discordapp.net/attachments/583842696247115854/583843194119389204/Tw.gif"
    )
    await wellcome_channel.send(embed=embed)
    await member.add_roles(intg)


@captcha.error
async def captcha_error(ctx, error):
    await ctx.channel.purge(limit=1)
    await ctx.send(no_staff + " " + ctx.author.mention)


# EasterEggs
# joya
@client.command()
async def joya(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        description=member.mention + "** está joya**",
        color=discord.Colour.random(),
    )
    embed.set_image(
        url=
        "https://i.pinimg.com/originals/31/6b/3c/316b3cd3d0c2522a3c9580cc74ba6ea7.jpg"
    )
    embed.set_footer(text=foot)
    await ctx.send(embed=embed)


@joya.error
async def joya_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            f"Necesitas introducir el usuario que está joya {ctx.author.mention}"
        )


# Public
# info
@client.command()
async def info(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f"**{ctx.guild.name}**",
                          description=f"**Miembros:** {ctx.guild.member_count}"
                          f"\n**Veteranos:** 13\n**Servidor creado el: "
                          f"\n**{ctx.guild.created_at}\n",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Colour.green())
    embed.set_footer(text=foot)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


# invit
@client.command()
async def invit(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f"**Invitación para {ctx.guild.name}**",
                          description="\nhttps://discord.gg/UcW5cc37Ad",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Colour.dark_green())
    embed.set_footer(text=foot)
    embed.set_image(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


# random
@client.command()
async def random10(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="**Número al azar del 0 al 10**",
                          description=f"__El bot ha elegido:__"
                          f"\n`{random.randint(0, 11)}`",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Colour.blurple())
    embed.set_thumbnail(url="https://pngimg.com/uploads/dice/dice_PNG49.png")
    embed.set_footer(text=foot)
    await ctx.send(embed=embed)


@client.command()
async def random100(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="**Número al azar del 0 al 100**",
                          description=f"__El bot ha elegido:__"
                          f"\n`{random.randint(0, 101)}`",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Colour.blurple())
    embed.set_thumbnail(url="https://pngimg.com/uploads/dice/dice_PNG49.png")
    embed.set_footer(text=foot)
    await ctx.send(embed=embed)


# help
@client.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="**###𝐇𝐄𝐋𝐏###**",
        description=
        "**Comandos**\n.invit (Invitación para el servidor)\n.help (Todos los comandos en el servidor)"
        "\n.info (Información del servidor)\n.ppt (Piedra, Papel, Tijeras)"
        "\n.random10 (Número al azar del 0 al 10)\n.random100 (Número al azar del 0 al 100)"
        "\n.repe (El bot repite lo que escribas)\n.didyouknow (Did You Know?)",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Colour.dark_blue())
    embed.add_field(
        name="**Staff**",
        value=
        ".mute (Mutea a la persona con un motivo)\n.unmute (Desmutea a la persona)"
        "\n.tempmute (Persona a la que muteas, por cuánto tiempo y motivo [Mutea temporalmente])"
        "\n.tell (El bot escribe en un embed tu mensaje)\n"
        ".poll (Crea una encuesta)\n.sorteo (Crea un sorteo)\n"
        ".warn (Añade un aviso al usuario mencionado)"
        "\n.ban (Banea al usuario mencionado)"
        "\n.kick (Kickea al usuario mencionado)\n.captcha (menciona a la persona para registrarlos en el server)",
        inline=True)
    embed.add_field(name="**Música**",
                    value="-p (canción)\n-next\n-loop\n-join\n-leave\n-stop",
                    inline=True)
    embed.add_field(
        name="**Normas**",
        value=
        "->Respeta al staff\n->Nada de spam\n->Prohibida toda la  pedofilia\n->Intentad ser lo menos racista posible",
        inline=False)
    embed.add_field(
        name="**Info extra**",
        value=">Si queréis roles personalizados o canales hablad con Tupei\n"
        ">Hay emojis y gifs personalizados. Disfrutadlos!!!\n>Hay comandos secretos escondidos en el bot!\n"
        ">Si no sabéis como invitar a alguien, utilizad este link:\n"
        "https://discord.gg/UcW5cc37Ad",
        inline=True)
    embed.add_field(name="**Página Web**", value="Próximamente", inline=True)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.set_footer(text="Creado por Tupei con amor")
    await ctx.send(embed=embed)


# ppt
@client.command()
async def ppt(ctx, *, args):
    await ctx.channel.purge(limit=1)
    var = ["`Piedra`", "`Papel`", "`Tijeras`"]
    embed = discord.Embed(title="**Piedra, Papel, Tijeras**",
                          description="El bot ha elegido: " +
                          random.choice(var) + "\nTú has elegido: " + "`" +
                          args + "`",
                          color=discord.Colour.blurple(),
                          timestamp=datetime.datetime.utcnow())
    embed.set_author(
        name=f"{ctx.author.name}"
    )
    embed.set_thumbnail(
        url=
        "https://e7.pngegg.com/pngimages/243/115/png-clipart-rock-paper-scissors-scissors-stone.png"
    )
    embed.set_footer(text=foot)
    await ctx.send(embed=embed)


@ppt.error
async def ppt_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: Necesitas introducir un objeto con el que jugar")


# repetidor
@client.command()
async def repe(ctx, *, args):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{ctx.author.mention}: " + args)


@repe.error
async def repe_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: Necesitas introducir un mensaje")


# did you know?
@client.command()
async def didyouknow(ctx):
	await ctx.channel.purge(limit=1)
	embed = discord.Embed(
		title="Did You Know?",
		description="Discord added a cool new way to use bot commands!\n一款默认表情符号。您可以在 Discord 的任意地方使用它",
		timestamp=datetime.datetime.utcnow(),
		color=discord.Colour.light_grey()
	)
	embed.set_footer(text=foot)
	await ctx.send(embed=embed)


# Mod
# tell
@client.command()
@commands.has_role(admin)
async def tell(ctx, *, args):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(description=args, color=discord.Colour.orange())
    embed.set_author(
        name=f"{ctx.author.name}"
    )
    await ctx.send(embed=embed)


@tell.error
async def tell_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: Necesitas introducir un mensaje")
    if isinstance(error, commands.MissingRole):
        await ctx.send("No dispones de admin " + ctx.author.mention)


# sorteo
@client.command()
@commands.has_role(staff)
async def sorteo(ctx, mins: float, *, prize: str):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="🎉 **SORTEO** 🎉",
                          description=f"**{prize}**",
                          color=discord.Colour.purple(),
                          timestamp=datetime.datetime.utcnow())
    embed.set_image(
        url=
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToPgbGnZW0B7W0ESr4OVaV9BflcYwxrOR0fUG2uimETtJc9LB3ZWuVEalVRiDl7ri1bHs&usqp=CAU"
    )
    embed.set_footer(text=f"Este sorteo termina en {mins} minutos!")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🎊")
    await asyncio.sleep(mins * 60)
    new = await ctx.channel.fetch_message(msg.id)
    users = await new.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)
    await ctx.send(f"**Felicidades {winner.mention}, has ganado** `{prize}`")


@sorteo.error
async def sorteo_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRole):
        await ctx.send(no_staff + " " + ctx.author.mention)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            ":x: Necesitas introducir un premio para hacer un sorteo")


# warn
@client.command()
@commands.has_role(staff)
async def warn(ctx, member: discord.Member, *, args):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="**Warning!** ⚠",
                          description=f"{member.mention} " + args,
                          color=discord.Colour.gold())
    embed.set_footer(text=f"Avisado por {ctx.author.name}")
    await ctx.send(embed=embed)


@warn.error
async def warn_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            ":x: Necesitas mencionar a una persona y poner un motivo para utilizar este comando"
        )
    if isinstance(error, commands.MissingRole):
        await ctx.send(no_staff + " " + ctx.author.mention)


# ban
@client.command()
@commands.has_role(admin)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    embed = discord.Embed(
        title="**BAN**❗",
        description=
        f"**Usuario: ** {member.mention}\n**Motivo: **{reason}\n**Autor del Ban: **{ctx.author.mention}",
        color=discord.Colour.dark_red(),
        timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(
        url=
        "https://static.wixstatic.com/media/2cd43b_9e166912409648999d8d19579e477321~mv2_d_2784_2910_s_4_2.png/v1/fill/w_640,h_670,fp_0.50_0.50,q_95/2cd43b_9e166912409648999d8d19579e477321~mv2_d_2784_2910_s_4_2.png"
    )
    await ctx.send(embed=embed)


@ban.error
async def ban_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            ":x: Necesitas mencionar a una persona y poner un motivo para utilizar este comando"
        )
    if isinstance(error, commands.MissingRole):
        await ctx.send("No dispones de admin " + ctx.author.mention)


# kick
@client.command()
@commands.has_role(admin)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    embed = discord.Embed(
        title="**KICK**❗",
        description=
        f"**Usuario: ** {member.mention}\n**Motivo: **{reason}\n**Autor del Kick: **{ctx.author.mention}",
        color=discord.Colour.gold(),
        timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(
        url=
        "https://cdn2.iconfinder.com/data/icons/fighter-fighting-attacking-poses/263/fight-007-512.png"
    )
    await ctx.send(embed=embed)


@kick.error
async def kick_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            ":x: Necesitas mencionar a una persona y poner un motivo para utilizar este comando"
        )
    if isinstance(error, commands.MissingRole):
        await ctx.send("No dispones de admin " + ctx.author.mention)


# mute, unmute
@client.command()
@commands.has_role(staff)
async def mute(ctx, member: discord.Member, *, reason):
    mutedrole = discord.utils.get(ctx.guild.roles, id=muted)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="**Mute! **🤫",
        description=f"{member.mention} fue muteado por `{reason}`",
        color=discord.Colour.purple(),
        timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f"Muteado por {ctx.author.name}")
    embed.set_image(
        url=
        "https://cdn130.picsart.com/341369715030211.png?to=crop&type=webp&r=310x310&q=75"
    )
    await ctx.send(embed=embed)
    await member.add_roles(mutedrole, reason=reason)


@mute.error
async def mute_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            ":x: Necesitas poner un miembro y motivo para mutear a un miembro")
    if isinstance(error, commands.MissingRole):
        await ctx.send(no_staff + " " + ctx.author.mention)


@client.command()
@commands.has_role(staff)
async def unmute(ctx, member: discord.Member):
    mutedrole = discord.utils.get(ctx.guild.roles, id=muted)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="**Unmute! **🗣️",
                          description=f"{member.mention} fue desmuteado",
                          color=discord.Colour.purple(),
                          timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f"Desuteado por {ctx.author.name}")
    await ctx.send(embed=embed)
    await member.remove_roles(mutedrole)


@unmute.error
async def unmute_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRole):
        await ctx.send(no_staff + " " + ctx.author.mention)


# tempmute
@client.command()
@commands.has_role(staff)
async def tempmute(ctx, member: discord.Member, mins: float, *, reason):
    mutedrole = discord.utils.get(ctx.guild.roles, id=muted)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="**Mute! **🤫",
        description=f"{member.mention} fue muteado por `{reason}`",
        color=discord.Colour.purple(),
        timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f"Muteado por {ctx.author.name} {mins} minutos")
    embed.set_image(
        url=
        "https://cdn130.picsart.com/341369715030211.png?to=crop&type=webp&r=310x310&q=75"
    )
    await ctx.send(embed=embed)
    await member.add_roles(mutedrole, reason=reason)
    await asyncio.sleep(mins * 60)
    await member.remove_roles(mutedrole)
    embed = discord.Embed(title="**Unmute! **🗣️",
                          description=f"{member.mention} fue desmuteado",
                          color=discord.Colour.purple(),
                          timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)


@tempmute.error
async def tempmute_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRole):
        await ctx.send(no_staff + " " + ctx.author.mention)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            ":x: Necesitas poner un miembro, duración y motivo para mutear a un miembro"
        )


# poll
@client.command()
@commands.has_role(staff)
async def poll(ctx, *, args):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(description=f"📊 **{args}**",
                          color=discord.Colour.dark_green())
    embed.set_author(name=ctx.author.name)
    embed.set_thumbnail(
        url=
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdb4GpqUeA6faSLS0jv-XBEDE162j4DEGbV7ev-8E0La2p1lE&s"
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❎")


@poll.error
async def poll_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: Necesitas introducir un mensaje")
    if isinstance(error, commands.MissingRole):
        await ctx.send(no_staff + " " + ctx.author.mention)


# dm
@client.command()
@commands.has_role(admin)
async def dm(ctx, member: discord.Member, *, args):
    await ctx.channel.purge(limit=1)
    channel = await member.create_dm()
    await channel.send(args)


@dm.error
async def dm_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRole):
        await ctx.send("No dispones de admin " + ctx.author.mention)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            ":x: Necesitas especificar un usuario y mensaje para utilizar este comando"
        )


# clear
@client.command()
@commands.has_role(admin)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)


@clear.error
async def clear_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRole):
        await ctx.send(":x: No dispones de admin " + ctx.author.mention)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(text="Introduce el número de mensajes a eliminar")


# Music
# join
@client.command()
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        commands_channel = client.get_channel(commands_chn)
        embed = discord.Embed(
            description=
            f"No estás en ningún canal de voz [{ctx.author.mention}]",
            color=discord.Colour.from_rgb(228, 233, 242))
        await commands_channel.send(embed=embed)


# leave
@client.command()
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        commands_channel = client.get_channel(commands_chn)
        embed = discord.Embed(
            description=
            f"No estoy en ningún canal de voz [{ctx.author.mention}]",
            color=discord.Colour.from_rgb(228, 233, 242))
        await commands_channel.send(embed=embed)


# play
# next
# stop
# resume
# BackUp
keep_alive()
client.run(os.getenv('TOKEN'))
