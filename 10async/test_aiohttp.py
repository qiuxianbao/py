"""
aiohttp 则是基于 asyncio 实现的HTTP框架


然后编写一个HTTP服务器，分别处理以下URL：
/ - 首页返回 Index Page ；
/{name} - 根据URL参数返回文本 Hello, {name}! 。
"""

from aiohttp import web


async def index(request):
    text = "<h1>Index Page</h1>"
    return web.Response(text=text, content_type="text/html")


async def hello(request):
    name = request.match_info.get("name", "World")
    text = f"<h1>Hello, {name}</h1>"
    return web.Response(text=text, content_type="text/html")


if __name__ == '__main__':
    app = web.Application()
    # 添加路由
    app.add_routes([web.get("/", index), web.get("/{name}", hello)])
    web.run_app(app)
