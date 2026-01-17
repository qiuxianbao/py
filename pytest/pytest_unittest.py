
"""
#1.安装单测包
pip install pytest


#2.方法名必须以test开头的文件
```
文件名不能是pytest

pytest.py:None (pytest.py)
import file mismatch:
imported module 'pytest' has this __file__ attribute:
  C:\Python\Python311\Lib\site-packages\pytest
which is not the same as the test file we want to collect:
  C:\VsCode\hello-agents\code\chapter4\test\pytest.py
HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules
```
"""
import pytest

# 类名必须是Test开头
class TestA:
    # 方法名必须以test开头
    def test_a(self):
        print("a")

class TestB:
    # 方法名必须以test开头
    def test_b(self):
        print("b")

if __name__ == '__main__':
    pytest.main([__file__])