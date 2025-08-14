from locust import HttpUser, task


class CartUser(HttpUser):

    host = "http://127.0.0.1:5000"

    # 每个用户启动时会执行一次, 后面不再执行
    def on_start(self):
        payload = {
            "username": 'abc',
            "password": '123'
        }
        self.client.post("/login", json=payload)

    @task
    def send_cart(self):
        self.client.post("/hello")

    # 每次每个用户结束都会执行一次, 后面不再执行
    def on_stop(self):
        self.client.post("/logout")
