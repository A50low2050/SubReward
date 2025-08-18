import json
from datetime import datetime
from typing import Optional


class User:
    def __init__(
            self,
            id: Optional[int] = None,
            user_id: int = 0,
            name: Optional[str] = None,
            last_name: Optional[str] = None,
            first_name: Optional[str] = None,
            phone: Optional[str] = None,
            referral_id: Optional[int] = None,
            giving_gift: bool = False,
            subscribe_to_group: bool = False,
            data_create_at: str = '',
            notifications_sent=None
    ):
        self._id = id
        self._user_id = user_id
        self._name = name
        self._last_name = last_name
        self._first_name = first_name
        self._phone = phone
        self._referral_id = referral_id
        self._giving_gift = giving_gift
        self._subscribe_to_group = subscribe_to_group
        self._data_create_at = data_create_at or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._notifications_sent = notifications_sent

    # Свойства и сеттеры для каждого поля

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        # Можно добавить валидацию номера телефона здесь.
        self._phone = value

    @property
    def referral_id(self):
        return self._referral_id

    @referral_id.setter
    def referral_id(self, value):
        self._referral_id = value

    @property
    def giving_gift(self):
        return self._giving_gift

    @giving_gift.setter
    def giving_gift(self, value):
        if isinstance(value, bool):
            self._giving_gift = value
        else:
            self._giving_gift = bool(value)

    @property
    def subscribe_to_group(self):
        return self._subscribe_to_group

    @subscribe_to_group.setter
    def subscribe_to_group(self, value):
        if isinstance(value, bool):
            self._subscribe_to_group = value
        else:
            # Можно выбросить исключение или привести к bool.
            self._subscribe_to_group = bool(value)

    @property
    def data_create_at(self):
        return self._data_create_at

    @data_create_at.setter
    def data_create_at(self, value):
        # Можно добавить проверку формата даты.
        self._data_create_at = value

    @property
    def notifications_sent(self):
        return self._notifications_sent

    @notifications_sent.setter
    def notifications_sent(self, value):
        # Можно добавить проверку формата даты.
        self._notifications_sent = value
    # Метод для обновления из словаря (используя свойства)

    def update_from_dict(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        # Метод для сериализации в JSON (используя свойства)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'phone': self.phone,
            'referral_id': self.referral_id,
            'giving_gift': self.giving_gift,
            'subscribe_to_group': self.subscribe_to_group,
            'data_create_at': self.data_create_at,
            'notifications_sent': self.notifications_sent
        }
