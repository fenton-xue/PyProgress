from time import sleep
from locust import HttpUser, task


class HelloInterface(HttpUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host = "http://uat.3plglobal.orsd.tech"
        self.payload = {
            "username": "kongxin-meiguokehu02",
            "password": "@usmeiguo002"
        }

    @task
    def send_request(self):
        sleep(5)
        # return self.client.post(self.host + "/3plapi/getToken", json=self.payload).json()

        response = self.client.post(self.host + "/3plapi/getToken", json=self.payload)
        print(response.json())
        return response.json()
