#类变量与对象变量
class A():
    AA=1  #类变量,所有实例共享同一个变量，可以被类访问，更改。不可被任何一个对象更改，只可被访问
    def __init__(self,x,y):  #第一个参数为类的实例并不是类，初始化对象的
        self.x=x   #self 为对象变量
        self.y=y

a=A(2,3)
print(a.x,a.y,a.AA)     #对象变量可以访问类变量，但要是从对象角度更改类变量，只会更改该对象的该属性值，并不会更改类的
print(A.AA)
#print(A.x)  #此句会报错，类不能访问到对象变量，若要更改类变量，只能通过类来访问，去更改，在对象上改是无效的


#类属性和实例属性以及查找顺序     对象属性==实例属性
        #查找顺序为从底层到高层查找，先从自己找起，若没有则找类属性
        #多继承较为麻烦
        #MRO算法（Python3为C3算法，既不是深度优先，也不是广度优先）

#静态方法，类方法以及对象方法以及参数
class Date():

    #构造函数
    def __init__(self,year,month,day):  #均为实例方法，实例方法很常见，普通定义的方法均为实例方法
        self.year=year
        self.month=month
        self.day=day


    #定义魔法函数，使之可以直接打印
    def __str__(self):                  #实例方法，第一个参数就是一个实例
        return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)

    #静态方法
    @staticmethod
    def parse_from_string(data_str):   #静态方法没有第一个参数self  如果要想使用，只能通过类名进行调用
        year,month,day=tuple(data_str.split('-'))
        return Date(int(year),int(month),int(day))

    #类方法
    @classmethod
    def better_parse_from_string(cls,data_str):
        year,month,day=tuple(data_str.split('-'))
        return cls(int(year),int(month),int(day))


if __name__ == '__main__':
    new_day=Date(2018,9,7)
    print(new_day)  #由于定义了魔法函数，所以可以格式化打印对象时的语句


# 若需要输入2018-09-07
# 最应该想到的逻辑，就是处理一下，使之满足需求,需要使用静态方法
#data_str='2018-09-07'
# year,month,day=tuple(data_str.split('-'))
# new_day1=Date(int(year),int(month),int(day))
# print(new_day1)

#使用静态方法解决
new_day1=Date.parse_from_string(data_str='2018-01-01')
print(new_day1)
#缺点是由于返回的是类的构造器，所以一旦类改名字，该类的所有静态方法都必须重写

#更好的解决方法是类方法，传入一个cls,self 表达的是实例对象，cls是类本身
#@classmethod


#classmethod 基本可以取代staticmethod，之所以保留，是因为在某些情况完全没有必有，引入类，比如判断输入的是否为合法字符串，只是需要一个判断而已