# 问题提出：
#         如何进行反向迭代以及如何实现反向迭代
#         正向迭代只需要实现__iter__方法即可（可以使用yield语句）
#         不使用revers，那样会改变原始序列
#         不适用切片操作l=[::-1] 那样会生成一个新列表，占用空间
# 解决方法
#         使用内置的reversed,将得到一个序列的反向迭代器，与iter方法正好相反
# 需要实现__reversed__方法，返回一个反向迭代器

class my_reversed():
    def __init__(self, start, end, setp=0.1):  # 传入这三个参数
        self.start = start  # 记录这三个参数
        self.end = end
        self.step = setp

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step  # 并在返回之后加上一个步进
