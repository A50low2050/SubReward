from bot.models.user import User


class SubscriptionValidator():
    def validate(self, user: User) -> bool:
        if not user.subscribe_to_group:
            return False
        return True
