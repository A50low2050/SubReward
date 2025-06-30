import logging

from telegram.ext import Application
from config.settings import TOKEN
from bot.handlers import commands


def main():
    logging.basicConfig(
        level=logging.DEBUG,  # Включаем все логи
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    app = Application.builder().token(TOKEN).build()

    all_handlers = (
        commands.setup_handlers()
    )
    # Обработчики команд
    # app.add_handler(CommandHandler("start", commands.start))
    # app.add_handler(CommandHandler("warn", warn_user))
    # app.add_handler(CommandHandler("buttons", generate_referral_link))

    # Обработчики сообщений
    # app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, delete_links))

    # Добавляем все обработчики
    app.add_handlers(all_handlers)

    # Запуск бота
    app.run_polling()


if __name__ == "__main__":
    main()

