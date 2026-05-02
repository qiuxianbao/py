"""
# 架构模型
Flask - 同步 WSGI 框架
基于同步 I/O，每个请求一个线程/进程
阻塞式处理，【适合 CPU 密集型任务】
使用 Werkzeug WSGI 服务器

aiohttp - 异步 asyncio 框架
基于异步 I/O，单线程事件循环
非阻塞处理，【适合 I/O 密集型任务】
内置异步服务

# 性能特点
Falsk
并发需要多线程/多进程
高并发下资源消耗

aiohttp
单线程处理数千并发连接
I/O 密集型场景性能优异

# 使用场景
Flask 适合：
    传统 Web 应用
    RESTful API（简单场景）
    需要大量同步库的场景
    快速原型开发
    CPU 密集型任务
aiohttp 适合：
    高并发 API 服务
    WebSocket 实时通信
    微服务架构
    爬虫和数据采集
    需要调用多个外部 API 的场

# 框架

                    Python Web 框架对比
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
    ┌───▼────┐      ┌────▼─────┐     ┌───▼────┐
    │ Flask  │      │ FastAPI  │     │ aiohttp│
    └───┬────┘      └────┬─────┘     └───┬────┘
        │                │               │
        ├─ 同步 WSGI     ├─ 异步 ASGI    ├─ 异步 asyncio
        ├─ 多线程/进程   ├─ async/await  ├─ 事件循环
        ├─ 阻塞式 I/O    ├─ 非阻塞 I/O   ├─ 非阻塞 I/O
        ├─ Werkzeug      ├─ Starlette    ├─ 内置服务器
        │                │               │
        ├─ CPU 密集型    ├─ 高性能 API   ├─ 高并发 I/O
        ├─ 传统 Web     ├─ 微服务       ├─ WebSocket
        ├─ 快速原型      ├─ 自动文档     ├─ 数据采集
        │                │               │
        └─ 类似：        └─ 类似：       └─ 类似：
           Spark Java      Spring         Netty
                           WebFlux

Java 开发者理解指南：
  Flask    → 轻量级 Servlet + Tomcat
  FastAPI  → Spring Boot + Swagger + Validation（适用于边缘部署、微服务、轻量API）
  Django  → Spring Boot全家桶（ORM + 后台、安全、模板、授权内置），开箱即用（适用于带管理后台、用户权限的完整系统）内置后台
  aiohttp  → Netty + Reactor 模式

"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
 <p><input name="username"></p>
 <p><input name="password" type="password"></p>
 <p><button type="submit">Sign In</button></p>
 </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
