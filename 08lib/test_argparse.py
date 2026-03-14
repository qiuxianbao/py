import argparse


# 参数解析

def _main():

    # 定义一个ArgumentParser实例:
    parser = argparse.ArgumentParser(
        prog='backup',  # 程序名
        description='Backup MySQL database.',  # 描述
        epilog='Copyright(r), 2023'  # 说明信息，比如示例用法
    )

    # 定义关键字参数:
    parser.add_argument('--host', default='localhost')
    # 此参数必须为int类型:
    parser.add_argument('--port', default='3306', type=int)

    # 允许用户输入简写的-u:
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)

    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true',
                        required=False, help='Compress backup files by gz.')

    """
    定义位置参数:
    
    参数名不以 - 或 -- 开头
    必须按顺序提供
    显示在帮助信息的 positional arguments: 部分
    """
    parser.add_argument('outfile')


    # 解析参数:
    args = parser.parse_args()
    # 打印参数:
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')


if __name__ == '__main__':

    """
    // 参数错误提示
    (py) PS C:\VsCode\py> uv run .\08lib\test_argparse.py                          
    usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE [-gz] outfile
    backup: error: the following arguments are required: -u/--user, -p/--password, --database, outfile

    
    // 帮助
    (py) PS C:\VsCode\py> uv run .\08lib\test_argparse.py -h
    usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE [-gz] outfile
    
    Backup MySQL database.
    
    positional arguments:
      outfile
    
    options:
      -h, --help            show this help message and exit
      --host HOST
      --port PORT
      -u USER, --user USER
      -p PASSWORD, --password PASSWORD
      --database DATABASE
      -gz, --gzcompress     Compress backup files by gz.
    
    Copyright(r), 2023
    
    // 正确示例
    (py) PS C:\VsCode\py> uv run .\08lib\test_argparse.py -u root -p 123456 --database testdb backup.sql
    parsed args:
    outfile = backup.sql
    host = localhost
    port = 3306
    user = root
    password = 123456
    database = testdb
    gzcompress = False

    """
    _main()
