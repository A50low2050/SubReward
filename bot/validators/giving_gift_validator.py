

class GiftValidator():
    def validate(self, user):
        if user.gifts_received == 3:
            return True, "🎁 Лимит подарков исчерпан"
        return True, ""