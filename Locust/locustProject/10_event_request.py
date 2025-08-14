from locust import HttpUser, task, events


class EventRequestUser(HttpUser):

    @task
    def send_event_request(self):
        self.client.get("/hello")

@events.request.add_listener
def request_complete(request_type, name, response_time, response_length, **kwargs):
    print(f"request_type: {request_type}")
