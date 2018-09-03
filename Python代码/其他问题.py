#问题
        #如何派生内置不可变类型并修改其实例化行为

#案例
        # 想自定义一种新类型的元素，对于传入的可迭代对象，只保留int类型且值大于0元素
        # 要求IntTuple是内置tuple的子类

#解决方法
        #定义类IntTuple继承内置tuple，并实现__new__,修改实例化行为

#知识补充
        #new方法是在创建对象时调用的
        #init方法是在对象一创建完就调用，而且只有通过系统的方法创建的对象才会执行init方法，object默认的new方法会先于init方法调用
        #new方法的形参是类，init方法的形参是对象

        #类创建对象时，若类中定义了init方法（重写了父类的init方法，会覆盖父类的init方法，但通过super（）方法
        #也可以继承父类的init方法），但没定义new方法，会自动调用父类object的new方法，通过系统的方式创建对象，对象一创建完会自动调用类中的init方法

class IntTuple(tuple):

    def __new__(cls, iterable):
        g=(x for x in iterable if isinstance(x,int )and x>0)  #使用一个生成器对象
        return super(IntTuple,cls).__new__(cls,g)
    def __init__(self,iterable):
        #在调用父类构造器之前
        #在self被传入之后，任何一个点都不可以被改变,所以要在创建self的时候进行改变，调用__new__方法
        #及时更改下一行传入的参数iterable也不可以
        print(self)  #已经传入了一个元组，这样已经不能改变了，不是改变父类构造器的参数就可以改变的
        super(IntTuple,self).__init__()  #调用父类的构造器方法
        #在调用父类构造器之后
        #不能在这里更改，因为tuple是一个不可变对象，一旦创建完成就不能更改

t=IntTuple([1,-1,'abc',6,3])
print(t)

#问题
        #如何为创建大量实例节省内存
#案例
        #网络游戏的玩家信息极多，如何降低开销

#解决方法
        #定义类的__slots__属性，他是用来声明实例属性名字的列表
        #关闭动态绑定属性的功能

class player(object):
    __slots__ = ['uid','name','stat','level']  #阻止进行动态绑定
    def __int__(self,uid,name,status=0,level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level

#类似与C语言中的结构体，无法支持动态绑定，有几个参数已经定义好了，不能随时添加

#问题
        #如何让对象支持上下文管理

#文件的上下文管理
# with open('history','w') as file:
#     file.writelines(['xyz\n'],'123\n')

#解决方案
        #实现上下文管理协议，需定义实例的__enter__，__exit__方法，他们分别在with开始和结束时被调用

#问题
        #如何创建可管理的对象属性

        #在面向对象编程中，我们把方法（函数）看做对象的接口，直接访问对象的属性可能是不安全的，或设计上不够灵活，
        #但是使用调用方法在形式上不如访问属性简洁
        #circle.getradius(5.0)   #方法可以对用户输入的值进行检查或者做一些额外操作，而访问属性则不可以
        #circle.getradiu=5.0

        #能否在形式上是属性访问，但实际上调用方法

#解决方案
        #使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问

#问题
        #如何让类支持比较操作

        #比如有一个矩形的类，希望两个矩阵的实例时，比较的是他们的面积，对运算符做一些重载

#解决
        #使用标准库下的functools 下的类装饰器total_ordering

#问题
        #如何使用描述符对实例属性做类型检查，比如实例的第一个参数必须是str ,第二个必须是int
        #要求：
                # 可以对实例变量名指定类型
                # 赋予不正确类型时抛出异常

#解决方法
        #使用描述符来实现需要类型检查的属性：分别实现  __get__  __set__  __delete__方法，这三个方法完成任意一个即可成为描述符
        #在set内部使用isinstance函数做类型检查


#问题
        #如何通过实例方法名字的字符串调用方法

#解决方法
        #方法一：使用内置函数getattr，通过名字在实例上获取方法对象，然后调用
        #使用标准库operator下的methodcaller函数调用








