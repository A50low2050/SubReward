from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard(channel_link: str) -> InlineKeyboardMarkup:

    keyboard = [
        [InlineKeyboardButton("Подписаться на канал", url=channel_link)],
        [InlineKeyboardButton("Я подписался! Получить бонус", callback_data="check_subscription")]
    ]
    return InlineKeyboardMarkup(keyboard)