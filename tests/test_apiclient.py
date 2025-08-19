from unittest.mock import MagicMock
import pytest
from config.settings import ApiRequest
from service.ApiClient import ApiService, RequestFactory


@pytest.fixture
def api_client():
    return ApiService()

@pytest.mark.asyncio
async def test_send_request_new_member(monkeypatch):
    user = MagicMock()
    user.to_dict.return_value = {"id": 123, "name": "Test User"}

    factory = RequestFactory()
    api_client = ApiService()

    request = factory.create_request("new_member", user)
    assert isinstance(request, ApiRequest)
    assert request.method == "POST"
    assert request.endpoint == "/user/create"
    assert request.data == {"id": 123, "name": "Test User"}

    fake_response = MagicMock()
    fake_response.status_code = 201
    fake_response.json.return_value = {"status": "ok"}

    mock_client = MagicMock()
    mock_client.post.return_value = fake_response

    monkeypatch.setattr(api_client, "_new_connection", lambda: mock_client)

    response = await api_client.send_request(request)

    mock_client.post.assert_called_once_with("/user/create", data={"id": 123, "name": "Test User"})
    assert response.status_code == 201
    assert response.json() == {"status": "ok"}
