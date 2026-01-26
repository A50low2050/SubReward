from bot.user.application.services.registration_strategy import (
    RegistrationStrategy,
    GuestRegistrationStrategy,
    MatrixRegistrationStrategy,
)

class RegistrationStrategyFactory:
    @staticmethod
    def get_strategy(message_text: str) -> RegistrationStrategy:
        if message_text and message_text.startswith('/start ref'):
            return MatrixRegistrationStrategy()
        return GuestRegistrationStrategy()
