import asyncio
import uvicorn
from logger import get_logger
from bot.database.models import import_all_models
from bot.database.session import init_db
from config.settings import TOKEN
from telegram_bot_facade import telegram_bot
from bot.api.endpoints import app as fastapi_app


async def run_api():
    config = uvicorn.Config(
        fastapi_app, host="127.0.0.1", port=8001, log_level="info"
    )
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    # Инициализируем бота (возвращает None, но настраивает singleton)
    telegram_bot.init(TOKEN)

    # Получаем application из singleton
    app = telegram_bot.application

    # Инициализируем и запускаем бота
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    import_all_models()
    init_db()

    # Запускаем FastAPI и бота параллельно
    await asyncio.gather(
        run_api(),
        # Бот работает в отдельном потоке через polling
        # Нужно оставить его работать в основном потоке
    )

    # Останавливаем бота
    await app.updater.stop()
    await app.stop()
    await app.shutdown()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        get_logger.info("Bot is stopping")