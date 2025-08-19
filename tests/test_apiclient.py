from unittest.mock import MagicMock
import pytest
from service.ApiClient import ApiService
from utils.factories.user_request_factories import NewMemberRequestFactory


@pytest.fixture
def api_client():
    return ApiService()

@pytest.mark.asyncio
async def test_send_request_new_member(monkeypatch, api_client):
    user = MagicMock()
    user.to_dict.return_value = {"id": 123, "name": "Test User"}

    factory = NewMemberRequestFactory()

    # фейковый ответ
    fake_response = MagicMock()
    fake_response.status_code = 201
    fake_response.json.return_value = {"status": "ok"}

    # мок клиента (имитируем ApiClient)
    mock_api_client = MagicMock()
    mock_api_client.post.return_value = fake_response

    # подменяем _new_connection, чтобы вернуть мок
    monkeypatch.setattr(api_client, "_new_connection", lambda: mock_api_client)

    # --- Act ---
    response = await api_client.send_request(factory, user)

    # --- Assert ---
    mock_api_client.post.assert_called_once_with(
        "/user/create",
        data={"id": 123, "name": "Test User"}
    )
    assert isinstance(response, MagicMock)  # response это наш fake_response
    assert response.status_code == 201
    assert response.json() == {"status": "ok"}
