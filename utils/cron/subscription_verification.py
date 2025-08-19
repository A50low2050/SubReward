import json

from telegram.constants import ParseMode
from datetime import datetime, timedelta, timezone

from bot.keyboards.keyboards import invitation_to_subscribe
from bot.messages.messages import invitation_to_subscribe_text
from bot.models.user import User
from config.settings import GROUP_ID, GROUP
from service.ApiClient import ApiService


async def subscribed_verification(app):
    print("Проверка подписки пользователей, крон задача")
    client = ApiService()

    print(f"получаем юзеров для нотификации")
    user = await client.get_non_subscribed_users()
    users = create_users_from_response(user)

    for user in users:

        try:
            member = await app.bot.get_chat_member(chat_id=GROUP_ID, user_id=user.user_id)

            if member.status in ["member", "administrator", "creator"]:
                user.subscribe_to_group = True
                await client.update_user(user)

            elif await check_user_status(user):
                await app.bot.send_message(
                    chat_id=user.user_id,
                    text=invitation_to_subscribe_text(GROUP),
                    parse_mode=ParseMode.HTML,
                    reply_markup=await invitation_to_subscribe()
                )
        except Exception as e:
            print(f"Ошибка при обработке пользователя {user.user_id}: {e}")




async def check_user_status(user):
    """Проверяет, нужно ли отправлять уведомление пользователю"""
    try:
        # Проверяем наличие необходимых атрибутов
        if not hasattr(user, 'notifications_sent') or not hasattr(user, 'data_create_at'):
            print("У пользователя отсутствуют необходимые атрибуты")
            return False


        # Парсим дату создания
        #отрезаем времененую зону
        naive_date_str = user.data_create_at.split('+')[0].split('Z')[0]

        create_date = datetime.fromisoformat(naive_date_str)
        now = datetime.now()
        diff = now - create_date

        # Если нет уведомлений, можно отправлять
        if not user.notifications_sent:
            return False

        # Проверяем каждое уведомление
        for notification in user.notifications_sent:
            print(f"объект в цикле: {notification}")
            # Пропускаем уже отправленные
            if notification['status'] != 'pending' or notification['sent_at'] is not None:
                continue

            notification_type = notification['type']
            print("срез времени", diff, timedelta(minutes=1),diff >= timedelta(hours=1))
            if notification_type == '1h' and diff >= timedelta(minutes=1):
                await send_status(user.user_id, notification_type)
                return True

            elif notification_type == '1d' and diff >= timedelta(days=1):
                await send_status(user.user_id, notification_type)
                return True

            elif notification_type == '2d' and diff >= timedelta(days=2):
                await send_status(user.user_id, notification_type)
                return True

            elif notification_type == '3d' and diff >= timedelta(days=3):
                await send_status(user.user_id, notification_type)
                return True

        # Если не нашли подходящих уведомлений для отправки
        return False

    except ValueError as e:
        print(f"Ошибка формата даты: {e}")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return False


async def send_status(id_user, type):
    client = ApiService()
    await client.send_status({
        'id': id_user,
        'type': type,
        'status': 'sent',
        'sent_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


def create_users_from_response(response: dict) -> list[User]:

    users = []

    # Проверка корректности входных данных
    if not response or not isinstance(response.get('users'), list):
        print("Ошибка: неверный формат ответа. Ожидается словарь с ключом 'users', содержащим список")
        return users

    for user_data in response['users']:
        try:
            # Создаем новый объект User
            user = User()

            user.id = user_data.get('id')
            user.user_id = int(user_data.get('userId', 0))  # преобразуем в int
            user.first_name = user_data.get('firstName')
            user.last_name = user_data.get('lastName')
            user.name = user_data.get('name')
            user.phone = user_data.get('phone')
            user.referral_id = user_data.get('referralId')

            user.subscribe_to_group = bool(user_data.get('subscribeToGroup', False))
            user.giving_gift = bool(user_data.get('givingGift', False))

            if 'dataCreateAt' in user_data:
                user.data_create_at = user_data['dataCreateAt']

            # Обрабатываем уведомления
            notifications = user_data.get('notificationsSent', [])

            if notifications and isinstance(notifications, list):
                user.notifications_sent = notifications

            users.append(user)

        except Exception as e:
            print(f"Ошибка при создании пользователя из данных {user_data}: {str(e)}")
            continue

    return users