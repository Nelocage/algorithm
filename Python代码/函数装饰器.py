#问题
        #某些时候想为多个函数，统一添加某种功能，又不想在每个函数内添加完全相同的代码

#装饰器类似于包裹函数（wrap）,在原函数上添加新的功能。并且替代原函数，

#*args，可以传入不固定参数
def sum(a,b):return a+b
#若是不定长数字相加，则需使用*args参数
def sum1(*args):
    sum=0
    for x in args:
        sum+=x

    return sum


import time
def add(a,b):
    print(a+b)

#最基本的装饰器
#给现有函数增加一个记录程序运行时间的功能

def timer(func):
    """

    :param func:    被装饰的函数
    :return:        一个运行函数运行时间
    """
    def wrapper(*args,**kwargs):
        """

        :param args:        收集被装饰函数的参数
        :param kwargs:      收集被装饰函数的关键字参数start
        :return:
        """
        start_time=time.time()
        #使进程暂停一秒
        time.sleep(1)
        result=func(*args,**kwargs)
        stop_time=time.time()
        print("{func} spend {time}".format(func="add",time=stop_time-start_time))
        return result
    return wrapper

@timer
def add(x,y):
    print(x+y)
add(1,2)

#带参数的装饰器
def timer1(flag):
    """

    :param flag: 接收装饰器的参数
    :return:
    """
    def outer_wrapper(func):
        """

        :param func:   接收被装饰的函数
        :return:
        """
        #接收被装饰函数的参数
        def wrapper(*args,**kwargs):
            """

            :param args:        收集被装饰函数的参数
            :param kwargs:  收集被装饰函数的关键字参数
            :return:
            """
            if flag=="true":
                start_time=time.time()
                #使进程暂停一秒
                time.sleep(1)
                result=func(*args,**kwargs)
                stop_time=time.time()
                print("{func} spend {time}".format(func="add",time=stop_time-start_time))
                return result
            else:
                print("unexpect ending")
        return wrapper      #这块调用函数不能加括号？
    return outer_wrapper

@timer1(flag='false')
def add1(a,b):
    print(a+b)
add1(1,3)

#被多个装饰器装饰时，从里到外装饰
# @a
# @b
# @c
# def func():
#     pass
# 相当于func=a(b(c(func)))

#https://foofish.net/python-decorator.html  介绍装饰器的博文

