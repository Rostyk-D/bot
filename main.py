from config.config import bot, BOT_TOKEN, random, discord
from music.help_cog import help_cog
from music.music_cog import music_cog
from functional_bot.text_cog import text_cog
import asyncio

# remove the default help command so that we can write our own
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' ({channel})")

    if isinstance(message.channel, discord.DMChannel) and user_message.lower().startswith('!clear'):
        ctx = await bot.get_context(message)
        await bot.invoke(ctx)
    elif user_message.lower() == 'hi':
        await message.channel.send('Hello!')
    elif user_message.lower() == 'roll':
        await message.channel.send(str(random.randint(0, 10)))
    elif user_message.lower() == 'thank':
        await message.channel.send('Ok')
    else:
        await bot.process_commands(message)

async def start_bot():
    await bot.login(BOT_TOKEN)
    # Додаємо коги
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(text_cog(bot))
    # Починаємо бота
    try:
        await bot.start(BOT_TOKEN)
    finally:
        await bot.close()

# Запускаємо бота
asyncio.run(start_bot())
