import math

from locust import HttpUser, task, LoadTestShape


class LoadUser(HttpUser):

    @task
    def send_hello(self):
        self.client.get("/hello")


class CustomLoadTest(LoadTestShape):

    # def tick(self):
    #     # 对tick()进行重写
    #     # 返回值是(number_of_users, spawn_rate)
    #     # 这个方法每秒钟都会被执行，所以可以动态的设置用户数量和用户生成速率
    #     print(f"当前执行时间: {self.get_run_time()}")
    #     print(f"当前用户总数: {self.get_current_user_count()}")
    #     return 10, 10

    rate = 10

    def tick(self):
        """
        每隔30s, 增长10个用户
        :return:
        """
        # if self.get_run_time() < 30:
        #     return 10, self.rate
        # if 30 <= self.get_run_time() < 60:
        #     return 20, self.rate
        # if 60 <= self.get_run_time() < 90:
        #     return 30, self.rate
        # return None

        # 可以寻找运行时间和用户数量之间的关系，简化代码
        # 1 -> 1/30 向上取整 1 * 10 = 10
        # 2 -> 2/30 向上取整 1 * 10 = 10
        # ...
        # 31 -> 31/30 向上取整 2 * 10 = 20
        # ...
        # 61 -> 61/30 向上取整 3 * 10 = 30
        user_num = math.ceil(self.get_run_time() / 30) * self.rate
        return user_num, self.rate
