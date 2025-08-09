from locust import HttpUser, task
import requests


# 1.继承HttpUser类，用于定义用户行为，让locust执行时能认识到该类
class HelloInterface(HttpUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host = "http://127.0.0.1:5000"

    # 2.task装饰器告诉locust，我是一个任务，你来执行我
    @task
    def send_hello(self):
        # return requests.get(self.host + "/hello").json()
        return self.client.get(self.host + "/hello").json()
