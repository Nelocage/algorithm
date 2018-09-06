#实际案例
        #某班学生期末考试成绩，三科分别存储在三个列表中，同时迭代三个列表，计算每个学生的总分（并行）
        #某年级有四个班，某次考试每班英语成绩分别存储在4个列表中，依次迭代每个列表，统计全学年成绩高于90分人数（串行）

from random import randint
class1=[randint(60,100) for  _ in  range(10)]
class2=[randint(60,100) for  _ in  range(10)]
class3=[randint(60,100) for  _ in  range(10)]

#简单的方式
        #使用引索,列表支持引索

for i  in range(len(class1)):
    sum=class1[i]+class2[i]+class3[i]
    print(class1[i],class2[i],class3[i],'sum:{sum}'.format(sum=sum))

#这种方法的局限性在于，不是所有的可迭代对象都支持引索操作
#解决方法
    #并行：使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组，迭代这些对象的相同位置,如不同，则返回到最短的那个长度
    #串行：使用标准库中的itertools.chain，它能将多个可迭代对象连接


#学习代码如何写
total=[]
#这块有一个自己给自己创造的玄学bug，特此记录一下
#为了图方便，循环变量之前写成了class1，class2，class3，也就是说我居然写成了跟列表一样的名字（没错，我就是这么菜）
#问题可想而知，经过下面的循环语句之后，三个列表都变成了他们每个的最后一个元素的值，之前的bug改变了变量的指向
#2018-09-06 20:54
for m,n,k in zip(class1,class2,class3):
    total.append(m+n+k)
print(total)
#串行

from itertools import chain  #将多个可迭代对象串联起来
for x in chain([1,2,3,4],['a','b','c']):
    print(x)
count=0
for s in chain(class1,class2,class3):
    if s>=90:
        count+=1

print(count)