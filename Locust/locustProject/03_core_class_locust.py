from time import sleep
from locust import HttpUser, task, constant, between


class CoreUser(HttpUser):

    host = "http://127.0.0.1:5000"

    # wait_time = constant(1)
    # wait_time = lambda instance: 2
    wait_time = between(3, 5)

    @task
    def send_hello(self):
        sleep(5)
        self.client.get("/hello")
