from locust import HttpUser, task


class PcUser(HttpUser):

    weight = 1

    @task
    def send_hello(self):
        headers = {
            "User-Agent": "Pc"
        }
        self.client.get("/hello", headers=headers)


class MobileUser(HttpUser):

    weight = 3

    @task
    def send_hello(self):
        headers = {
            "User-Agent": "Mobile"
        }
        self.client.get("/hello", headers=headers)
