
# UV教程-Python 包与环境管理工具

参考资料：
> [uv](https://uv.doczh.com/)

---
## 安装
```shell
# 在 Windows 上安装
  
PS C:\Users\admin> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"                                                                                               
Downloading uv 0.10.2 (x86_64-pc-windows-msvc)                                                                                                               
Installing to C:\Users\admin\.local\bin
  uv.exe
  uvx.exe
  uvw.exe
everything's installed!
```


```shell
# 查看可用的 Python 版本

PS C:\Users\admin> uv -V
uv 0.10.2 (a788db7e5 2026-02-10)
```

---
## 管理 Python 版本
```shell
# 安装特定版本的 Python

PS C:\Users\admin> uv python list
cpython-3.15.0a5-windows-x86_64-none                 <download available>
cpython-3.15.0a5+freethreaded-windows-x86_64-none    <download available>
cpython-3.14.3-windows-x86_64-none                   <download available>
cpython-3.14.3+freethreaded-windows-x86_64-none      <download available>
cpython-3.13.12-windows-x86_64-none                  <download available>
cpython-3.13.12+freethreaded-windows-x86_64-none     <download available>
cpython-3.12.12-windows-x86_64-none                  <download available>
cpython-3.11.14-windows-x86_64-none                  <download available>
cpython-3.10.19-windows-x86_64-none                  <download available>
cpython-3.9.25-windows-x86_64-none                   <download available>
cpython-3.8.20-windows-x86_64-none                   <download available>
pypy-3.11.13-windows-x86_64-none                     <download available>
pypy-3.10.16-windows-x86_64-none                     <download available>
pypy-3.9.19-windows-x86_64-none                      <download available>
pypy-3.8.16-windows-x86_64-none                      <download available>
graalpy-3.12.0-windows-x86_64-none                   <download available>
graalpy-3.11.0-windows-x86_64-none                   <download available>
graalpy-3.10.0-windows-x86_64-none                   <download available>
```

```shell
# 安装特定版本的 Python

PS C:\Users\admin> uv python install 3.10
Installed Python 3.10.19 in 1m 44s
 + cpython-3.10.19-windows-x86_64-none (python3.10.exe)
 
PS C:\Users\admin> uv python install 3.11
Installed Python 3.11.14 in 34.08s
 + cpython-3.11.14-windows-x86_64-none (python3.11.exe) 
 
```

---
## 使用

```shell
# 进入到项目根目录，创建虚拟环境

PS C:\VsCode\hello-agents> uv venv
Using CPython 3.11.14
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate

# 激活环境
PS C:\VsCode\hello-agents> .venv\Scripts\activate
(hello-agents) PS C:\VsCode\hello-agents> uv pip --help         
Manage Python packages with a pip-compatible interface

# 为当前项目固定 Python 3.11
uv python pin 3.11

```

```shell
# 安装依赖包
(hello-agents) PS C:\VsCode\hello-agents> uv pip install "hello-agents[all]==0.2.2"
⠼ python-dotenv==1.2.1

uv pip install -r requirements.txt
```

```shell
# 列出已安装包及其版本
PS C:\VsCode\hello-agents> uv pip freeze                            
a2a-sdk==0.3.22

```

```shell
#显示 uv 安装的 Python 版本路径
PS C:\VsCode\hello-agents> uv python dir         
C:\Users\admin\AppData\Roaming\uv\python
```

```shell
# 运行脚本
PS C:\VsCode\hello-agents\code\chapter4> uv run .\test_llm_client.py

```

