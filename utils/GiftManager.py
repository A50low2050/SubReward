from bot.messages import messages
from bot.models.user import User


class GiftManager:
    def __init__(self):
        self.gift_messages = messages

    def send_gift(self, user_data: User):
        if self._check_eligibility(User.id):
            self.deliver_gift(User.id, self._get_gift_type(User.id))
            return True
        return False

    def _check_eligibility(self, user_id):
        if not user_id:
            return False
        return True

    def _get_gift_type(self, user_id):

        return ['type:promo']

    def deliver_gift(self, user_id, gift_type):

        pass
