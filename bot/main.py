import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram.ext import Application

from config.settings import TOKEN
from bot.handlers.callbacks import setup_handlers_callbacks
from bot.handlers.commands import setup_handlers_commands
from utils.cron.subscription_verification import subscribed_verification
from utils.cron.giving_gift import giving_gift

async def main():
    # Инициализация бота
    app = Application.builder().token(TOKEN).build()

    # Добавление обработчиков
    app.add_handlers(setup_handlers_commands())
    app.add_handler(setup_handlers_callbacks())



    scheduler = AsyncIOScheduler()
    # scheduler.add_job(
    #     subscribed_verification,
    #     'interval',
    #     seconds=5,
    #     args=[app],
    #     misfire_grace_time=60
    # )

    scheduler.add_job(
        giving_gift,
        'interval',
        # hours=1,
        seconds=10,
        args=[app],
        misfire_grace_time=60
    )

    scheduler.start()

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    try:
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, SystemExit):

        await app.updater.stop()
        await app.stop()
        await app.shutdown()
        scheduler.shutdown()


if __name__ == "__main__":
    # Запуск асинхронного main()
    asyncio.run(main())
