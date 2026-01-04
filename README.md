## KimetsuBot - Demon Slayer Discord Bot

A modular Discord bot for Demon Slayer fans, using the https://www.demonslayer-api.com API.

### ✨ Features
- `$characters` — Get a list of all Demon Slayer characters
- `$character <name>` — Get info about a specific character
- `$combatstyles` — Get a list of all combat styles
- `$combatstyle <name>` — Get info about a specific combat style
- `$help` — Show help message
- `$docs` — Show API documentation link
- `$welcome` — Get a welcome message

### 🗂️ File Structure

```
bot.py                # Discord bot logic & command handling
main.py               # Flask server to keep bot alive
requirements.txt      # Python dependencies
features/
  character_api.py    # Fetches character info from API
  character_list_api.py # Fetches character list from API
  combat_style_api.py # Fetches combat style info/list from API
utils/
  help_cmd_api.py     # Help command text
  ping.py             # Ping response
```

### 🚀 Getting Started

1. Clone this repo
2. Install dependencies:
	```
	pip install -r requirements.txt
	```
3. Add your Discord token to a `.env` file:
	```
	DISCORD_TOKEN=your_token_here
	```
4. Run the bot:
	```
	python bot.py
	```

### 💬 Commands

| Command                | Description                                 |
|------------------------|---------------------------------------------|
| $characters            | List all Demon Slayer characters            |
| $character <name>      | Info about a specific character             |
| $combatstyles          | List all combat styles                      |
| $combatstyle <name>    | Info about a specific combat style          |
| $help                  | Show help message                           |
| $docs                  | Show API documentation link                 |
| $welcome               | Get a welcome message                       |

---
Made with ❤️ for Demon Slayer fans!
