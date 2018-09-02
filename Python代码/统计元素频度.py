# 问题提出：
        # 如何统计序列中元素的出现频度
        # 第一个例子 某随机序列找到出现次数最高的三个元素，他们出现次数是多少
        # 第二个例子 对某英文文章的单词进行词频统计，找到出现次数最多的十个单词，他们出现的次数是多少


# 第一个例子
from random import randint

data = [randint(0, 20) for _ in range(30)]  # 利用列表解析生成随机列表
# 可以以data中的值作为字典的键，0作为值，创造出一个字典来
c = dict.fromkeys(data, 0)  # 用data中的每一个元素作为键 ,0作为初始值
print(c)
for x in data:
    c[x] += 1  # python 中没有自增运算符，循环遍历每一个元素，出现一次就加一
print(c)
# 进行到这步时，下一步要做的工作是根据字典的值对字典排序，又回到了“对字典进行排序.py"下

# 解决方法
        # 使用collection下的counter
        # 将序列传入counter的构造器，得到counter对象是元素频度的字典
        # counter.most_common(n)方法得到频度最高的n个元素的列表
from collections import Counter

c2 = Counter(data)  # 直接将data传给counter的构造器,返回一个字典，所以c2也是一个字典
print(c2.most_common(3))

# 第二个例子
# 使用正则表达式re 模块
import re

txt = open('english_article', encoding='UTF-8').read()  # 遇到open函数读取文档由于编码问题失败，可以使用encoding参数，限制打开文件的编码
txt1 = Counter(re.split('\W+', txt))  # 使用正则表达式的分割模块，利用非字母元素进行分割，并形成一个列表，准备传给counter
print(txt1.most_common(10))
