#抽象基类
        #内部实现了一些方法，所有继承他的类，必须重写他里面的方法，抽象基类无法进行实例化
        # 抽象基类无法进行实例化Python的抽象基类类似于Java、C++等面向对象语言中的接口的概念。
        # 抽象基类提供了一种要求子类实现指定协议的方式，如果一个抽象基类要求实现指定的方法，
        # 而子类没有实现的话，当试图创建子类或者执行子类代码时会抛出异常

#hasattr()  #判断某个对象有没有某个属性
#但更好的则是使用
#isinstance()

class Company():
    def __init__(self,employee_list):
        self.employee=employee_list
    def __len__(self):
        return len(self.employee)
com=Company(['bobby1','bobby2'])
#为什么已经有鸭子类型，还需要提出抽象基类的概念？
#主要有以下两种应用情景
        #我们需要在某些情况下希望判定某个对象的类型
from collections import Sized
isinstance(com,Sized)
        #我们需要强制某个子类必须实现某些方法
        #可以作为一种约定，开发框架常用
        #可以做一些接口的强制规定


#模拟抽象基类
# class CacheBase1():
#     #可以定义为抛出异常，这样只要子类不重写该方法，则会默认抛出异常
#     def __get__(self, instance, owner):
#         raise NotImplementedError
#     def __set__(self, instance, value):
#         raise NotImplementedError
#
#
# class RedisCache(CacheBase):
#     pass
# redis_cache=RedisCache()
# redis_cache.__set__('key','value')  #由于没有重写基类的方法，这条语句会抛出异常

#定义抽象基类，需要引入ABC模块，（abstract，base，class）
import abc


# noinspection PyDeprecation
class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def get(self,key):
        pass
    @abc.abstractclassmethod
    def set(self,key,value):
        pass
class RedisCache(CacheBase):
    def set(self,key,value):
        pass
    def get(self,key):
        pass
redis_cache=RedisCache()
redis_cache.set('key','value')

#抽象基类用的比较少，Python更多应该用鸭子类型，如果非要继承，可以使用mixin这种多继承的方式
#避免使用抽象基类，很容易设计过度，一些优秀的框架ABC这个包也很少使用

#网址：https://blog.csdn.net/xiemanr/article/details/78374643