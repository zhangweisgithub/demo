import os
import multiprocessing
import time


#              文件名称　　　源目录　　　目的目录
def copy_file(file_name, src_path, dest_path, q):
    """子进程函数　完成指定文件的拷贝"""
    # 源目录　+ ‘／’＋　文件名称　　　－－－－－－> 目的目录　+ '/'＋　文件
    # print("正在拷贝一个文件")
    # 打开源文件　　读
    # 打开目的文件　写入
    src_file = open(src_path + '/' + file_name, "rb")
    dest_file = open(dest_path + '/' + file_name, 'wb')

    # 完成拷贝
    # file_data = src_file.read()
    # dest_file.write(file_data)
    while True:
        file_data = src_file.read(4096)
        if not file_data:
            break
        dest_file.write(file_data)

    # 关闭文件
    src_file.close()
    dest_file.close()

    # 将拷贝完成的文件名称　写入队列
    q.put(file_name)


if __name__ == '__main__':
    # 1 输入需要拷贝的目录名称　- 源目录 demo
    src_path = input("请输入你需要拷贝的目录:")

    # 2 根据输入的名称　创建一个新的目录名  -备份　－－　目的目录
    dest_path = src_path + '-备份'
    os.mkdir(dest_path)

    # ３　获取源目录下的额文件列表 ['1.py','2.py']
    file_list = os.listdir(src_path)

    # 创建队列　子进程通过该队列告诉主进程　文件拷贝完成的进度
    queue = multiprocessing.Queue(128)

    # ４　遍历文件列表　为其中没有一个文件创建一个子进程完成这个文件的拷贝
    for file in file_list:
        pro = multiprocessing.Process(target=copy_file, args=(file, src_path, dest_path, queue))
        pro.start()

    # 计算已经完成的拷贝的文件数量
    count = 0
    while True:
        file_name = queue.get()
        count += 1
        # 　回到行开始的地方　　　　　　　　　　　　　　　　　　　　　　　　　不让默认换行
        print("\r 当前完成的进度是%f %%" % (100 * count / len(file_list)), end='')
        # time.sleep()
        if count == len(file_list):
            break
