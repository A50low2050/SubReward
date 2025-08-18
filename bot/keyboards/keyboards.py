from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from config.settings import GROUP


async def start():
    keyboard = [
        [InlineKeyboardButton("Подписаться на группу в телеграмм ⚠️", callback_data="subscribe")],
        [InlineKeyboardButton("О нас  🔨", callback_data="about"),
         InlineKeyboardButton("Получить оптовый прайс 😇", url="https://beautyservice.ru/price/"  # Прямая ссылка
                              )],
        [InlineKeyboardButton("💰Акции и спецпредложения", callback_data="stocks")],
        [InlineKeyboardButton("📞 Связаться с менеджером", callback_data="contact_the_manager")],

    ]
    return InlineKeyboardMarkup(keyboard)


async def start_subscribed():
    keyboard = [
        [
            InlineKeyboardButton("О нас  🔨", callback_data="about"),
            InlineKeyboardButton("Получить оптовый прайс 😇", url="https://beautyservice.ru/price/")
        ],
        [InlineKeyboardButton("💰Акции и спецпредложения", callback_data="stocks")],
        [InlineKeyboardButton("📞 Связаться с менеджером", callback_data="contact_the_manager")],

    ]
    return InlineKeyboardMarkup(keyboard)


async def assistance_and_training() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("📹Видеообзоры продукции", callback_data="btn1")],
        [InlineKeyboardButton("📖Гайды по уходу за волосами", callback_data="btn2")],
        [InlineKeyboardButton("💡Тренды 2025 года", callback_data="btn3")],
        [InlineKeyboardButton("⬅️ Главное меню", callback_data="main_menu")]

    ]
    return InlineKeyboardMarkup(keyboard)


async def about() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("💰 Условия оплаты", callback_data="paymentsOptions"),
         InlineKeyboardButton(" О компании", callback_data="about_the_company")
         ],
        [
            InlineKeyboardButton("🚚 Условия доставки", callback_data="delivery"),
            InlineKeyboardButton("🔄 Условия обмена", callback_data="refund")
        ],
        [InlineKeyboardButton("💎 Программа лояльности", url="https://beautyservice.ru/help/programma-loyalnosti")],
        [InlineKeyboardButton("👤 Зарегистрироваться", url="https://beautyservice.ru/auth/registrationx")],
        [InlineKeyboardButton("⬅️ Главное меню", callback_data="main_menu")]

    ]
    return InlineKeyboardMarkup(keyboard)


async def ref(ref_link):
    keyboard = [
        [InlineKeyboardButton("Поделиться ссылкой", url=f"tg://msg_url?url={ref_link}&text=Присоединяйся!")]
    ]

    return InlineKeyboardMarkup(keyboard)


async def stocks():
    keyboard = [
        [InlineKeyboardButton("Телеграм", url=f"https://t.me/beautyserviceb2b/4443")],
        # [InlineKeyboardButton("Вк", callback_data="btn3")],
        [InlineKeyboardButton("Cайт", url="https://beautyservice.ru/sale/")],
        [InlineKeyboardButton("⬅️ Главное меню", callback_data="main_menu")]
    ]

    return InlineKeyboardMarkup(keyboard)


async def contact_the_manager():
    phone_number = "8 (800) 555-15-76"  # Красивый формат для отображения
    clean_phone = "+78005551576"
    keyboard = [
        # [InlineKeyboardButton("заказать звонок", callback_data="call_back")],
        # [InlineKeyboardButton("написать менеджеру", callback_data="write_to_the_manager")],
        # [InlineKeyboardButton("позвонить менеджеру", callback_data="call_manager")],
        [InlineKeyboardButton("⬅️ Главное меню", callback_data="main_menu")]
    ]

    return InlineKeyboardMarkup(keyboard)


async def back_about():
    keyboard = [
        [InlineKeyboardButton("⬅️ Назад", callback_data="about")]
    ]

    return InlineKeyboardMarkup(keyboard)


async def subscribe():
    group_invite_link = f"https://t.me/{GROUP}"

    keyboard = [
        [InlineKeyboardButton("Подписаться", url=group_invite_link)],
        [InlineKeyboardButton("⬅️ Главное меню", callback_data="main_menu")]
    ]

    return InlineKeyboardMarkup(keyboard)


async def invitation_to_subscribe():
    keyboard = [
        [InlineKeyboardButton("🔔 Подписаться на группу", url=f"https://t.me/{GROUP}")],
    ]

    return InlineKeyboardMarkup(keyboard)
