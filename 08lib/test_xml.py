# DOM vs SAX
# Document Object Model（文档对象模型）
# Simple API for XML（XML 简单应用程序接口）
from pyexpat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


def test_xml_parse():
    xml = r'''<?xml version="1.0"?>
    <ol>
     <li><a href="/python">Python</a></li>
     <li><a href="/ruby">Ruby</a></li>
    </ol>
    '''

    handler = DefaultSaxHandler()

    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data

    parser.Parse(xml)

def _main():
    test_xml_parse()


if __name__ == '__main__':
    _main()
