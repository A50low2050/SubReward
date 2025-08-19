from typing import Any, Dict
from bot.models.user import User
from config.settings import ApiRequest
from utils.factories.request_factory import RequestFactory


class NewMemberRequestFactory(RequestFactory):
    def create_request(self, payload: User) -> ApiRequest:
        return ApiRequest("POST", "/user/create", payload.to_dict())

class UpdateUserRequestFactory(RequestFactory):
    def create_request(self, payload: User) -> ApiRequest:
        return ApiRequest("PATCH", "/user/update", payload.to_dict())

class SendStatusRequestFactory(RequestFactory):
    def create_request(self, payload: Dict[str, Any]) -> ApiRequest:
        return ApiRequest("POST", "/user/update-status", payload)

class GetMemberRequestFactory(RequestFactory):
    def create_request(self, payload: Dict[str, Any] = None) -> ApiRequest:
        return ApiRequest("GET", "/user/get/", payload or {})

class GetNonSubscribedUsersFactory(RequestFactory):
    def create_request(self, payload: Any = None) -> ApiRequest:
        return ApiRequest("GET", "/user/non_subscribed_users")

class GetUsersGiftFactory(RequestFactory):
    def create_request(self, payload: Any = None) -> ApiRequest:
        return ApiRequest("GET", "/user/gift")
