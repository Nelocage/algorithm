# 问题提出
        # 如何快速找到多个字典中的公共键
# 场景模拟
        # 统计西甲每场比赛中都有进球的球员

from random import randint, sample

players = 'ABCDEFG'  # 假设只有这几个球员
b1 = sample(players, 3)  # 随机取样，抽出三个
print(b1)
game_number = sample(players, randint(0, 6))  # 进球的球员，进球的球员个数都应该是随机的，第二个参数虽然是个数字，但也可以用一个函数表示，只要这个函数的返回值是一个数字即可

# 使用字典解析产生每一轮的数据,共产生三轮数据
game_data1 = {x: randint(0, 5) for x in game_number}  # 每个球员的进球数目也是随机的
game_data2 = {x: randint(0, 5) for x in game_number}
game_data3 = {x: randint(0, 5) for x in game_number}

# 一种稍简单的方法
res = []
for k in game_data1:  # 循环迭代，迭代的是字典的键
    if k in game_data2 and game_data3:  # 是否同时存在于其他两个列表中
        res.append(k)  # 使用append函数，每次检测都加入到res空列表中
print(res)

# 高效解决方案
        # 利用集合(set)的交集操作
        # step1：使用字典的keys()方法，得到一个字典的keys的集合
        # step2：使用map函数，得到所有字典keys的集合
        # step3：使用reduce函数，取所有字典的keys的集合的交集
print(game_data1.keys())  # keys的返回值是一个集合，所以可以用集合的操作
print(game_data1.keys() & game_data2.keys() & game_data3.keys())  # 这种只适合比较小的，n轮则需要用map

# 要得到每一轮keys的集合可以用map这个函数 list函数真他妈好用啊,可以显示所有迭代器的数据
print(list(map(dict.keys, [game_data1, game_data2, game_data3])))

# Python3取消了全局命名空间的reduce函数，将reduce 放到了functools 模块中， 要使用reduce函数，需要先引用模块
from functools import reduce

# 迭代所有map中的集合做一个&操作
reduce = reduce(lambda a, b: a & b,map(dict.keys, [game_data1, game_data2, game_data3]))  # lambda 函数： lambda +参数个数，名字+“：”+函数体。冒号之前为参数
print(list(reduce))  # 直接print reduce变量不可以，必须用上万能的list（）
