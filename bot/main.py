import asyncio
from telegram.ext import Application, MessageHandler, filters

from bot.database.models import import_all_models
from bot.message_manager.manager import handle_all_messages
from bot.database.session import init_db
from config.settings import TOKEN


async def main():
    # Инициализация бота
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_all_messages))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    import_all_models()
    init_db()

    try:
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, SystemExit):

        await app.updater.stop()
        await app.stop()
        await app.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
