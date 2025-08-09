### 一、项目结构

-- server
1. 被压服务使用flask编写，放在server层

-- locustProject
1. locust本身脚本

#### locust 常用的包
```python
from locust import HttpUser, task
```
1. HttpUser：继承HttpUser类，用于定义用户行为，让locust执行时能认识到该类
2. task： 定义用户行为
```python
    @task
    def send_hello(self):
        return requests.get(self.host + "/hello").json()

    @task
    def send_hello(self):
        return self.client.get(self.host + "/hello").json()
```
3. 上面一种，locust只是不停的发送请求，而无法获取到返回值，需要使用client


#### 启动locust
1. 在终端进入locustProject目录
2. 执行命令：locust -f locustfile.py 其中 locustfile.py 替换成文件路径
3. 如果有文件里有多个类，默认执行第一个类，可以在文件路径后，加空格，然后指定类名；可以写多个类，不写则默认执行全部类。其中类的数量和并发用户数要相等
4. 或者直接：locust 默认locustfile.py
5. 一种调试常用的启动方法，导入 run_single_user 包，然后在main()，执行run_single_user(类名)


#### locust Web
1. Number of users(peak concurrency) 并发用户数（峰值并发）
2. Spawn rate(users started/second) 生成率（用户启动速率/秒）
3. Host (e.g. http://example.com) 请求的域名
4. 当控制台输出 All users spawned ... 时，表明所有并发用户数都已经生成完毕

#### 管理端指标
- 常见的指标
  - QPS：1秒内请求数
  - RPS：1秒内响应数
  - TPS：1秒内事务数，例如访问home，请求一次home.html, home.css, home.js，那TPS是1，QPS就是3
  - RT：响应时间，浏览器开发者工具中的Time
  - 并发用户数：1秒内并发用户数
- Statistics 统计tab