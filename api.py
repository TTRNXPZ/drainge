import httpx
import json 

BASE_URL = "https://sensor.sjp-gis.com/v1/sensor/test"
AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY3Rpb24iOiJub2l0ZnkiLCJpYXQiOjE3NDA0NzAwMzZ9.V56j-FyQ68GkOtwXdpeqcWD0SfDCbIz6yNral7WUTvM"

class SendAPI:
    def __init__(self, base_url=BASE_URL, token=AUTH_TOKEN):
        self.base_url = base_url
        self.headers = {"Authorization": token}

    async def send_api_request(self, data: dict) -> str:
        # print(f"Sending Data: {data}")  
        async with httpx.AsyncClient() as client:
            response = await client.post(self.base_url, json=data, headers=self.headers)
            # print(f"API Response Status: {response.status_code}")  
            return json.dumps(response.json(), ensure_ascii=False)
