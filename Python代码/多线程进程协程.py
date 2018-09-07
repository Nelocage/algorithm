#问题描述
        #多线程
        #要同时下载多个文件，并保存

#解决方法
        #使用标准库threading.Thread创建线程

from threading import Thread
import timeit   #  计算每部所有的时间，跨平台精度使用timeit.default_timer()
from collections import deque
import queue  #线程安全的队列
import time

a=deque()  #线程内部共有同一个地址空间


#第一种使用线程的方法
def v_print(number):

    print(number)
    return number+1

#t=Thread(target=v_print(),args=(1,)) #生成一个线程
#t.start()

#print("main thread")


#第二种使用线程的方法：使用类
class my_Thrad(Thread):

    def __init__(self,number):#构造器方法
        Thread.__init__(self)
        self.number=number
    def run(self):  #定义程序的入口点
        v_print(self.number)

#a=my_Thrad(1)
#a.start()
#print('main')

#若想每次子线程退出后，主线程在退出，相当于主线程对子线程的等待函数
#a.join()

#利用多线程模拟解决下载问题
#通常都将线程定义为列表
threads=[]

for  i  in range(1,11):
    start=timeit.default_timer()
    a=my_Thrad(i)
    threads.append(a)
    a.start()
    end=timeit.default_timer()
    print(end-start)
for i in threads:  #主线程等待每一个子线程的退出，一个阻塞函数
    i.join()

print("主线程结束")

#不使用进程的正常方法
for i in range(1,11):

    start=timeit.default_timer()
    v_print(i)
    end=timeit.default_timer()
    print(end-start)

#两者相比差很多，熟悉多进程，多线程，协程的使用方法

#Python中的线程只适合处理IO型的操作，由于Python的GIL（全局性解释器锁）的存在，Python中的线程无法处理CPU密集的操作

#问题
        #如何线程间通信
        #由于全局解释器锁的存在，多线程进行CPU密集型操作并不能提高执行效率

        #假设有一个程序，任务为下载并做相应转换，我们修改程序架构
        #1）使用多个downloadThread线程进行下载（IO操作）
        #2）使用一个covertThread线程进行转换（cpu 密集型操作）
        #3）下载线程把下载数据安全的传递给转换线程




#一个线程，间隔一定的时间，把一个递增的数字写入队列
#生产者模型
class productorThread(Thread):
    def __init__(self,work_queue):      #类函数需要加上self
        Thread.__init__(self)
        #若是Thread.__init__(self)  则扩号里面要加上self
        #若是super().__init__()  则扩号里面一定不能加上self
        self.work_queue=work_queue
    def run(self):
        num=1
        while True:
            self.work_queue.put(num)
            num+=1
            time.sleep(1)   #暂停一秒

          #多个线程同时访问同一个对象是不安全的，应该加锁，或者使用线程安全的队列

        #解决方法
        #使用标准库中的queue.queue,他是一个线程安全的队列，内部已经实现了锁
        #downloadThread把下载数据放入队列中 coverThread从队列中提取数据

#一个线程，从队列中取出数字并显示到终端
class consumerThread(Thread):
    def __init__(self,work_queue):
        Thread.__init__(self)
        self.work_queue=work_queue  #记录参数
    def run(self):
        while True:
            num=self.work_queue.get()  #当队列为空时，会阻塞，直到有数据
            print(num)

def main():
    work_queue=queue.Queue()
    productor=productorThread(work_queue)
    productor.daemon=True  #当主线程退出时，子线程也退出
    productor.start()

    consumer=consumerThread(work_queue)
    consumer.daemon=True
    consumer.start()


    work_queue.join() #主线程会停在这里，直到所有数字被get（），并且task_done()，因为没有调用task_done()，所以会一直阻塞在这里

# if __name__ == '__main__':
#     main()

