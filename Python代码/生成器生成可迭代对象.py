# 问题提出
# 如何使用生成器函数实现可迭代对象
# 案例模拟
# 实现一个可迭代对象的类，他能迭代出给定范围内的所有素数

# 解决方案
# 将该类的__iter__方法实现成生成器函数，每次yield返回一个素数
# 知识补充
# 生成器函数：包含yield语句
# 生成器对象也是一个可迭代对象
class PrintNumbers:
    def __init__(self, start, end):  # 首先实现构造器，需要两个参数
        self.start = start  # 并在内部维护他们
        self.end = end
        self.answer = []

    def isPrime(self, number):
        if number < 2:
            return False
        for x in range(2, number):
            if number % x == 0:
                return False
        return True

    def __iter__(self):
        for number in range(self.start, self.end + 1):  # range的迭代范围是左闭右开
            if self.isPrime(number):  # 类内函数互相调用，需要在函数名字前面加上self
                # self.answer.append(number)   这么写并没有实现一个生成器，实现生成器需要调用yield语句
                yield number  # 实现生成器函数


test = PrintNumbers(1, 100)
for x in test:
    print(x)
