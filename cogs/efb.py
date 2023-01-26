from discord.ext import commands, tasks
from discord import app_commands
import discord
from tools.embedtools import embed_builder
import config
import tools.db as db


class EFB(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def profile(self, interaction:discord.Interaction):
        try:
            await interaction.channel.send("Vitun paska ei toimi ees vittu")
            """Tekee profiilin ja jos profiili on näyttää statsit"""
            stats = db.create_account(interaction.user.id, interaction.user.name)
            em = await embed_builder(interaction, f"Pelaajan {interaction.user.name} statsit", description=stats, image="./models/player/player_model.png")
            await interaction.channel.send(embed=em)
        except Exception as e:
            print(e)    

async def setup(bot):
    await bot.add_cog(EFB(bot),
    guilds= [discord.Object(config.TEST_GUILD)])
