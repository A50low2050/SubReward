from telegram.constants import ParseMode
from bot.messages.messages import bonus_message
from bot.models.user import User
from service.ApiClient import ApiService


async def giving_gift(app):
    client = ApiService()
    print(f"получаем юзера для проверки подарка")

    users = create_users_from_response(await client.get_users_gift())

    for user in users:

        await app.bot.send_message(
            chat_id=user.user_id,
            text=bonus_message(),
            parse_mode=ParseMode.HTML,
        )

        user.giving_gift = True
        print(user.to_dict())
        await client.update_user(user)

    print("Выполняю задачу...")  # Ваш код здесь


def create_users_from_response(response: dict) -> list[User]:
    users = []

    # Проверяем, что ответ содержит ключ 'users' и это список
    if not isinstance(response.get('users'), list):
        return users

    for user_data in response['users']:
        print(f"парсим данные: {user_data}")
        try:
            # Создаем объект User, преобразуя типы при необходимости
            user = User(
                id=user_data.get('id'),
                user_id=user_data.get('userId'),
                name=user_data.get('name'),
                last_name=user_data.get('lastName'),
                first_name=user_data.get('firstName'),
                phone=user_data.get('phone'),
                referral_id=user_data.get('referralId'),
                giving_gift=user_data.get('givingGift'),
                subscribe_to_group=bool(user_data.get('subscribeToGroup', False)),
                data_create_at=user_data.get('dataCreateAt', ''),
                notifications_sent=user_data.get('notificationsSent', []),
            )
            print(f"смапленные данные: {user.to_dict()}")
            users.append(user)

        except Exception as e:
            # Логируем ошибку, но продолжаем обработку других пользователей
            print(f"Error creating user from data {user_data}: {str(e)}")

    return users
