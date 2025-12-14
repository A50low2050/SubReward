import httpx
from response.response_bot_factory import Response

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client()

    def get(self, endpoint: str, params: dict = None) -> Response:
        url = self.base_url + endpoint
        try:
            response = self.client.get(url, params=params)
            response.raise_for_status()
            json_data = response.json()
            status = json_data.get("status", "success")
            error = json_data.get("error")
            data = json_data.get("data")

        except Exception as error:
            raise error

        return Response(
            status=status,
            error=error,
            data=data,
            endpoint=endpoint,
            payload=params
        )

    def post(self, endpoint: str, data: dict = None) -> Response:
        url = self.base_url + endpoint
        try:
            response = self.client.post(url, json=data)
            response.raise_for_status()
            json_data = response.json()
            status = json_data.get("status", "success")
            error = json_data.get("error")
            resp_data = json_data.get("data")

        except Exception as error:
            raise error

        return Response(
            status=status,
            error=error,
            data=resp_data,
            endpoint=endpoint,
            payload=data
        )

    def close(self):
        self.client.close()
