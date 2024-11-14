# D2T-msg-forward using Self-Bot

This is a simple Python script that forwards messages from a Discord channel to a Telegram channel when a message includes a Solana token address.
This is a **self-bot**.

## Main Features

- Forward messages from a Discord channel to a Telegram channel.

## Screenshots

## Tech stack

- Python
- Discord Self-bot
- Discord.py
- telegram.py
- telegramify_markdown

## Prerequisites

- Python 3.13.0 or higher
- Telegram bot
- Telegram channel

## Configuration

1. clone the repository:

```
https://github.com/Any-bot/D2T-msg-forward.git
```

2. Go to the project directory:

```
cd D2T-msg-forward
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Create a .env file in the root directory of the project and add the following variables:

```
DISCORD_USER_TOKEN=
TELEGRAM_TOKEN=
TELEGRAM_CHANNEL_ID=
```

5. Run the script:

```
python main.py
```

## Version 1.0 13/11/2024
