import unittest
from unittest.mock import Mock, MagicMock, patch
from telegram import Message
from bot.message_manager.validators import MessageValidator


class TestMessageValidatorSimple(unittest.TestCase):
    """Упрощенные тесты для MessageValidator"""

    def setUp(self):
        self.validator = MessageValidator()

    def test_valid_message_returns_true(self):
        mock_message = Mock(spec=Message)
        mock_message.text = "Сообщение"
        result = self.validator.validate(mock_message)
        self.assertTrue(result)

    def test_empty_message(self):
        mock_message = None
        with self.assertRaises(ValueError) as context:
            self.validator.validate(mock_message)

        self.assertEqual(str(context.exception), "Параметр message не может быть пустым")


    def test_empty_message_text(self):
        mock_message = Mock(spec=Message)
        mock_message.text = None
        with self.assertRaises(ValueError) as context:
            self.validator.validate(mock_message)

        self.assertEqual(str(context.exception), "Текст не должен быть пустым")


if __name__ == '__main__':
    unittest.main()