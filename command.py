from discord.ext import commands
import discord
import json
import requests

bot = commands.Bot(command_prefix='<')

@bot.command()
async def info(ctx):
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

@bot.remove_command('help')

@bot.command()
async def kick(ctx,user):
    await ctx.send(f"Kicked {user}")

def jokes_json():
    response=requests.get('https://icanhazdadjoke.com/slack')
    json_data=json.loads(response.text)
    joke=""+json_data['attachments'][0]['text']
    return joke

@bot.command()
async def jokes(ctx,*args,**kwargs):
    joke=jokes_json()

    await ctx.send(joke)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Command Help',
        description='I am here for you!',
        color=discord.Color.red()
    )
    embed.add_field(
        name='<kick',
        value='This command will help you to kick some one!',
        inline=False
    )
    embed.add_field(
        name='<info',
        value='This command will help you to to get info of your id!',
        inline=False
    )
    embed.add_field(
        name='<jokes',
        value='This command will help you to to get jokes!',
        inline=False
    )
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.listen()
async def on_message(message):
    if message.author==bot.user:
        return
    if message.content=='hello' or message.content=='Hello':
        await message.channel.send("Welcome to our server")

    if message.content == 'good':
        await message.add_reaction('\U0001F47B')

    member = f"{message.author}";
    if member=="Irfan#5854":
        await message.channel.send("Now it's study time!")





@bot.listen()
async def on_message_edit(before,after):
    await before.channel.send(
        f'message was edited by {before.author} \n'
        f'before message was {before.content} \n'
        f'after message is {after.content} \n'
    )

@bot.listen()
async def on_reaction_add(reaction,user):
    if user==bot.user:
        return
    else:
        await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')




token="ODk1MzIxODEwMTMwODM3NTI1.YV23aQ.pQIFZu85x6UvvVikEeePqXnRfPY"


bot.run(token)
