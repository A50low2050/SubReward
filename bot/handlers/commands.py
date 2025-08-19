import logging
from datetime import datetime
from pyexpat.errors import messages

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from bot.messages import messages
from config.settings import GROUP_ID
from bot.validators.subscription_validator import SubscriptionValidator
from bot.keyboards import keyboards
from service.ApiClient import ApiService
from bot.models.user import User


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("update:", update)

    member = await context.bot.get_chat_member(chat_id=GROUP_ID, user_id=update.effective_user.id)
    service = ApiService()
    args = context.args
    user = User(
        None,
        update.message.from_user.id,
        None,
        update.message.from_user.last_name,
        update.message.from_user.first_name,
        None,
        None,
        False,
        False,
        str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        []
    )

    if member.status in ["member", "administrator", "creator"]:
        user.subscribe_to_group = True
        user.giving_gift = True

    if args and args[0].startswith('ref_'):
        user.referral_id = args[0][4:]

        # await track_referral(update, context)
    validate = SubscriptionValidator()
    print(validate.validate(user))
    if user.referral_id is not None or not user.subscribe_to_group:

        await update.message.reply_text(
            messages.general(),
            reply_markup=await keyboards.start(),
            parse_mode="Markdown")

    elif user.subscribe_to_group:

        await update.message.reply_text(
            messages.general(),
            reply_markup=await keyboards.start_subscribed(),
            parse_mode="Markdown")

    await service.new_member(user)


def setup_handlers_commands():
    return [
        CommandHandler("start", start),
    ]
