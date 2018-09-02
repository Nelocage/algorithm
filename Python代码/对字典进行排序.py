# 问题提出：
# 如何根据字典中值的大小，对字典的项进行排序
# 解决方案：
# 使用内置函数sorted，有两种方法
# 利用zip将字典数据转化为元组，
# 传递sorted函数的key参数

from random import randint

dict = {x: randint(60, 100) for x in range(1, 6)}  # 创建随机字典

print(dict)
# sorted #默认按照键的acsii码进行排序
# list() 这个函数可以让迭代器对象或者可迭代对象的值显示出来，变成一个列表，这个函数十分重要
# 元组的比较是先比较第0个元素，按元素顺序进行比较，所以要把字典的键值对反过来，让值在前面

dict.keys()  # 得到一个字典中所有的键
dict.values()  # 得到一个字典所有的值
# zip函数，把两个列表拼起来变成一个

# 第一种方法
l = list(zip(dict.values(), dict.keys()))  # 让值在列前面  一旦碰到显示不出来的时候，直接加一个list函数，使之变成列表即可访问
print(l)  # 有的函数可能返回的是个对象或者是迭代器，无法直接print，使用list()可将其变成可打印版本
print(sorted(l))

# 第二种方法
dict.items()  # 字典中的item方法直接就可以打印每一对键值，但是不可以直接用他排序，因为比较的还是当前的键值。可使用sorted的一个参数
sorted(dict.items(), key=lambda x: x[1])  # key参数需要传入一个函数，一般是lamdba函数，可以自己定义根据哪一个部分进行比较，序号从0 开始
