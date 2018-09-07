from ..chapter03.类和对象 import Date  #这块遇到一个导入包的问题
class User():
    def __init__(self,birthday):
        self.birthday=birthday

    def get_age(self):
        #返回年龄
        return 2018-self.birthday.year

if __name__ == '__main__':
    user=User(Date(1990,2,1))
    print(user.get_age())
