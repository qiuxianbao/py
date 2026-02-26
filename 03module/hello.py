#!/usr/bin/env python3
# -*- coding: utf-8 -*-


' a test module '

__author__ = 'Michael'


"""
1.模块
任何模块代码的第一个字符串都被视为模块的文档注释
在Python中，一个.py文件就称之为一个模块（Module）
为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）

2.在 python交互模式下，通过 import 可以检查一个模块是否存在
当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错.
(llm) PS C:\VsCode\py\03module> python
Python 3.10.19 (main, Feb  3 2026, 22:48:33) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello

>>> hello.test
<function test at 0x000001CE0CA3F910>

>>> hello.test()
Hello, world!


3.默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在 sys 模块的 path 变量中
(llm) PS C:\VsCode\py\03module> python
Python 3.10.19 (main, Feb  3 2026, 22:48:33) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Users\\admin\\AppData\\Roaming\\uv\\python\\cpython-3.10-windows-x86_64-none\\python310.zip', 'C:\\Users\\admin\\AppData\\Roaming\\uv\\python\\cpython-3.10-windows-x86_64-none\\DLLs', 'C:\\Users\\admin\\AppData\\Roaming\\uv\\python\\cpython-3.10-windows-x86_64-none\\lib', 'C:\\Users\\admin\\AppData\\Roaming\\uv\\python\\cpython-3.10-windows-x86_64-none', 'C:\\VsCode\\llm\\.venv', 'C:\\VsCode\\llm\\.venv\\lib\\site-packages']

# 追加path
sys.path.append('C:\VsCode\py\03module')

"""

import sys


def test():
    """
    运行 uv run .\03module\hello.py, args 就是 ['hello.py']
    运行 uv run .\03module\hello.py lisi, args 就是 ['hello.py', 'lisi']
    """
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


def _main():
    """
    _main前面有一个下划线，这种函数被称为私有函数
    :return:
    """
    test()



if __name__ == '__main__':
    _main()
