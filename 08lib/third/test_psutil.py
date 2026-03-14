import psutil


def test_cpu():
    # print(psutil.cpu_count())  # 8
    # print(psutil.cpu_count(logical=False))  # 物理，4

    # 统计CPU的用户／系统／空闲时间/处理硬件中断时间/延迟过程调用时间
    # scputimes(user=356303.265625, system=460385.64062500023, idle=1880169.6249999998, interrupt=19107.5, dpc=74422.96875)
    print(psutil.cpu_times())

    # 实现类似 top 命令的CPU使用率，每秒刷新一次，累计10次
    for x in range(10):
        # 每个逻辑核心的使用率
        print(psutil.cpu_percent(interval=1, percpu=True))


def test_memory():
    # 虚拟内存
    # svmem(total=16805048320, available=653099008, percent=96.1, used=16151949312, free=653099008)
    print(psutil.virtual_memory())

    # 交换分区 /sin 从交换分区读入的字节数 page-in/ sout 写入交换分区的字节数 page-out
    # sswap(total=33351442432, used=13081968640, free=20269473792, percent=39.2, sin=0, sout=0)
    print(psutil.swap_memory())


def test_disk():
    # 磁盘分区信息
    # [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed')]
    print(psutil.disk_partitions())
    # 磁盘使用
    # sdiskusage(total=511868952576, used=422803513344, free=89065439232, percent=82.6)
    print(psutil.disk_usage('/'))
    # 磁盘IO
    # sdiskio(read_count=45860580, write_count=34151679, read_bytes=1276980207616, write_bytes=655518115840, read_time=46561, write_time=22505)
    print(psutil.disk_io_counters())


def test_network():
    # 获取网络读写字节／包的个数
    # snetio(bytes_sent=1325845185, bytes_recv=7132125662, packets_sent=5418390, packets_recv=7692385, errin=0, errout=0, dropin=0, dropout=0)
    # print(psutil.net_io_counters())

    # 获取网络接口信息
    # print(psutil.net_if_addrs())

    # 获取网络接口状态
    # print(psutil.net_if_stats())

    # 获取当前网络连接信息
    print(psutil.net_connections())


def test_ps():
    # print(psutil.pids())
    p = psutil.Process(26376)
    print(p.name())
    print(p.exe())

    print(p.cwd())
    print(p.cmdline())

    print(p.ppid)
    print(p.parent())
    print(p.children())

    print(p.status())
    print(p.username())
    print(p.create_time())
    print(p.memory_info())
    print(p.memory_percent())
    # 进程打开的文件
    print(p.open_files())
    # 进程的线程数量
    print(p.num_threads())

    # 所有线程信息
    print(p.threads())
    print(p.environ())

    #
    print(p.terminate())



def _main():
    # test_cpu()
    # test_memory()
    # test_disk()
    # test_network()
    test_ps()

if __name__ == '__main__':
    _main()
