import discord
from discord.ext import commands
import random

TOKEN = 'MTE4OTg4NTI5MTY3OTQ0OTEzOQ.Gu2gJq.P3L6WgWgQ8zRiGmRSH1Fn2bSrq5e4iLvwV9960'
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' ({channel})")

    if isinstance(message.channel, discord.DMChannel) and user_message.lower().startswith('!clear'):
        command = user_message.split(' ')[0]  # Get the command part from the message
        message.content = command  # Set the content to command
        ctx = await bot.get_context(message)
        await bot.invoke(ctx)
    elif user_message.lower() == 'hi':
        await message.channel.send('Hello!')
    elif user_message.lower() == 'roll':
        await message.channel.send(str(random.randint(0, 10)))
    elif user_message.lower() == '!help':
        await message.channel.send("`This is a help message!`")
    else:
        await bot.process_commands(message)


@bot.command()
async def clear(ctx, amount: str = ""):
    if isinstance(ctx.channel, discord.TextChannel):  # Check if it's a TextChannel
        if amount.lower() == "all":
            await ctx.channel.purge(limit=None)
            await ctx.send('All messages have been deleted.', delete_after=5)
        elif amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                if isinstance(ctx.author, discord.Member) and ctx.author.guild_permissions.manage_messages:
                    await ctx.channel.purge(limit=amount + 1)
                    await ctx.send(f'{amount} messages have been deleted.', delete_after=5)
                else:
                    await ctx.send("You don't have permission to use this command.")
            else:
                await ctx.send("Amount should be a positive number.")
        else:
            await ctx.send("Invalid amount. Use '!clear all' or provide a valid number.")
    else:
        await ctx.send("This command can't be used in DMs.")


@bot.command()
async def roll(ctx, start: int, end: int):
    if isinstance(ctx.channel, discord.TextChannel):  # Check if it's a TextChannel
        if start < end:
            result = random.randint(start, end)
            await ctx.send(f'Random number between {start} and {end}: {result}')
        else:
            await ctx.send("The start number should be less than the end number.")
    else:
        await ctx.send("This command can't be used in DMs.")

if __name__ == '__main__':
    bot.run(TOKEN)
