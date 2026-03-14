import requests


def test_get():
    r = requests.get('https://www.baidu.com', timeout=2.5)
    print(r.url)  # 实际请求的URL
    print(r.encoding)

    print(r.status_code)
    print(r.headers)
    print(r.cookies)


    # print(r.text)
    # print(r.content)  # 获得 bytes 对象

    # print(r.json())   # 提取 json 对象


    # 构建 请求参数
    r = requests.get('https://www.baidu.com/search', params={'q': 'python', 'cat': '1001'})

    # 构建 请求头
    r = requests.get('https://www.baidu.com/',
                     headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

    # 构建 cookie
    cs = {'token': '12345', 'status': 'working'}
    r = requests.get('https://www.baidu.com', cookies=cs)


def test_post():
    # 默认使用 application/x-www-form-urlencoded 对POST数据编码
    r = requests.post('https://accounts.douban.com/login',
                      data={'form_email': 'abc@example.com', 'form_password': '123456'})

    # json请求体
    r = requests.post('', json={'key': 'value'})  # 内部自动序列化为JSON


def _main():
    test_get()
    # test_post()


if __name__ == '__main__':
    _main()
