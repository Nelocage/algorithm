# 问题提出
        # 如何实现可迭代对象和迭代器对象

# 案例模拟
        # 抓取各个城市的气温
        # 如果一次抓取所有城市的气温再显示，由于网络IO较慢，延迟极高，并且浪费存储空间，期望以“用时访问的策略”，
        # 并且能把所有城市气温封装到一个对象里，可用for语句进行迭代
# 知识补充
        # 字符串也是可迭代对象
        # 由可迭代对象生成迭代器对象
        # 实现可迭代需要对象内部实现.__iter__方法（自身的迭代器接口），或者.__getitem__ 方法（实现一个序列的接口）
        # 迭代器对象只实现了next方法，不停的调用下一个

# 解决方案
        # step1：实现一个迭代器对象weatheriterator,next()方法每次返回一个城市的气温
        # step2：实现一个可迭代对象weatheriterable,__iter__方法返回一个迭代器对象

from collections import Iterable, Iterator  # python标准库中已经对实现接口有了定义


class WeatherIterator(Iterator):  # 从iterator中直接继承
    def __init__(self, cities):  # 定义一个构造器，需要传入一个城市列表
        self.cities = cities  # 将这个城市列表对象，维护在这个类中
        self.index = 0  # 还需要维护迭代器的初始位置

    def getweather(self):  # 抓取天气的函数应该放在函数的内部，这样每次返回一个城市的天气
        pass

    def __next__(self):  # 迭代器对象应该实现next方法
        if self.index == len(self.cities):  # 先描述迭代完成时的情况
            raise StopIteration  # 抛出一个异常
        # 正常情况下
        city = self.cities[self.index]  # 当前的位置
        self.index += 1  # 迭代完成后每次进行自增操作，Python不支持++
        return self.getweather(city)  # 并且返回这次的城市信息


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities  # 内部同样维护这个变量，这样可以传给iterator构造器

    def __iter__(self):
        return WeatherIterator(self.cities)  # 返回一个迭代器的实例
