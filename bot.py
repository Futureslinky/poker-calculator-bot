import discord
from discord.ext import commands, events

import config

COGS = [
    "bot",
]


class Bot(commands.Bot, events.EventsMixin):
    def __init__(self, **kwargs):
      
        self.config = config
      
        super().__init__(
            **kwargs,
            command_prefix=config.PREFIX,
            intents=discord.Intents.all(),
            allowed_mentions=discord.AllowedMentions(everyone=False, roles=False),
            case_insensitive=True,
        )
        
    async def setup_hook(self):
        await self.load_extension("jishaku")
        for i in COGS:
            await self.load_extension(f"cogs.{i}")

    async def close(self):
        await super().close()


if __name__ == "__main__":
    bot = Bot()
    bot.run(config.BOT_TOKEN)
