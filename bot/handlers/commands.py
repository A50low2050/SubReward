import logging
from pyexpat.errors import messages

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from config.settings import BOT
from bot.messages import messages
from utils.track_referral import track_referral
from bot.keyboards import keyboards
from service.apiService import ApiService
from bot.models.user import User


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from_user = update.message.from_user
    member = User(
        None,
        update.message.from_user.id,
        None,  # Можно оставить None или заполнить по необходимости
        update.message.from_user.last_name,
        update.message.from_user.first_name,
        None,
        None,
        False,
        str(update.message.date)  # или текущая дата/время
    )

    args = context.args

    if 'start_count' not in context.user_data:
        context.user_data['start_count'] = 1
        await update.message.reply_text(messages.first_welcome_messege())

    if args and args[0].startswith('ref_'):
        referrer_id = args[0][4:]  # ID пригласившего

        member.referral_id = referrer_id
        print(member.to_dict())
        service = ApiService()

        await track_referral(update, context, referrer_id)

        await service.new_member(member.to_d())
    else:
        await update.message.reply_text(
            messages.start(),
            reply_markup=await keyboards.start(),
            parse_mode="Markdown"
        )


# async def greet_new_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Приветствие новых участников"""
#     for member in update.message.new_chat_members:
#         await update.message.reply_text(
#             f"Добро пожаловать, {member.mention_markdown()}!\n"
#             "Пожалуйста, ознакомьтесь с правилами группы."
#         )


async def get_referral_link(update: Update, context):
    user_id = update.effective_user.id
    ref_link = f"https://t.me/{BOT}?start=ref_{user_id}"

    await update.message.reply_text(
        messages.ref(ref_link),
        reply_markup=await keyboards.ref(ref_link),
        parse_mode="Markdown"
    )

    # async def process_referral(referrer_id: int, new_user_id: int):
    # Здесь логика начисления бонусов
    # Пример с SQLite базой:
    # import sqlite3
    # conn = sqlite3.connect('bot.db')
    # cursor = conn.cursor()

    # # Добавляем запись о реферале
    # cursor.execute(
    #     "INSERT OR IGNORE INTO referrals (referrer_id, referral_id) VALUES (?, ?)",
    #     (referrer_id, new_user_id)
    # )
    #
    # # Начисляем бонусы
    # cursor.execute(
    #     "UPDATE users SET balance = balance + 100 WHERE user_id = ?",
    #     (referrer_id,)
    # )

    # conn.commit()
    # conn.close()

    # # Уведомляем пригласившего
    # await context.bot.send_message(
    #     chat_id=referrer_id,
    #     text="🎉 По вашей ссылке зарегистрировался новый пользователь! +100 баллов!"
    # )


def setup_handlers_commands():
    return [
        CommandHandler("start", start),
        CommandHandler("ref", get_referral_link)
    ]
