import pytest
from api_client.ApiClient import ApiService
from api_client.TelegramBotRequest import TelegramBotRequest
from api_client.builders import TelegramBotRequestBuilder


@pytest.fixture
def api_client():
    return ApiService()


def test_builder_creates_valid_request():
    builder = TelegramBotRequestBuilder()
    request = (
        builder
        .set_method("POST")
        .set_endpoint("/update_user")
        .add_param("user_id", 123)
        .add_param("name", "Tema")
        .build()
    )

    assert isinstance(request, TelegramBotRequest)
    assert request.get_method() == "POST"
    assert request.get_endpoint() == "/update_user"
    assert request.get_payload() == {"user_id": 123, "name": "Tema"}