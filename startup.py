import os
import logging
import sys
import discord
from discord.ext import commands
from utils.sqlite import DataBase

handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')

extensions = ['cogs.modify', 'cogs.query', 'cogs.misc']


class Bot(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print(f'Discordpy version: {discord.__version__}')
        print(f'Python version: {sys.version}')
        print('---------')

    async def setup_hook(self):
        for extension in extensions:
            await self.load_extension(extension)
        self.db = DataBase(self, 'data.sqlite')


intents = discord.Intents.all()

bot = Bot('>', intents=intents)
bot.remove_command('help')
bot.run(os.environ.get('FACILITYLOCATOR_API_TOKEN'), log_handler=handler)
