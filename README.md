# 🤖 Discord Bot

A fun and functional Discord bot that welcomes users, rolls dice 🎲, sends Giphy GIFs 🐱, and can create temporary voice and text channels.

---

## 📦 Features

- ✅ Slash commands using `discord.app_commands`
- 🎲 Dice roller with interactive buttons (D6, D8, D10, D20)
- 🐱 Giphy integration (fail/cat)
- 📢 Auto welcome new members
- 📜 Temporary text and voice channels
- ⚙️ Easily extensible and modular architecture

---

## 🛠️ Tech Stack

- Python 3.11+
- [discord.py](https://discordpy.readthedocs.io/)
- `aiohttp` for async HTTP requests
- Environment-based config using `dotenv`

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/veras-d/discordBot.git
cd wastedservices-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup your environment variables

Create a `.env` file based on the example:

```bash
cp .env.example .env
```

Edit `.env` with your bot token and API key:

```env
DISCORD_BOT_TOKEN=your_discord_token_here
GIPHY_API_KEY=your_giphy_api_key_here
SERVER_ID=your_discord_server_id
```

### 4. Run the bot

```bash
python bot/main.py
```

---

## 🧱 Project Structure

```bash
bot/
├── __init__.py
├── events.py                 # on_ready and on_member_join handlers
├── commands/
│   ├── __init__.py
│   ├── gif.py                # /fail and /cat commands
│   ├── roll.py               # /roll command with dice buttons
│   └── temp_channels.py      # /create_temp_text_channel and /create_temp_voice_channel
├── utils/
│   ├── __init__.py
│   └── giphy.py              # Function to fetch gifs from Giphy
main.py                       # Entrypoint
.env.example
requirements.txt
```

---

## 🧪 Requirements

- Python 3.11+
- Discord Bot Token
- Giphy API Key

---

## 🧼 .gitignore

Make sure you're not committing sensitive info:

```
.env
__pycache__/
*.pyc
*.pyo
```

---

## 📬 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
