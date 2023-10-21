import discord
from discord.ext import commands

client = commands.Bot(help_command=None,
                      command_prefix="",
                      intents=discord.Intents().all())

@client.tree.command(name="badge")
async def _badge(interaction: discord.Interaction):
    await interaction.response.send_message(f"Command completed, you will get the badge", ephemeral=True)

@client.event
async def on_ready():
    await client.loop.create_task(client.tree.sync())

client.run(input("Paste your Token > "))
