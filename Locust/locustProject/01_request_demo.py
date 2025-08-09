import requests

class HelloInterface:
    def __init__(self):
        self.host = "http://127.0.0.1:5000"

    def send_request(self):
        return requests.get(self.host + "/hello").json()

    def send_world(self):
        return requests.get(self.host + "/world").json()


if __name__ == '__main__':
    hello_interface = HelloInterface()
    print(hello_interface.send_request())