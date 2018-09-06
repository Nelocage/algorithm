#Python中一切皆对象，函数也是对象，也可以被当做参数传给其他函数，函数和类都是对象，属于Python的一等公民
#Python的面向对象比Java更加彻底
#类也是对象，可以将类理解为一个模板，根据模板去创造对象，它本身也是对象，可以看成模板对象
#动态修改对象的属性---猴子补丁
# 一等公民的权利
#         可以赋值给一个变量
def ask(name="bobby"):
    print(name)

my_func=ask  #此处不能加（），当需要函数作为值传递，而不是运行函数本身的时候，不能加括号，直接写函数名就可以
my_func("bobby")

class Person:
    def __init__(self):
        print('bobby1')
my_class=Person
my_class()  #对这个类进行实例化

#         可以添加到集合对象中

obj_list=[]
obj_list.append(ask)
obj_list.append(Person)

for x in obj_list:
    print(x())  #此处需要加括号，表示对变量进行调用，可不只是作为值进行传递
    #函数没有return，默认none


#         可以作为参数传递给函数
def  my_decorator():
    return ask   #作为值时，不可以加括号
#函数可以返回一个函数，也就是装饰器的实现原理
#         可以作为函数的返回值

#Python中函数若没有指定返回值，则默认返回none