import threading
from datetime import datetime
def thread_func():  # 线程函数
    i = 0
    while(1):
        print(datetime.now())
        i += 1

def many_thread():
    threads = []
    for _ in range(10):  # 循环创建500个线程
        t = threading.Thread(target=thread_func)
        threads.append(t)
        # t.setDaemon(True)  # 给每个子线程添加守护线程
    for t in threads:  # 循环启动500个线程
        t.start()


if __name__ == '__main__':
    many_thread()
    print("thread end")