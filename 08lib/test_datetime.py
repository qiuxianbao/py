# 时间
from datetime import datetime, timedelta, timezone


def test_datatime_timestamp():
    print(datetime.now())  # 2026-03-10 10:16:09.966113

    # 获取指定日期和时间
    dt = datetime(2015, 4, 19, 12, 20)
    print(dt)

    """
    知识点：时间戳
    
    在计算机中，时间实际上是用数字表示的。
    我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为 epoch time（纪元时间），记为 0 （1970年以前的时间timestamp为负数），
    当前时间就是相对于epoch time的秒数，称为timestamp
    
    可以理解为：
    timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
    
    对应的北京时间为：
    timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
    
    可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，
    因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。
    
    """
    print(dt.timestamp())  # 1429417200.0   单位是s

    """
    注意到timestamp是一个浮点数，它没有时区的概念，而【datetime】是有时区的
    
    此处转换是在timestamp和本地时间做转换
    本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间
    """
    t = 1429417200.0

    print(datetime.fromtimestamp(t))  # 2015-04-19 12:20:00，实际上就是UTC+8:00时区的时间 2015-04-19 12:20:00 UTC+8:00
    print(datetime.utcfromtimestamp(t))  # 2015-04-19 04:20:00 UTC+0:00

    print(datetime.fromtimestamp(t).astimezone())  # 2015-04-19 12:20:00+08:00


def test_datatime_str():
    # 字符串转换后的datetime是没有时区信息
    cday = datetime.strptime('2015-06-01 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday)

    # 转字符串
    print(cday.strftime('%a, %b %d %H:%M'))  # Mon, Jun 01 18:19


def test_datatime_delt():
    now = datetime.now()
    print(now.astimezone())

    after_two_hours = now + timedelta(hours=2)
    print(after_two_hours.astimezone())

    after_one_day_two_hours = now + timedelta(days=1, hours=2)
    print(after_one_day_two_hours.astimezone())


def test_datatime_tz():
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00

    now = datetime.now(tz=tz_utc_8)  # 强制设置为UTC+8:00
    print(now)

    # 另一种设置时区的方式
    replace = datetime.now().replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
    print(replace)


    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)

    # astimezone()将转换时区为北京时间
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)

    # 将转换时区为东京时间
    tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt)

    """
    astimezone原理：保留原始时刻不变，直接进行时区转换
    
    时区转换的关键在于，拿到一个 datetime 时，要获知其正确的时区，然后强制设置时区，作为基准时间
    利用带时区的 datetime ，通过 astimezone() 方法，可以转换到任意时区
    
    不是必须从UTC+0:00时区转换到其他时区，任何带时区的 datetime 都可以正确转换
    """
    tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt2)


def _main():
    # test_datatime_timestamp()
    # test_datatime_str()
    # test_datatime_delt()
    test_datatime_tz()


if __name__ == '__main__':
    _main()
