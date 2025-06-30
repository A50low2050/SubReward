import logging
from telegram.ext import Application, CallbackQueryHandler
from dotenv import load_dotenv
import os

from bot.handlers.start import start_handler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(start_handler)

    application.run_polling()

if __name__ == "__main__":
    main()