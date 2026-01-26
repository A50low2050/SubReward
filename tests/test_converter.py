import unittest
from unittest.mock import Mock
import pytest
from telegram import Message, User
from bot.message_manager.manager import MessageConverter, ManagerMessage
from bot.message_manager.models import MessageInputDTO


class TestMessageConverterConvert(unittest.TestCase):
    """Тесты для метода MessageConverter.convert()"""

    def setUp(self):
        self.converter = MessageConverter()

    def create_mock_message(self, user_id=123, chat_id=456, message_id=789, text="Test message"):
        """Создает mock объект Message с заданными параметрами"""
        mock_user = Mock(spec=User)
        mock_user.id = user_id
        mock_user.username = "test_user"

        mock_message = Mock(spec=Message)
        mock_message.from_user = mock_user
        mock_message.chat_id = chat_id
        mock_message.message_id = message_id
        mock_message.text = text

        return mock_message

    def test_convert_basic_message(self):
        """Тест преобразования базового сообщения"""

        mock_message = self.create_mock_message()

        result = self.converter.convert(mock_message)

        self.assertIsInstance(result, MessageInputDTO)
        self.assertEqual(result.user_id, 123)
        self.assertEqual(result.message_id, 789)
        self.assertEqual(result.chat_id, 456)
        self.assertEqual(result.text, "Test message")
        self.assertEqual(result.type, "text")
        self.assertIsNone(result.command)

class TestMessageType:

    @pytest.mark.parametrize("message_text, expected_type", [
        ("/start", "command"),
        ("/help", "command"),
        ("/command_with_args arg1 arg2", "command"),
        ("/", "command"),
        ("message", "text"),



    ])
    def test_determine_message_type(self, message_text, expected_type):
        converter = MessageConverter()
        result = converter._determine_message_type(message_text)
        assert result == expected_type


class TestsCommand:
    """Тесты для статического метода _get_command"""

    @pytest.mark.parametrize(
        "command, expected_command", [
            ("/start", "start"),
            ("/help", "help"),
            ("/long_command_name", "long_command_name"),
        ]
    )

    def test_get_commands(self, command, expected_command):
        """Тест валидных команд"""

        result = MessageConverter._get_command(command)
        assert result == expected_command

    def test_none_command(self):
        message_text = ""

        result = MessageConverter._get_command(message_text)
        assert result is None

