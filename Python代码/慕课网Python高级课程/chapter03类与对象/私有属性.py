#from ..chapter03类与对象.类和对象 import Date  #这块遇到一个导入包的问题，不知道为什么不能这样导入
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

class User():
    def __init__(self,birthday):  #函数或者变量名字前加双下划线，声明为私有变量，将函数隐藏。实现封装
        self.__birthday=birthday

    def get_age(self):
        #返回年龄
        return 2018-self.birthday.year

if __name__ == '__main__':
    user=User(Date(1990,2,1))

    print(user.get_age())
