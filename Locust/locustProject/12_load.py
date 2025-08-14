import math

from locust import HttpUser, task, LoadTestShape


class LoadUser(HttpUser):

    @task
    def send_hello(self):
        self.client.get("/hello")


class CustomLoadTest(LoadTestShape):

    def tick(self):
        # if self.get_run_time() < 20:
        #     return 10, 10
        # if self.get_run_time() < 50:
        #     return 100, 50
        # if self.get_run_time() < 80:
        #     return 1000, 300
        # if self.get_run_time() < 110:
        #     # 这里从1000降, 是做减法
        #     return 500, 200
        # if self.get_run_time() < 140:
        #     return 100, 200
        # return None # 停止压测

        stages = [
            (20, 10, 10),
            (50, 100, 50),
            (80, 1000, 300),
            (110, 500, 200),
            (140, 100, 200)
        ]
        for stage in stages:
            if self.get_run_time() < stage[0]:
                return stage[1], stage[2]
            return None