#queue线程是安全的，从多个线程访问时无需加锁。
# 如果在work_queue.get()之后调用work_queue.task_done()，那么在队列空时work_queue.join()会返回。
# 这里work_queue.put()是间隔一定时间才往队列放东西，如果调用work_queue.task_done()，在数字1被get()后，队列空时，join()就返回，程序就结束了。
# 也就是程序只打印了1然后就退出了。
# 所以在这种使用情景下，不能调用task_done()，程序会一直循环下去。


#问题
        #如何在线程间进行事件通知
        #事件机制，是线程间最简单的通信机制：一个线程发送事件，其他线程等待事件
        #事件机制使用一个内部的标志，使用set方法进行是能为true，使用clear清除为false。wait方法会阻塞当前线程直到标记为true

import queue
from random import randint
from threading import Thread
from threading import Event


class WriteThread(Thread):
    def __init__(self,queue,WEvent,REvent):  #第二个参数需要一个queue
        Thread.__init__(self)
        self.queue=queue        #将值赋给类的内部对象
        self.WEvent=WEvent
        self.REvent=REvent

    def run(self):
        data=[randint(1,10) for _ in range(0,5)]
        self.queue.put(data)
        print("send read thread")
        self.REvent.set()  #通知读线程可以读了

        self.WEvent.wait() #等待写事件
        print("recv write event")
        self.WEvent.clear() #清除写事件，以方便下次读取
class ReadThread(Thread):
    def __init__(self,queue,WEvent,REvent):
        Thread.__init__(self)
        self.queue=queue
        self.WEvent=WEvent
        self.REvent=REvent

    def run(self):
        while True:
            self.REvent.wait()  #等待读事件
            print("rec read event")
            data=self.queue.get()
            print('read data is {0}'.format(data))
            print("send write event")
            self.WEvent.set()  #发送写事件
            self.REvent.clear()     #清除读事件，以方便下次读取

q=queue.Queue()#一个线程安全的队列
WEvent=Event()
REvent=Event()
WThread=WriteThread(q,WEvent,REvent)
RThread=ReadThread(q,WEvent,REvent)

WThread.start()
RThread.start()

#问题
        #如何使用线程本地数据
        #可以解决多线程并发的问题

#知识补充
        #如果在多线程并发环境中，一个可变对象涉及到共享与竞争，那么该可变对象就一定会涉及到线程间同步操作
        #这就是多线程并发的问题，否则该可变对象将作为线程私有对象，可通过threadlocal进行管理，实现线程间私有对象隔离的目的
        # threadlocal并没有解决多线程并发的问题，因为threadlocal管理的可变对象的性质本来就不会涉及到多线程并发而引发的
        # 共享，竞争和同步问题，使用threadlocal管理只是方便了多线程获取和使用该私有可变对象的途径和方

#解决方法
        #threading.local函数可以创建线程本地数据空间，其下属性对每个线程独立存在

#线程池
from concurrent.futures import ThreadPoolExecutor   #使用submit和map方法可以用来启动线程池中线程执行任务
executor=ThreadPoolExecutor(3)   #参数指定线程池中有几个线程

#使用线程池中的线程去执行任务
#任务函数
def f(a,b):
    print('f',a,b)
    return a**b

#通过submit方法调用线程池中的线程
res=executor.submit(f,2,3)  #第一个参数为任务函数名，之后的参数为任务函数所需要的参数  调用之后，那个线程又会被归还到线程池中
print(res.result())  #正常是不返回结果的，可以通过这个函数来得到运行结果,也是一个阻塞函数，若线程没有运行完，他将一直等待，直到运行完成


#map函数在多个线程上同时调用任务函数
executor.map(f,[2,3],[2,3])  #之后的参数均为任务函数的参数列表

#问题
        #如何使用多进程
        #https://blog.csdn.net/CityzenOldwang/article/details/78584175
        #由于全局解释锁的存在， 在任意时刻，只允许一个线程在解释器中运行，因此Python的多线程不适合处理CPU密集型任务
        #想要处理CPU密集型任务，可以使用多进程模型
from multiprocessing import Process
def f(s):
    print(s)

p=Process(target=f,args=('hello'))
p.start()
