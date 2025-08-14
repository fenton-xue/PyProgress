from locust import HttpUser, task, tag


class TagUser(HttpUser):

    @tag("hello")
    @task
    def hello(self):
        self.client.post("/hello")

    @tag("world")
    @task
    def world(self):
        self.client.post("/world")


