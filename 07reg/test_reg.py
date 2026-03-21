"""
正则

^ 行的开头；在 [^...] 内，则表示取反/非，示例 [^"]表示除了双引号外的字符
$ 行的结束

直接给出字符，就是精确匹配
\d 可以匹配一个数字
\w 可以匹配一个字母或数字
\s 可以匹配一个空格（也包括Tab等空白符）
'\' 转义，示例：\-

. 可以匹配任意字符
* 表示任意个字符（包括0个）
+ 表示至少一个
? 表示0个或1个字符
{n} 表示n个字符，用 {n,m} 表示n-m个字符

| 或，示例：A|B, 可以匹配A或B
[] 表示范围，示例 [0-9a-zA-Z\_] 可以匹配一个数字、字母或者下划线

() 表示组

"""
import re


def test_match():
    s1 = 'ABC\\-001'  # Python的字符串, 对应的正则表达式字符串变成 'ABC\-001'
    s2 = r'ABC\-001'  # r'' 表示 '' 内部的字符串默认不转义
    # print(s1 == s2)  # True

    # <re.Match object; span=(0, 9), match='010-12345'>
    print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

    # None
    print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))


    # 贪婪匹配，能多匹配就多匹配
    print(re.match(r'^(\d+)(0*)$', '102300').groups())
    # 非贪婪匹配，能少匹配就少匹配
    print(re.match(r'^(\d+?)(0*)$', '102300').groups())


def test_split():
    """
    输出是 ['a', 'b', '', '', 'c']

    分析：
    当您使用 .split(' ') 按单个空格分割时，Python 会:
    遇到第一个空格 → 分割出 'a'
    遇到第二个空格 → 分割出 'b'
    遇到第三个空格 → 分割出 ''(空字符串)
    遇到第四个空格 → 再分割出 ''(空字符串)
    最后剩下 'c'
    :return:
    """
    print('a b   c'.split(' '))
    # ['a', 'b', 'c']
    print('a b   c'.split())

    # 用户输入了一组标签，可以使用正则表达式来把不规范的输入转化成正确的数组
    # 空格
    print(re.split(r'\s+', 'a b c'))
    # 空格+,
    print(re.split(r'[\s\,]+', 'a,b, c d'))
    # 空格,;
    print(re.split(r'[\s\,\;]+', 'a,b;; c d'))


def test_group():

    """
    分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码

    如果正则表达式中定义了组，就可以在 Match 对象上用 group() 方法提取出子串来
    :return:
    """
    match = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

    # ('010', '12345')
    print(match.groups())

    # 010-12345
    print(match.group())
    print(match.group(0))

    # 010
    print(match.group(1))
    # 12345
    print(match.group(2))



def test_compile():
    """
    如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式
    编译正则表达式，可以提高性能
    :return:
    """
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    print(re_telephone.match('010-12345').groups())
    print(re_telephone.match('010-8086').groups())


def _main():
    # test_match()
    # test_split()
    # test_group()
    test_compile()


if __name__ == '__main__':
    _main()
