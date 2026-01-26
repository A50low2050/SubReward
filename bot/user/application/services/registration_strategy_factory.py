from bot.user.application.services.registration_strategy import (
    RegistrationStrategy,
    GuestRegistrationStrategy,
    MatrixRegistrationStrategy,
)

class RegistrationStrategyFactory:
    @staticmethod
    def get_strategy(message_text: str) -> RegistrationStrategy:
        if not message_text:
            return GuestRegistrationStrategy()

        command_parts = message_text.split()
        command = command_parts[0]

        if command == '/start':
            if len(command_parts) > 1:
                return MatrixRegistrationStrategy()
            return GuestRegistrationStrategy()
        elif command == '/get_referral':
            return MatrixRegistrationStrategy()

        return GuestRegistrationStrategy()
