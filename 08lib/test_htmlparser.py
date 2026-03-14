from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # 开始标签
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        # 结束标签
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        # 自闭合标签
        print('<%s/>' % tag)

    def handle_data(self, data):
        # 文本内容
        print(data)

    def handle_comment(self, data):
        # 注释
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        # handle_entityref，比如&nbsp;, &lt;, &copy;
        print('&%s;' % name)

    def handle_charref(self, name):
        # 数字字符，比如&#65;, &#x41;
        print('&#%s;' % name)


def test_parser():
    parser = MyHTMLParser()

    # 将 HTML 字符串喂给解析器
    # 解析器会逐步处理并调用相应的回调方法
    parser.feed('''<html>
    <head></head>
    <body>
        <!-- test html parser -->
        <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
    </body></html>''')


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':  # 只处理 <a> 标签
            for name, value in attrs:
                if name == 'href':
                    self.links.append(value)
                    print(f'找到链接：{value}')


def test_link_extractor():
    parser = LinkExtractor()
    parser.feed('<html><body><a href="http://example.com">Link</a></body></html>')

    print(parser.links)  # ['http://example.com']


def _main():
    test_parser()
    # test_link_extractor()


if __name__ == '__main__':
    _main()
