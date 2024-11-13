import discord
from discord.ext import commands
import telegram
import os
from dotenv import load_dotenv
from utils.utils import detect_solana_token_address
from logger import logger

# Load environment variables at the start
load_dotenv()
# Access your environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

# Initialize Discord client
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize Telegram bot
telegram_bot = telegram.Bot(token=TELEGRAM_TOKEN)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    # logger.info(f"Received message from {message.author}: {message.content}")
    # Detect Solana addresses in the message
    solana_addresses = detect_solana_token_address(message.content)
    # logger.info(f"Detected Solana addresses: {solana_addresses}")
    if solana_addresses:
        content = f"{solana_addresses[0]}\n{message.author.name} in #{message.channel.name}:\n{message.content}"
        
        await telegram_bot.send_message(
            chat_id=TELEGRAM_CHANNEL_ID,
            text=content,
        )
        logger.info(f"Detected Solana addresses: {solana_addresses}")
    # Handle attachments (images, files, etc.)
    # if message.attachments:
    #     for attachment in message.attachments:
    #         # For images
    #         if any(attachment.filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif']):
    #             await telegram_bot.send_photo(
    #                 chat_id=TELEGRAM_CHANNEL_ID,
    #                 photo=attachment.url,
    #                 caption=content
    #             )
    #         # For other files
    #         else:
    #             await telegram_bot.send_document(
    #                 chat_id=TELEGRAM_CHANNEL_ID,
    #                 document=attachment.url,
    #                 caption=content
    #             )
    # else:
    # Send text message
    # await telegram_bot.send_message(
    #     chat_id=TELEGRAM_CHANNEL_ID,
    #     text=content,
    #     # parse_mode=telegram.ParseMode.MARKDOWN
    # )

    await bot.process_commands(message)

# Run the Discord bot
bot.run(DISCORD_TOKEN)