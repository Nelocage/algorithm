#魔法函数就是以双下划线开头，双下划线结尾的函数
#for函数会拿到一个迭代器，会优先查找类的__iter__方法，若没有则有getitem方法也可以，魔法函数有多个代替品，程序需要实现某些魔法函数时
     #会在多个魔法函数中查找， 实现任意一个即可
# 实现魔法函数可以增加自定义类的特性，魔法函数会影响到使用Python的语法
# 学习切片操作
#魔法函数与Python从哪个类继承没有关系
class magic():

#常见魔法函数
#字符串表示

    def __repr__(self):
        pass

    def __str__(self):
        pass
#集合，序列相关
    def __len__(self):
        pass
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        pass
    def __delitem__(self, key):
        pass
    def __contains__(self, item):
        pass
#迭代相关
    def __iter__(self):
        pass
    def __next__(self):
        pass
#可调用
    def __call__(self, *args, **kwargs):
        pass
#with上下文管理器
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
#数值转换
    def __abs__(self):
        pass
    def __bool__(self):
        pass
    def __int__(self):
        pass
    def __float__(self):
        pass
    def __hash__(self):
        pass
#元类相关
    def __new__(cls, *args, **kwargs):
        pass
    def __init__(self):
        pass
#属性相关
    def __getattr__(self, item):
        pass
    def __setattr__(self, key, value):
        pass
    def __getattribute__(self, item):
        pass
    #def __setattribute__:
        pass
    def __dir__(self):
        pass
#属性描述符
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass
#协程相关
    def __await__(self):
        pass
    def __aiter__(self):
        pass
    def __anext__(self):
        pass
    def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
    def __aenter__(self):
        pass

