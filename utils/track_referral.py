from decimal import Context
from telegram import Update
from telegram.error import BadRequest
from config.settings import GROUP


async def track_referral(update: Update, context: Context, referrer_id: str):

    group_id = -1002632486930

    try:
        # Получаем информацию о пользователе в группе
        member = await context.bot.get_chat_member(chat_id=group_id, user_id=update.effective_user.id)

        # Проверяем статус пользователя
        if member.status in ["member", "administrator", "creator"]:
            # Пользователь в группе
            await update.message.reply_text(
                "✅ Вы состоите в группе! Спасибо!\n"
                f"Пригласивший: ID {referrer_id}"
            )
            # Записываем в БД (если нужно)
            # save_referral(update.effective_user.id, referrer_id)
        else:
            # Пользователь не в группе (например, вышел или его выгнали)
            await update.message.reply_text(
                "❌ Вы не состоите в нашей группе. Вступите, и получите подарок.\n"
                f"'https://t.me/{GROUP}'"
            )

    except BadRequest as e:
        if "user not found" in str(e).lower():
            # Пользователь точно не в группе (если группа приватная)
            await update.message.reply_text("❌ Вы не состоите в нашей группе. Вступите, чтобы продолжить.")
        else:
            print(f"Ошибка при проверке участника: {e}")
            await update.message.reply_text("⚠ Произошла ошибка при проверке.")
