import discord
from discord.ext import commands
import telegram
import os
from dotenv import load_dotenv
from utils.utils import detect_solana_token_address
from logger import logger
import telegramify_markdown

# Load environment variables at the start
load_dotenv()
# Access your environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
DISCORD_USER_TOKEN = os.getenv('DISCORD_USER_TOKEN')

client = commands.Bot(command_prefix="!", self_bot=True)

telegram_bot = telegram.Bot(token=TELEGRAM_TOKEN)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Get channel and server info
    solana_addresses = detect_solana_token_address(message.content)
    # logger.info(f"Detected Solana addresses: {solana_addresses}")
    if solana_addresses:

        # Send the message to the Telegram channel
        channel_name = getattr(message.channel, 'name', 'direct-message')
    
        # Get server name safely
        server_name = message.guild.name if message.guild else "DM"
        
        # Format the message content
        log_message = f"""
    Server: {server_name}
    Channel: {channel_name}
    Author: {message.author}
    Content: {message.content}
    Time: {message.created_at}
    """
        logger.info(log_message)
        tmp = f"# {solana_addresses[0]}\n{log_message}"
        content = telegramify_markdown.markdownify(tmp)
        
        await telegram_bot.send_message(
            chat_id=TELEGRAM_CHANNEL_ID,
            text=content,
            parse_mode="MarkdownV2"
        )
        logger.info(f"Detected Solana addresses: {solana_addresses}")

    # Check if the message is a Telegram channel

client.run(DISCORD_USER_TOKEN)