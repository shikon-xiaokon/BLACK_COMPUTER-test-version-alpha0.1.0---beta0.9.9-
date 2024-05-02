import tkinter as tk
import os
import pofile as po
import time
from datetime import datetime
import platform
import psutil
import datetime
from poprogress import simple_progress

# posix: linux系统;  nt: windows系统

po.mkdir(r'C:\py_pan')
po.mkdir(r'C:\py_pan\down')
po.mkdir(r'C:\py_pan\desk')
po.mkdir(r'C:\py_pan\system')
po.mkdir(r'C:\py_pan\systemAPP')
po.mkdir(r'C:\py_pan\code table')
po.mkdir(r'C:\py_pan\user')
po.mkdir(r'C:\py_pan\systemAPP\Test version of document writing tool')

jx = os.name


# print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")


def get_size():
    pass


if jx == "nt":
    print("welcom to black_computer tsv0.1")
    print("you use this system is black_computer alpha 0.1.5.If you want to learn about this system, you can enter in system () to view system information.")
    print("If you have any questions, you can input the command help() to consult me.")
    while True:
        gondo = 0
        shuru = input("black_computer root directory ~$ ")  # shuru函数代表用户输入的指令，将用户输入的指令存入一个函数中，以便后续处理。
        if shuru == "in system()":  # 查看系统信息
            print("""
        system:black_computer
        version:Test version system black_computer alpha 0.1.5
        Release time:2024/1/18 18:05:00
        author's name:Li Yanyi
        
        author's username:shikon_xiaokon
        kernel:Tuladinba Junk Kernel tvs0.1(Author's self-developed core)
        system application:Calculator Test Version
                           Test version of document writing tool
                           Device Manager beta version
                           Test version software for converting binary, octal, decimal, and hexadecimal numbers to each other
                           Generate merits and virtues and so on machine Test Version
        """)
        if shuru == "open Generate merits and virtues and so on machine Test Version":  # 功德机测试版
            gonde = int(input("Please enter the number of merits you want to add:"))  # gonde表示功德数量
            print("""
        功德+1
        功德+1""" * gonde)

        if shuru == "open Calculator Test Version":
            root = tk.Tk()
            root.title("Calculator Test Version")

            expression = ""

            result_label = tk.Label(root, text="计算结果")
            result_label.pack()


            def fun_0():
                global expression
                expression += "0"


            def fun_1():
                global expression
                expression += "1"


            def fun_2():
                global expression
                expression += "2"


            def fun_3():
                global expression
                expression += "3"


            def fun_4():
                global expression
                expression += "4"


            def fun_5():
                global expression
                expression += "5"


            def fun_6():
                global expression
                expression += "6"


            def fun_7():
                global expression
                expression += "7"


            def fun_8():
                global expression
                expression += "8"


            def fun_9():
                global expression
                expression += "9"


            def fun_add():
                global expression
                expression += "+"


            def fun_subtraction():
                global expression
                expression += "-"


            def fun_multiplication():
                global expression
                expression += "*"


            def fun_division():
                global expression
                expression += "/"


            def fun_result():
                global expression
                result_label.config(text=str(eval(expression)))
                expression = ""


            btn_number_0 = tk.Button(root, text="0", command=fun_0)
            btn_number_0.pack()
            btn_number_1 = tk.Button(root, text="1", command=fun_1)
            btn_number_1.pack()
            btn_number_2 = tk.Button(root, text="2", command=fun_2)
            btn_number_2.pack()
            btn_number_3 = tk.Button(root, text="3", command=fun_3)
            btn_number_3.pack()
            btn_number_4 = tk.Button(root, text="4", command=fun_4)
            btn_number_4.pack()
            btn_number_5 = tk.Button(root, text="5", command=fun_5)
            btn_number_5.pack()
            btn_number_6 = tk.Button(root, text="6", command=fun_6)
            btn_number_6.pack()
            btn_number_7 = tk.Button(root, text="7", command=fun_7)
            btn_number_7.pack()
            btn_number_8 = tk.Button(root, text="8", command=fun_8)
            btn_number_8.pack()
            btn_number_9 = tk.Button(root, text="9", command=fun_9)
            btn_number_9.pack()

            btn_add = tk.Button(root, text="+", command=fun_add)
            btn_add.pack()
            btn_subtraction = tk.Button(root, text="-", command=fun_subtraction)
            btn_subtraction.pack()
            btn_multiplication = tk.Button(root, text="*", command=fun_multiplication)
            btn_multiplication.pack()
            btn_division = tk.Button(root, text="/", command=fun_division)
            btn_division.pack()
            btn_result = tk.Button(root, text="=", command=fun_result)
            btn_result.pack()

            root.mainloop()
        # help
        if shuru == "help(black_computer's code table)":
            print("""
        if you entered "in system()"code,you can know black_coputer has five system application.They are Calculator Test Version;Test 
        version of document writing tool;Device Manager beta version;Test version software for converting binary, octal, decimal, and 
        hexadecimal numbers to each other;Generate merits and virtues and so on machine Test Version.So we want to open their we can 
        input"open+software name"and black_computer have two code too.They are respectively"help(black_computer's code table)"and"in
        system".you can have a try.
        """)
        # Test version of document writing tool工具代码
        if shuru == "open Test version of document writing tool":
            print("""
            [ —————————————————————————————————————————————————————————————————————————]
            [             Test version of document writing tool                        ]
            [——————————————————————————————————————————————————————————————————————————]
            [     {1}       Create a txt file                                          ]
            [     {2}       Write txt file                                             ]
            [     {3}       Delete txt file                                            ]
            [     {4}       Exit                                                       ]
            [——————————————————————————————————————————————————————————————————————————]
            
            """)
            while True:
                shu = int(input("Test version of document writing tool>>> "))
                if shu == 1:
                    wenj = input("txt name:")
                    with open('%s.txt' % (wenj), 'a') as f:
                        f.write('')
                        f.close()
                    print("创建成功!")

                if shu == 4:
                    print("已返回系统界面")
                    break

                if shu == 2:
                    while True:
                        wd = input("请输入要编写的文档：")  # wd函数表示将要编写的文档名
                        os.path.exists('C:/%s' % (wd))
                        with open('%s.txt' % (wd), 'r+') as f:
                            print("文档已编写内容如下：", f.read())

                        sr = input("""请输入你要输入的内容：""")  # sr函数存储用户输入的内容
                        with open('%s.txt' % (wd), 'a') as f:
                            f.write("%s" % (sr))
                        xw = input("是否删除txt中的内容 y/n：")

                        if xw == "y":
                            nr = input("请输入要删除的内容：")
                            with open('%s.txt' % (wd), 'r') as file:
                                lines = file.readlines()

                            with open('%s.txt' % (wd), 'w') as file:
                                for line in lines:
                                    if '%s' % (nr) not in line:
                                        file.write(line)
                        tc = input("是否退出文档编写 y/n：")
                        if tc == "y":
                            break

                if shu == 3:
                    j = input("请输入要删除的文档：")
                    os.remove(r'%s.txt' % (j))
                    print("成功删除！")

        # Device Manager beta version
        if shuru == "open Device Manager beta version":
            a_list = [214087, 124879, 8231947, "saufgwey", "asfugvbuwaiyf,asuhxhsdujenjcxkdef", 375925764943,
                      3890579834, 3284] * 10000
            for i in simple_progress(a_list):
                pass

            print("=" * 40, "System Information(系统信息)", "=" * 40)
            uname = platform.uname()

            processor_architecture = platform.architecture()
            print(f'Processor Architecture: {processor_architecture}')

            print(f"System: {uname.system}")
            print(f"Node Name: {uname.node}")
            print(f"Release: {uname.release}")
            print(f"Version: {uname.version}")
            print(f"Machine: {uname.machine}")
            print(f"Processor: {uname.processor}")

            # let's print CPU information
            print("=" * 40, "CPU Info", "=" * 40)


            # number of cores
            def cpuInfo():
                cpuTimes = psutil.cpu_times()

                # 获取CPU信息中的内存信息
                def memoryInfo(memory):
                    print(memory)
                    return {
                        '总内存(total)': str(round((float(memory.total) / 1024 / 1024 / 1024), 2)) + "G",
                        '已使用(used)': str(round((float(memory.used) / 1024 / 1024 / 1024), 2)) + "G",
                        '空闲(free)': str(round((float(memory.free) / 1024 / 1024 / 1024), 2)) + "G",
                        '使用率(percent)': str(memory.percent) + '%',
                        '可用(available)': (memory.available) if hasattr(memory, 'available') else '',
                        '活跃(active)': (memory.active) if hasattr(memory, 'active') else '',
                        '非活跃(inactive)': (memory.inactive) if hasattr(memory, 'inactive') else '',
                        '内核使用(wired)': (memory.wired) if hasattr(memory, 'wired') else ''
                    }

                return {
                    '物理CPU个数': psutil.cpu_count(logical=False),
                    '逻辑CPU个数': psutil.cpu_count(),
                    'CPU使用情况': psutil.cpu_percent(percpu=True),
                    '虚拟内存': memoryInfo(psutil.virtual_memory()),
                    '交换内存': memoryInfo(psutil.swap_memory()),
                    '系统启动到当前时刻': {
                        pro: getattr(cpuTimes, pro) for pro in dir(cpuTimes) if
                        pro[0:1] != '_' and pro not in ('index', 'count')
                    },
                }


            if __name__ == '__main__':
                computer_info = cpuInfo()
                print(computer_info)

            # 获取计算机的处理器名称
            # 获取计算机的处理器名称
            processor_name = platform.processor()
            print(f'processor name: {processor_name}')
            # 获取计算机的处理器架构
            print("Physical cores:", psutil.cpu_count(logical=False))
            print("Total cores:", psutil.cpu_count(logical=True))
            # CPU frequencies
            cpufreq = psutil.cpu_freq()
            print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
            print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
            print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
            # CPU usage
            print("CPU Usage Per Core:")
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                print(f"Core {i}: {percentage}%")
            print(f"Total CPU Usage: {psutil.cpu_percent()}%")

            # Memory Information
            print("=" * 40, "Memory Information", "=" * 40)
            # get the memory details
            svmem = psutil.virtual_memory()
            print(f"Total: {get_size()}")
            print(f"Available: {get_size()}")
            print(f"Used: {get_size(svmem.used)}")
            print(f"Percentage: {svmem.percent}%")
            print("=" * 20, "SWAP", "=" * 20)
            # get the swap memory details (if exists)
            swap = psutil.swap_memory()
            print(f"Total: {get_size(swap.total)}")
            print(f"Free: {get_size(swap.free)}")
            print(f"Used: {get_size(swap.used)}")
            print(f"Percentage: {swap.percent}%")

            # Disk Information
            print("=" * 40, "Disk Information", "=" * 40)
            print("Partitions and Usage:")
            # get all disk partitions
            partitions = psutil.disk_partitions()
            for partition in partitions:
                print(f"=== Device: {partition.device} ===")
                print(f"  Mountpoint: {partition.mountpoint}")
                print(f"  File system type: {partition.fstype}")
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    # this can be catched due to the disk that
                    # isn't ready
                    continue
                print(f"  Total Size: {get_size(partition_usage.total)}")
                print(f"  Used: {get_size(partition_usage.used)}")
                print(f"  Free: {get_size(partition_usage.free)}")
                print(f"  Percentage: {partition_usage.percent}%")
            # get IO statistics since boot
            disk_io = psutil.disk_io_counters()
            print(f"Total read: {get_size(disk_io.read_bytes)}")
            print(f"Total write: {get_size(disk_io.write_bytes)}")

            # Network information
            print("=" * 40, "Network Information", "=" * 40)
            # get all network interfaces (virtual and physical)
            if_addrs = psutil.net_if_addrs()
            for interface_name, interface_addresses in if_addrs.items():
                for address in interface_addresses:
                    print(f"=== Interface: {interface_name} ===")
                    if str(address.family) == 'AddressFamily.AF_INET':
                        print(f"  IP Address: {address.address}")
                        print(f"  Netmask: {address.netmask}")
                        print(f"  Broadcast IP: {address.broadcast}")
                    elif str(address.family) == 'AddressFamily.AF_PACKET':
                        print(f"  MAC Address: {address.address}")
                        print(f"  Netmask: {address.netmask}")
                        print(f"  Broadcast MAC: {address.broadcast}")
            # get IO statistics since boot
            net_io = psutil.net_io_counters()
            print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
            print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

            # Install with "pip install nvidia-ml-py3"
            import pynvml  # Must call this first

            print("=" * 40, "NVIDID GPU", "=" * 40)
            pynvml.nvmlInit()

            # Use device index to get handle
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)

            # Use handle to get device stats
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)

            # Report device stats
            print("Total memory:", memory_info.total)
            print("Free memory:", memory_info.free)
            print("Used memory:", memory_info.used)
            print("GPU Utilization:", utilization.gpu)
            print("Memory Utilization:", utilization.memory)
            print("=" * 40, "python", "=" * 40)
            # 获取Python版本
            python_version = platform.python_version()
            print(f'Python版本: {python_version}')

            # 获取Python解释器名称
            python_implementation = platform.python_implementation()
            print(f'Python解释器名称: {python_implementation}')

            # 获取Python解释器实现名称
            python_implementation_name = platform.python_implementation()
            print(f'Python解释器实现名称: {python_implementation_name}')

            print("=" * 89)
            print("")

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
else:
    print("your computer can't use this system")
    print("Error")
