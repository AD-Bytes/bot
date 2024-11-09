from settings import *
import discord
from bot_logic import *
import os
import random
from get_duck import *
from get_apokemon import *
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

    client.run("TOKEN HERE")

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
    async def mem(ctx):
        with open('bot//images//meme1.jpeg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    @bot.command()
    async def memealeatorio(ctx):
        meme = random.choice(os.listdir('bot//images'))
        with open(f'bot//images//{meme}', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    @bot.command('duck')
    async def duck(ctx):
        '''Una vez que llamamos al comando duck, 
        el programa llama a la función get_duck_image_url'''
        image_url = get_duck_image_url()
        await ctx.send(image_url)
    @bot.command('pokemon')
    async def pokemon(ctx):
        '''Una vez que llamamos al comando pokemon, 
        el programa llama a la función get_pokemon_img_url'''
        image_url = get_apokemon_img_url()
        await ctx.send(image_url)
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

    bot.run("TOKEN HERE")

bot()
