import discord, os, re
from dotenv import load_dotenv

from main import keep_alive
from features.character_api import get_character_info
from utils.help_cmd_api import get_help_text as help_text
from utils.ping import ping, welcome_message

# Load environment variables
load_dotenv()

# Start Flask server
keep_alive()

"""Discord Bot Client Class"""
class MyClient(discord.Client):
  # Event listener for when the bot is ready
  async def on_ready(self):
    print(f"Logged on as {self.user}!")

  # Event listener for messages
  async def on_message(self, message):
    # Ignore messages sent by the bot itself
    if message.author == self.user:
      return

    content = message.content.strip()

    if content.startswith("$characters"):
      from features.character_list_api import get_characters_list
      await message.channel.send(get_characters_list())
    elif content.startswith("$character"):
      # Usage: $character <name>
      parts = content.split(maxsplit=1)
      if len(parts) < 2:
        await message.channel.send('Please provide a character name. Example: $character tanjiro')
      else:
        char = get_character_info(parts[1])
        if char:
          embed = discord.Embed(
            title=char.get('name', 'Unknown'),
            description=char.get('description', 'No description available.'),
            color=discord.Color.purple()
          )
          embed.add_field(name="Age", value=char.get('age', 'Unknown'), inline=True)
          embed.add_field(name="Gender", value=char.get('gender', 'Unknown'), inline=True)
          embed.add_field(name="Race", value=char.get('race', 'Unknown'), inline=True)
          if char.get('affiliation'):
            embed.add_field(name="Affiliation", value=char['affiliation'].get('name', 'Unknown'), inline=True)
          if char.get('first_arc_appearance'):
            embed.add_field(name="First Arc Appearance", value=char['first_arc_appearance'].get('name', 'Unknown'), inline=True)
          if char.get('quote'):
            embed.add_field(name="Quote", value=char['quote'], inline=False)
          if char.get('combat_style') and isinstance(char['combat_style'], list):
            styles = '\n'.join([f"{style.get('name', 'Unknown')}: {style.get('description', '')}" for style in char['combat_style']])
            embed.add_field(name="Combat Styles", value=styles, inline=False)
          if char.get('img'):
            embed.set_thumbnail(url=char['img'])
          await message.channel.send(embed=embed)
        else:
          await message.channel.send('Character not found or failed to fetch info.')
    elif content.startswith("$combatstyles"):
      from features.combat_style_api import get_combat_styles_list
      await message.channel.send(get_combat_styles_list())
    elif content.startswith("$combatstyle"):
      # Usage: $combatstyle <name>
      from features.combat_style_api import get_combat_style
      parts = content.split(maxsplit=1)
      if len(parts) < 2:
        await message.channel.send('Please provide a combat style name. Example: $combatstyle water breathing')
      else:
        await message.channel.send(get_combat_style(parts[1]))
    elif content.startswith("$random"):
      from features.random_character_api import get_random_character
      char = get_random_character()
      if char:
        embed = discord.Embed(
          title=char.get('name', 'Unknown'),
          description=char.get('description', 'No description available.'),
          color=discord.Color.purple()
        )
        embed.add_field(name="Age", value=char.get('age', 'Unknown'), inline=True)
        embed.add_field(name="Gender", value=char.get('gender', 'Unknown'), inline=True)
        embed.add_field(name="Race", value=char.get('race', 'Unknown'), inline=True)
        if char.get('affiliation'):
          embed.add_field(name="Affiliation", value=char['affiliation'].get('name', 'Unknown'), inline=True)
        if char.get('first_arc_appearance'):
          embed.add_field(name="First Arc Appearance", value=char['first_arc_appearance'].get('name', 'Unknown'), inline=True)
        if char.get('quote'):
          embed.add_field(name="Quote", value=char['quote'], inline=False)
        if char.get('combat_style') and isinstance(char['combat_style'], list):
          styles = '\n'.join([f"{style.get('name', 'Unknown')}: {style.get('description', '')}" for style in char['combat_style']])
          embed.add_field(name="Combat Styles", value=styles, inline=False)
        if char.get('img'):
          embed.set_thumbnail(url=char['img'])
        await message.channel.send(embed=embed)
      else:
        await message.channel.send('No characters found or failed to fetch.')
    elif content.startswith("$help"):
      await message.channel.send(help_text())
    elif content.startswith("$docs"):
      await message.channel.send('Demon Slayer API docs: https://www.demonslayer-api.com/docs')
    elif content.startswith(("$welcome", "$start", "$hello", "$ping")):
      await message.channel.send(welcome_message())
    elif content.startswith("$ping"):
      await message.channel.send(ping())
    else:
      return

# Initialize and run the Discord client
intents = discord.Intents.default()
intents.message_content = True

# Create and run the client
client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))