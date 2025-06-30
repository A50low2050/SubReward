from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from bot.keyboards.main_menu import start_keyboard

CHANNEL_LINK = "https://t.me/beautyserviceb2b"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user

    welcome_text = f"""
    Привет, {user.first_name}! 👋

    Добро пожаловать в BeautyService B2B - платформу для профессионалов индустрии красоты!

    🎁 Получите специальный бонус за подписку на наш канал:
    {CHANNEL_LINK}

    После подписки нажмите кнопку ниже, чтобы получить бонус!
    """

    await update.message.reply_text(
        text=welcome_text,
        reply_markup=start_keyboard(CHANNEL_LINK)
    )

# Экспортируем обработчик для удобного импорта
start_handler = CommandHandler("start", start)