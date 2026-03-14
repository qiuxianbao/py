"""
print_info 函数解析示例
演示 email 模块如何解析 MIME 邮件结构
"""
from email.parser import Parser
from email.utils import parseaddr
from nntplib import decode_header


def decode_str(s):
    """解码邮件头部的编码字符串"""
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    """猜测邮件的字符编码"""
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def print_info(msg, indent=0):
    """
    递归打印邮件信息
    
    参数:
        msg: Message 对象（可以是顶层邮件或 MIME 部分）
        indent: 缩进级别（用于显示层级结构）
    """
    # 第一层：打印邮件头部信息
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))

    # 判断是否为多部分邮件
    if msg.is_multipart():
        # === 多部分邮件处理 ===
        parts = msg.get_payload()  # 获取所有子部分
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s--------------------' % (' ' * indent))
            # 递归调用，处理每个子部分
            print_info(part, indent + 1)
    else:
        # === 单部分邮件处理 ===
        content_type = msg.get_content_type()
        
        if content_type == 'text/plain' or content_type == 'text/html':
            # 文本内容：解码并打印
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
                print('%sText: %s' % (' ' * indent, content + '...'))
            else:
                print('%sAttachment: %s' % (' ' * indent, content_type))
        else:
            # 其他类型（如图片、附件等）
            print('%sAttachment: %s' % (' ' * indent, content_type))


# ==================== 示例演示 ====================

if __name__ == '__main__':
    # ========== 示例 1: 简单纯文本邮件 ==========
    print("=" * 60)
    print("示例 1: 简单纯文本邮件")
    print("=" * 60)
    
    simple_email = """From: 张三 <zhangsan@example.com>
To: 李四 <lisi@example.com>
Subject: =?utf-8?b?5L2g5oiQ5ZC+5bi4?=
MIME-Version: 1.0
Content-Type: text/plain; charset="utf-8"

你好，这是一封测试邮件。
这是第二行内容。
"""
    
    msg1 = Parser().parsestr(simple_email)
    print_info(msg1)
    
    
    # ========== 示例 2: HTML 邮件 ==========
    print("\n" + "=" * 60)
    print("示例 2: HTML 邮件")
    print("=" * 60)
    
    html_email = """From: 系统管理员 <admin@example.com>
To: 用户 <user@example.com>
Subject: =?utf-8?b?55Sf54iX5ZC+5bi4?=
MIME-Version: 1.0
Content-Type: text/html; charset="utf-8"

<html>
<body>
<h1>欢迎</h1>
<p>这是一封<strong>HTML</strong>格式的邮件。</p>
<a href="http://example.com">点击这里</a>
</body>
</html>
"""
    
    msg2 = Parser().parsestr(html_email)
    print_info(msg2)
    
    
    # ========== 示例 3: 多部分邮件 (MIMEMultipart) ==========
    print("\n" + "=" * 60)
    print("示例 3: 多部分邮件（同时包含纯文本和 HTML）")
    print("=" * 60)
    
    multipart_email = """From: 王五 <wangwu@example.com>
To: 赵六 <zhaoliu@example.com>
Subject: =?utf-8?b?5Yqz5LiA5Yqz5YWo?=
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="boundary123456"

--boundary123456
Content-Type: text/plain; charset="utf-8"

你好！
这是纯文本版本的内容。
如果你的邮件客户端不支持 HTML，就会显示这个。

--boundary123456
Content-Type: text/html; charset="utf-8"

<html>
<body>
<h2>你好！</h2>
<p>这是 <b>HTML</b> 版本的内容。</p>
</body>
</html>

--boundary123456--
"""
    
    msg3 = Parser().parsestr(multipart_email)
    print_info(msg3)
    
    
    # ========== 示例 4: 带附件的邮件 ==========
    print("\n" + "=" * 60)
    print("示例 4: 带附件的邮件")
    print("=" * 60)
    
    attachment_email = """From: 同事 <colleague@company.com>
To: 我 <me@company.com>
Subject: =?utf-8?b?6KGM77yM5Lit5Zu95YiG5L+h5oGv5Lu2?=
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="attach789"

--attach789
Content-Type: text/plain; charset="utf-8"

请查看附件中的报告。

谢谢！

--attach789
Content-Type: application/pdf; name="report.pdf"
Content-Disposition: attachment; filename="report.pdf"
Content-Transfer-Encoding: base64

JVBERi0xLjQKJeLjz9MKMSAwIG9iago8PAovVHlwZSAvQ2F0YWxvZwovUGFnZXMgMiAwIFIKPj4K
ZW5kb2JqCjIgMCBvYmoKPDwKL1R5cGUgL1BhZ2VzCi9LaWRzIFszIDAgUl0KL0NvdW50IDEKPDwK
ZW5kb2JqCjMgMCBvYmoKPDwKL1R5cGUgL1BhZ2UKPj4KZW5kb2JqCnhyZWYKMCA0CnRyYWlsZXIK
PDwKL1NpemUgNAovUm9vdCAxIDAgUgo+PgpzdGFydHhyZWYKMTIzNAolJUVPRgo=

--attach789--
"""
    
    msg4 = Parser().parsestr(attachment_email)
    print_info(msg4)
