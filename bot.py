from settings import *
import discord
from bot_logic import *

def client():
    # La variable intents almacena los privilegios del bot
    intents = discord.Intents.default()
    # Activar el privilegio de lectura de mensajes
    intents.message_content = True
    # Crear un bot en la variable cliente y transferirle los privilegios
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Hemos iniciado sesión como {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send("Hi!")
        elif message.content.startswith('$smile'):
            await message.channel.send(gen_emodji())
        elif message.content.startswith('$bye'):
            await message.channel.send("\U0001f642")
        elif message.content.startswith('$GP'):
            await message.channel.send(gen_pass(random.randint(1,50)))
        elif message.content.startswith('$coin'):
            await message.channel.send(flip_coin())
        else:
            await message.channel.send(message.content)

    client.run("MTI5Njk3ODM3Nzg1NjY1MTMyNg.Gsgdqp.Q-9Nva_dUk-OQWtyq30R_Lz9xIqy9f-QpIydH0")

def bot():
    from discord.ext import commands

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

    @bot.command()
    async def hello(ctx):
        await ctx.send(f'Hola, soy un bot {bot.user}!')

    @bot.command()
    async def bye(ctx):
        await ctx.send('\U0001f642')

    @bot.command()
    async def heh(ctx, count_heh = 5):
        await ctx.send("he" * count_heh)
    
    @bot.command()
    async def GP(ctx):
        await ctx.send(gen_pass(random.randint(1,50)))

    @bot.command()
    async def coin(ctx):
        await ctx.send(flip_coin())

    @bot.command()
    async def Planta(ctx):
        await ctx.send(plantaR())

    @bot.command()
    async def roll(ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    bot.run("MTI5Njk3ODM3Nzg1NjY1MTMyNg.Gsgdqp.Q-9Nva_dUk-OQWtyq30R_Lz9xIqy9f-QpIydH0")

bot()