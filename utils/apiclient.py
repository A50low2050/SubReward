import httpx

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client()

    def get(self, endpoint: str, params: dict = None) -> dict:
        """
        Отправляет GET-запрос к API.
        :param endpoint: путь к ресурсу (например, "/api/data")
        :param params: словарь параметров запроса
        :return: ответ в виде словаря (распарсенный JSON)
        """
        url = self.base_url + endpoint
        response = self.client.get(url, params=params)
        print("Ответ сервера:", response.text)
        response.raise_for_status()  # выбросит исключение при ошибке
        return response.json()

    def post(self, endpoint: str, data: dict = None) -> dict:
        """
        Отправляет POST-запрос с JSON-данными.
        :param endpoint: путь к ресурсу
        :param data: словарь данных для отправки
        :return: ответ в виде словаря (распарсенный JSON)
        """
        url = self.base_url + endpoint
        response = self.client.post(url, json=data)
        print("Ответ сервера:", response.text)
        response.raise_for_status()
        return response.json()

    def close(self):
        """Закрывает соединение"""
        self.client.close()
