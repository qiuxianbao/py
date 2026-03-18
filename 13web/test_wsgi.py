# Web Server Gateway Interface
from wsgiref.simple_server import make_server


def application(environ, start_response):
    # 输出
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


def test_server():
    # 创建一个服务器，IP地址为空，端口是8080
    # 处理函数是application:
    httpd = make_server('', 8080, application)
    print('Serving HTTP on port 8080...')
    # 开始监听HTTP请求:
    httpd.serve_forever()


def _main():
    test_server()


if __name__ == '__main__':
    _main()
