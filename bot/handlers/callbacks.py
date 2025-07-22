from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes, CallbackContext
from bot.messages import messages


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Обязательно подтверждаем нажатие

    # Получаем данные из callback_data
    action = query.data

    if action == "warn":
        await warn_user(update, context)
    elif action == "ban":
        await new_member(update, context)
    elif action == "pardon":
        await pardon_user(update, context)


async def warn_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.edit_message_text("Пользователь был предупрежден ⚠️")


async def ban_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.edit_message_text("Пользователь забанен 🔨")


async def pardon_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.edit_message_text("Пользователь прощен 😇")





def setup_handlers_callbacks():
    return CallbackQueryHandler(button_handler)
