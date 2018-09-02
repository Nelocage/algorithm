# 如何让字典保持有序
        # 应用场景：查询选手成绩，并排序，又不想使用列表，因为那样会遍历整个列表，效率较低
        # 但是Python内部的字典是以字典序进行排列的，如果想按其他的排序方式（比如进入字典的先后顺序）应
from os import open
from collections import OrderedDict  # 根据进入字典的先后顺序进行排序
from random import randint

d = OrderedDict()  # 先创建一个空的成绩表,创建一个实例 ,详细了解这个函数的其他用法
# 具体实战  答题竞赛用时较短的选手
players = list('A1BCDEFGH')  # 模拟出选手的名字
from time import time  # 可以返回系统的时间

start = time()  # 记录考试开始的时间点
# print(players.count())  count方法查看某个元素在列表中出现的个数  len 是统计列表长度的方法
# python2 有range 和xrange,python3中只有range,range就是xrange,之前的range取消 ,pyhton3中等待用户输入也只有input没有raw_input
for i in range(8):  # 这块要用8而不是player.__len__(),因为player里只有一个元素，打印出来会是1，而不是8

    input()  # 等待用户输入   每次循环完毕则获得一个时间，在player列表中随机选出一个
    p = players.pop(randint(0, 7 - i))  # 由于弹出一个就少了一个，所以长度是7-i
    end = time()  # 记录结束时的时间点
    print(i + 1, p, end - start)  # 由于从0 开始，所以是i+1,得到是第几名，第二个打印的说明是哪个人,最后一个参数，说明这个人用了多长时间
    d[p] = (i + 1, end - start)  # 为每一个用户创建一个元组，里面存储了他的排名以及用时

# 公布最终成绩，则遍历整个成绩单即可
print(players.__len__())  #
print('*' * 20)  # 建立一些分隔符
for k in d:
    print(k, d[k])  # 循环遍历成绩表中的每一个元素
