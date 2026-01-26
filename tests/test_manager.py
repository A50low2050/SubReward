from unittest.mock import Mock

from bot.message_manager.manager import ProcessMessageManager


class TestManagerMessage:
    """Тесты для класса ManagerMessage"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.manager = ProcessMessageManager()

    def test_register_command_handler(self):
        """Тест регистрации обработчика команды"""
        mock_handler = Mock()
        mock_handler.__name__ = "test_command_handler"

        self.manager.register_handler('command', mock_handler, command_name='test')

        assert 'command' in self.manager.handlers
        assert 'test' in self.manager.handlers['command']
        assert self.manager.handlers['command']['test'] == mock_handler

    def test_register_default_handler(self):
        """Тест регистрации обработчика по умолчанию"""
        mock_handler = Mock()
        mock_handler.__name__ = "test_default_handler"

        self.manager.register_handler('text', mock_handler)

        assert 'text' in self.manager.handlers
        assert 'default' in self.manager.handlers['text']
        assert self.manager.handlers['text']['default'] == mock_handler

    def test_register_multiple_handlers_same_type(self):
        """Тест регистрации нескольких обработчиков одного типа"""
        handler1 = Mock()
        handler1.__name__ = "handler1"
        handler2 = Mock()
        handler2.__name__ = "handler2"

        self.manager.register_handler('command', handler1, command_name='start')
        self.manager.register_handler('command', handler2, command_name='help')

        assert len(self.manager.handlers['command']) == 2
        assert self.manager.handlers['command']['start'] == handler1
        assert self.manager.handlers['command']['help'] == handler2

    def test_register_multiple_types(self):
        """Тест регистрации обработчиков разных типов"""
        command_handler = Mock()
        command_handler.__name__ = "cmd_handler"
        text_handler = Mock()
        text_handler.__name__ = "txt_handler"

        self.manager.register_handler('command', command_handler, command_name='start')
        self.manager.register_handler('text', text_handler)

        assert 'command' in self.manager.handlers
        assert 'text' in self.manager.handlers
        assert self.manager.handlers['command']['start'] == command_handler
        assert self.manager.handlers['text']['default'] == text_handler


def test_integration_with_real_functions():
    """Интеграционный тест с реальными функциями из примера"""

    async def command_start(update, context, data):
        pass

    async def message_handler(update, context, data):
        pass

    manager = ProcessMessageManager()

    manager.register_handler('command', command_start, command_name='start')
    manager.register_handler('text', message_handler)

    assert 'command' in manager.handlers
    assert 'text' in manager.handlers
    assert manager.handlers['command']['start'] == command_start
    assert manager.handlers['text']['default'] == message_handler

    assert manager.handlers['command']['start'].__name__ == 'command_start'
    assert manager.handlers['text']['default'].__name__ == 'message_handler'