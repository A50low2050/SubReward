import logging
from telegram.ext import Application
from config.settings import TOKEN
from bot.handlers.messages import setup_handlers_messages
from bot.handlers.callbacks import setup_handlers_callbacks
from bot.handlers.commands import setup_handlers_commands

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.DEBUG
# )

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handlers(setup_handlers_commands())
    app.add_handler(setup_handlers_callbacks())
    app.add_handlers(setup_handlers_messages())

    app.run_polling()


if __name__ == "__main__":
    main()
