from config.config import discord, commands, random

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = ""
        self.text_channel_list = []
        self.set_message()

    def set_message(self):
        self.help_message = f"""
```
Основні команди:
{self.bot.command_prefix}help - Вивід інформації про команди

{self.bot.command_prefix}q - показує список пісень
{self.bot.command_prefix}p/play <keywords> - Грає пісню в войс чаті з <youtube>.
{self.bot.command_prefix}skip - пропустити пісню.
{self.bot.command_prefix}clean - зупинити пісню і почистити список пісень.
{self.bot.command_prefix}stop - Вихід з войс чата.
{self.bot.command_prefix}pause - пауза пісні.
{self.bot.command_prefix}resume - продовження пісні.
{self.bot.command_prefix}prefix - Поміняти символ команди
{self.bot.command_prefix}remove - удалити останню пісню з списка

{self.bot.command_prefix}clear/c - для адміністраціїї щоби чистити чат.
{self.bot.command_prefix}roll <star> <end> - з вибіркі вибрає рандомне числов 
{self.bot.command_prefix}loop/lp - зациклення музикі <покіщо не працює>
```
"""

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(f"Пиши {self.bot.command_prefix}help"))
        print(f"Bot started!")

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    @commands.command(name="prefix", help="Change bot prefix")
    async def prefix(self, ctx, *args):
        self.bot.command_prefix = " ".join(args)
        self.set_message()
        await ctx.send(f"Префікс змінений на **'{self.bot.command_prefix}'**")
        await self.bot.change_presence(activity=discord.Game(f"type {self.bot.command_prefix}help"))

    @commands.command(name="send_to_all", help="send a message to all members")
    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
