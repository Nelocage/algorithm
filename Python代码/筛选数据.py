# 问题提出：如何在列表，字典，集合中根据条件筛选数据
        # 场景举例
        # 过滤掉列表中的负数
        # 筛选出字典中高于90的项
        # 筛出集合中能被3整除的元素

# 常规思路
    # 常规思路 用迭代的方式遍历每一个元素

data = [1, 2, -3, 42, -5]
res = []
for x in data:
    if x > 0:
        res.append(x)
print(res)

# 在Python中可以使用一些高级工具


#序列的解析十分重要，可以筛选数据
# 列表
        # filter函数:filter(lambda x:x>=0,data)
        # 列表解析:[x for x in data if x>=0] *首选
# 字典
        # 字典解析:{k:v for k ,v in data.iteritems()if v>90}
# 集合解析
        # {x for x in s if x%3==0}


# 列表举例
from random import randint  # 生成一个随机列表

data = [randint(-10, 10) for _ in range(10)]  # 在-10~10区间随机生成10个数，随机列表的生成方法，若是没有指定，则需要_ 占位
print(data)

a = filter(lambda x: x >= 0, data)  # 需要两个参数，第一个参数为一个函数，一般都是lambda,第二个为序列.filter返回一个迭代器对象  #第一种方法
b = []
b = list(a)
print(b)  # 可以使用这种方式显示出迭代器的内容

print([x for x in data if x >= 0])  # 首选的方法

# 字典举例 ，20个人的成绩
d = {x: randint(60, 100) for x in range(1, 21)}  # range 为学号    randint为成绩,range的区间是左开右闭  随机字典的生成方法
print(d)
# {for x in d}   #若是这样迭代字典，则只能迭代他的键
# {for k,v in d.items()}  #用items则可以同时迭代他的键和值
filter_dict = {k: v for k, v in d.items() if v > 90}
print(filter_dict)

# 集合举例
s = set(data)  # 将列表转化为set
print(s)
