from collections import defaultdict

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


async def start():
    keyboard = [
        [InlineKeyboardButton("Тест ⚠️", callback_data="start")],
        [InlineKeyboardButton("Забанить 🔨", callback_data="warn"),
         InlineKeyboardButton("Простить 😇", callback_data="ban")
        ]
    ]
    # return InlineKeyboardMarkup(keyboard)
    return InlineKeyboardMarkup(keyboard)


async def ref(ref_link):
    keyboard = [
        [InlineKeyboardButton("Поделиться ссылкой", url=f"tg://msg_url?url={ref_link}&text=Присоединяйся!")]
    ]

    return InlineKeyboardMarkup(keyboard)

