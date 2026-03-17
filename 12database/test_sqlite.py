import sqlite3
from pathlib import Path

current_dir = Path(__file__).parent


def test_insert():
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建
    conn = sqlite3.connect(current_dir.joinpath('test.db'))

    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute('insert into user (id, name) values (\'1\',\'Michael\')')

    # 返回影响的行数
    print(cursor.rowcount)

    # 提交事务:
    conn.commit()
    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()


def test_select():
    conn = sqlite3.connect(current_dir.joinpath('test.db'))
    cursor = conn.cursor()
    # 执行查询语句
    cursor.execute('select * from user where id=?', ('1',))

    # 获得查询结果集:
    values = cursor.fetchall()

    # 结果集是一个list ，每个元素都是一个 tuple ，对应一行记录
    # [('1', 'Michael')]
    print(values)

    cursor.close()
    conn.close()


def _main():
    # test_insert()
    test_select()


if __name__ == '__main__':
    _main()
