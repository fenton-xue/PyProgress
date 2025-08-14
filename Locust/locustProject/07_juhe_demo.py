import random

from locust import HttpUser, task, tag


class CalUser(HttpUser):

    @task
    def send_cal(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        params = {
            "num1": num1,
            "num2": num2
        }
        with self.client.get("/cal", params=params, catch_response=True, name='cal') as response:
            if response.text == str(num1 + num2):
                response.success()
            else:
                response.failure("计算错误")