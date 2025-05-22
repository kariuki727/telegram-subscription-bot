import logging
import os
from aiogram import Bot, Dispatcher, executor
from bot.handlers import register_handlers

API_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

def main():
    register_handlers(dp)
    logger.info("Bot is starting...")
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()
