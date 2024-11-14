import discord
from discord.ext import commands
import telegram
import os
from dotenv import load_dotenv
from utils.utils import detect_solana_token_address, save_address, load_tracked_addresses
from logger import logger
import telegramify_markdown
import asyncio 

# Load environment variables at the start
load_dotenv()

# Access your environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
DISCORD_USER_TOKEN = os.getenv('DISCORD_USER_TOKEN')

print(f"TELEGRAM_CHANNEL_ID, {TELEGRAM_CHANNEL_ID}")

client = commands.Bot(command_prefix="!", self_bot=True)

telegram_bot = telegram.Bot(token=TELEGRAM_TOKEN)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    solana_addresses = detect_solana_token_address(message.content)
    logger.info(f"Detected Solana addresses: {solana_addresses}")

    if solana_addresses:
        # channel_name = getattr(message.channel, 'name', 'direct-message')
        # server_name = message.guild.name if message.guild else "DM"
        
#         log_message = f"""
# Server: {server_name}
# Channel: {channel_name}
# """
# Author: {message.author}
        # logger.info(log_message)

        #filter
        tracked_addresses = load_tracked_addresses()
        # Send separate message for each address
        for address in solana_addresses:
            if address not in tracked_addresses:
                tmp = f"{address}"
                content = telegramify_markdown.markdownify(tmp)
                
                await telegram_bot.send_message(
                    chat_id=TELEGRAM_CHANNEL_ID,
                    text=content,
                    parse_mode="MarkdownV2"
                )
                logger.info(f"Sent message for address: {address}")
                save_address(address)
                await asyncio.sleep(1)
            else:
                logger.info(f"Address already tracked: {address}")

client.run(DISCORD_USER_TOKEN)
