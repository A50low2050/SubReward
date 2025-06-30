from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Опция 1", callback_data="opt1")],
        [InlineKeyboardButton("Опция 2", callback_data="opt2")]
    ])

async def send_buttons(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Предупредить ⚠️", callback_data="warn_user")],
        [InlineKeyboardButton("Забанить 🔨", callback_data="ban_user"),
         InlineKeyboardButton("Простить 😇", callback_data="pardon_user")]
    ]
    await update.message.reply_text(
        "Выберите действие:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
