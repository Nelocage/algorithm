# 问题提出：
# 如何为元组的每个元素命名，提高程序的可读性
# 集合，字典{}  元组() 列表[ ]
# 元组的优势：占用小，速度快
# 劣势：需要使用index ，大量使用index降低程序的可读性
# 元组劣势举例
student = ('JIM ', 16, 'male', '452@qq.com')
# 在访问某一项的时候需要使用index

# name
print(student[0])
# age
print(student[1])
# sex
print(student[2])
# 在元组很长的时候，元组的数据使用[number]的方式，使得可读性很差，不知道[number]的含义
# 在C 中解决这个可读性的问题可以使用宏定义的方式或者结构体的方式

# Python的解决方法
# 1)定义类似与其他语言的枚举类型，也就是定义一系列数值常量
# 2)使用标准库中collection.nametuple代替内置tuple
# 第一种方法：
#         由于Python中没有真正的枚举类型可以定义一些常量
NAME = 0
AGE = 1
print(student[NAME])
# 或者使用列表拆包的形式
NAME, AGE = range(2)  # 这种方法也可以，更加简单
# 第二种方法
from collections import namedtuple  # 返回一个内置元组的子类

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])  # 第一个参数：子类的名字,给每一个引索的名字
# 使用位置传参
s = Student('jim', 16, 'male', '43223@qq.com')  # 相当于实例化或者一个构造器
print(s)
# 使用关键字进行传参
s1 = Student(name='jim', age=16, sex='male', email='....')
print(s1)
# 这样直接可以使用属性名来进行访问
print(s.name)

# 判断两个类是否为父子类 这个函数是一个bool函数
isinstance(s, tuple)
