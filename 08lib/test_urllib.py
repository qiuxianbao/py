import json
from urllib import request, parse


def test_request():
    # 模拟iPhone去请求
    req = request.Request('https://blog.csdn.net/u010773514')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0Mobile/10A5376e Safari/8536.25')

    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
    pass


def test_get():
    with request.urlopen('https://blog.csdn.net/u010773514') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))


def test_post():
    print('Login to csdn...')

    # user = input('user: ')
    # passwd = input('Password: ')

    user = 'root'
    passwd = '123456'

    # login_data = parse.urlencode([
    #     ('userIdentification', user),
    #     ('pwdOrVerifyCode', passwd),
    #     ('loginType', '1'),
    #     ('webUmidToken', ""),
    #     ('uaToken', ''),
    #     ('agreedPrivacyPolicy', 0),
    # ])

    login_data = {
        'userIdentification': user,
        'pwdOrVerifyCode': passwd,
        'loginType': '1',
        'webUmidToken': '',
        'uaToken': '',
        'agreedPrivacyPolicy': 0,
    }

    login_data = json.dumps(login_data)

    req = request.Request('https://passport.csdn.net/v1/register/pc/login/doLogin')
    req.add_header('Content-Type', 'application/json')
    # 标识请求的来源域名，主要用于 CORS（跨域资源共享）验证，服务器会根据这个判断是否允许跨域请
    req.add_header('Origin', 'https://passport.csdn.net')
    # 表示当前请求是从哪个页面跳转过来的，服务器可以用来做来源验证、防盗链
    req.add_header('Referer', 'https://passport.csdn.net/login?code=applets')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    req.add_header('Accept', 'application/json, text/plain, */*')
    req.add_header('Accept-Encoding', 'gzip, deflate, br')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')
    req.add_header('Connection', 'keep-alive')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


def _main():
    # test_get()
    # test_request()
    test_post()


if __name__ == '__main__':
    _main()
