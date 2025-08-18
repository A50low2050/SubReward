from decimal import Context
from telegram import Update
from telegram.error import BadRequest
from config.settings import GROUP,GROUP_ID


async def track_referral(update: Update, context: Context):

    try:
        member = await context.bot.get_chat_member(chat_id=GROUP_ID, user_id=update.effective_user.id)

        if member.status in ["member", "administrator", "creator"]:
            return ("✅ Вы состоите в группе! Спасибо!\n")
        else:
            return (

                "❌ Вы не состоите в нашей группе. Вступите, и получите подарок.\n"
                f"'https://t.me/{GROUP}'"
            )

    except BadRequest as e:
        if "user not found" in str(e).lower():
            # Пользователь точно не в группе (если группа приватная)
            return ("❌ Вы не состоите в нашей группе. Вступите, чтобы продолжить.")
        else:
            print(f"Ошибка при проверке участника: {e}")
            return ("⚠ Произошла ошибка при проверке.")
