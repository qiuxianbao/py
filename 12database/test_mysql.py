import mysql


def test_insert():
    # 注意把password设为你的root口令
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    cursor = conn.cursor()

    # 创建user表
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

    # 返回影响条数
    print(cursor.rowcount)

    # 提交事务:
    conn.commit()
    cursor.close()


def test_select():
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    # 获取游标
    cursor = conn.cursor()

    # 运行查询
    cursor.execute('select * from user where id = %s', ('1',))

    values = cursor.fetchall()
    #
    print(values)

    cursor.close()
    conn.close()


def _main():
    test_insert()
    test_select()


if __name__ == '__main__':
    _main()
