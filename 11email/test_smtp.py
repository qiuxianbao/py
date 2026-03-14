"""
# 电子邮件概念
1.电子邮件软件，我们称为 MUA：Mail User Agent——【邮件用户代理】，比如foxmail
2.Email从 MUA 发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent——【邮件传输代理】，就是那些Email服务提供商，比如网易、新浪等等
3.由 MTA 发送给对方邮件的MTA
4.MTA 接收到邮件之后，投递到邮件的最终目的地 MDA：Mail Delivery Agent——【邮件投递代理】

Email到达MDA后，就静静地某个服务器上，存放在某个文件或特殊的数据库里，我们将这个长期保存邮件的地方称之为电子邮箱。

# 一封邮件的生命周期：
发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

# 要编写程序来发送和接收邮件，本质上就是：
1. 编写MUA把邮件发到MTA
2. 编写MUA从MDA上收邮件

# 协议
发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol

收邮件时，MUA和MDA使用的协议有2种：
POP：Post Office Protocol，目前版本是3，俗称POP3；
IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件

说明：
特别注意，目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能
"""
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def test_plain():
    """
    纯文本
    :return:
    """
    # 输入Email地址和口令
    from_addr = input('From: ')
    password = input('Password: ')
    to_addr = input('To: ')  # 输入收件人地址
    smtp_server = input('SMTP server: ')  # 输入SMTP服务器地址

    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)  # 发件人
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)  # 收件人
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()  # 主题

    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.set_debuglevel(1)  # 可以打印出和SMTP服务器交互的所有信息
    server.login(from_addr, password)  # 登录

    # SMTP发送的是经过编码后的一大段文本
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def test_html():
    msg = MIMEText('<html><body><h1>Hello</h1>' +
                   '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
                   '</body></html>', 'html', 'utf-8')


def test_attach():
    # 输入Email地址和口令
    from_addr = input('From: ')
    to_addr = input('To: ')  # 输入收件人地址

    # 邮件对象
    msg = MIMEMultipart()
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

    # 邮件正文是 MIMEText
    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

    # 正文中包含图片，用cid:0来引用
    # msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    #                     '<p><img src="cid:0"></p>' +
    #                     '</body></html>', 'html', 'utf-8'))

    # 添加附件就是加上一个 MIMEBase，从本地读取一个图片
    with open('/Users/michael/Downloads/test.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型
        mime = MIMEBase('image', 'png', filename='test.png')
        # 加上必要的头信息
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')

        # 把附件的内容读进来
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart
        msg.attach(mime)


def test_alternative():
    """
    同时支持HTML和Plain格式

    解决：
    如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件
    :return:
    """
    msg = MIMEMultipart('alternative')

    # 知识点：... 是占位符
    msg['From'] = ...
    msg['To'] = ...
    msg['Subject'] = ...

    msg.attach(MIMEText('hello', 'plain', 'utf-8'))
    msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))


def test_tls():
    """
    Transport Layer Security
    :return:
    """
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    # 先创建SSL安全连接
    server.starttls()
    server.set_debuglevel(1)


def _main():
    test_plain()
    test_html()
    test_attach()
    test_alternative()
    test_tls()


if __name__ == '__main__':
    _main()
