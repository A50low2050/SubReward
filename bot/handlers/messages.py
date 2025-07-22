from dataclasses import dataclass

from telegram import Update
from telegram.ext import MessageHandler, filters, CallbackContext
from bot.messages import messages
from utils.GiftManager import GiftManager
from bot.models.user import User


async def new_member(update: Update, context: CallbackContext):
    user_data = None

    for user in update.message.new_chat_members:
        user_data = User(
            full_name=user.full_name,
            username=user.username,
            id=user.id
        )

    print(user_data)

    if user_data is not None:
        await update.message.reply_text(
            messages.welcome(user_data)
        )

        gift = GiftManager()

        if await gift.send_gift(user_data):
            await context.bot.send_message(
                chat_id=user_data.id,
                text=messages.gift()
            )


def setup_handlers_messages():
    return [
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member)

    ]
