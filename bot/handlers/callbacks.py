from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackQueryHandler, ContextTypes, CallbackContext
from bot.messages import messages
from utils.track_referral import track_referral
from bot.keyboards import keyboards

GET_PHONE = 1


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Обязательно подтверждаем нажатие

    # Получаем данные из callback_data
    action = query.data

    if action == "subscribe":
        await subscribe(update, context)
    elif action == "about":
        await about(update, context)
    elif action == "price_list":
        await price_list(update, context)
    elif action == "stocks":
        await stocks(update, context)
    elif action == "contact_the_manager":
        await contact_the_manager(update, context)
    elif action == "contact_the_manager":
        await contact_the_manager(update, context)
    elif action == "assistance_and_training":
        await assistance_and_training(update, context)
    elif action == "call_back":
        await call_back(update, context)
    elif action == "paymentsOptions":
        await paymentsOptions(update, context)
    elif action == "refund":
        await refund(update, context)
    elif action == "delivery":
        await delivery(update, context)
    elif action == "about_the_company":
        await about_the_company(update, context)


    elif action == "main_menu":
        await main_menu(update, context)

async def about_the_company(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=messages.first_welcome_messege(),
        reply_markup=await keyboards.back_about(),
        parse_mode='HTML',
    )
async def refund(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=messages.refundText(),
        reply_markup=await keyboards.back_about(),
        parse_mode='HTML',
    )


async def delivery(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=messages.delivery_text(),
        reply_markup=await keyboards.back_about(),
        parse_mode='HTML',
        disable_web_page_preview=True
    )


async def paymentsOptions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=messages.paymentsOptions(),
        reply_markup=await keyboards.back_about(),
        parse_mode='HTML',
    )


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    text = await track_referral(update, context)
    await query.answer()
    await query.edit_message_text(
        text=messages.subscribe(),
        reply_markup=await keyboards.subscribe()
    )


async def assistance_and_training(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()  # Обязательно отвечаем на callback_query
    await query.edit_message_text(
        text=messages.assistance_and_training(),
        reply_markup=await keyboards.assistance_and_training()
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()
    await query.edit_message_reply_markup(
        reply_markup=await keyboards.about()
    )


async def price_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.edit_message_text("Раздел находиться в разработке 😇")


async def stocks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()
    await query.edit_message_reply_markup(
        reply_markup=await keyboards.stocks()
    )


async def contact_the_manager(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()
    await query.edit_message_text(
        text=messages.contact_the_manager(),
        parse_mode='HTML',
        reply_markup=await keyboards.contact_the_manager(),

    )


async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        text=messages.first_welcome_messege(),
        reply_markup=await keyboards.start_subscribed(),
        parse_mode="Markdown"

    )


async def call_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    query = update.callback_query
    await query.answer()

    await query.message.reply_text(
        "Оставьте ваш номер телефона, и наш менеджер свяжется с вами в рабочее время: будни с 9 до 18"
    )
    print(f"Current state: {context.user_data.get('state')}")

    return GET_PHONE


def setup_handlers_callbacks():
    return CallbackQueryHandler(button_handler)
