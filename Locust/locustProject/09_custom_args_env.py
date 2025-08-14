from locust import HttpUser, task, events

class CustomArgsUser(HttpUser):

    @task
    def send_hello(self):
        if self.environment.parsed_options.env == "test":
            pass
        else:
            self.client.get("/hello")

# Web 启动页面, 也会增加一个对应的参数
@events.init_command_line_parser.add_listener()
def init(parser):
    parser.add_argument("--env", type=str, default="test", help="环境信息")