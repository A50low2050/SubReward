import pytest
from api_client.ApiClient import ApiService
from api_client.telegram_bot_factory import TelegramBotRequestFactory
from bot.models.user import User


@pytest.fixture
def api_client():
    return ApiService()

@pytest.mark.asyncio
async def test_send_request_new_member(api_client):
    user = User(
        id = 1
    )

    response = await api_client.send_request(TelegramBotRequestFactory.create_member(user.to_dict()))

    # response = await api_client.send_request(TelegramBotRequestFactory.create_member_oz(user.to_dict()))
