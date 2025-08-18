from bot.models.user import User

class UserValidator:
    @staticmethod
    def validate(user: User) -> bool:

        return all(user_data.get(field) for field in required_fields)
