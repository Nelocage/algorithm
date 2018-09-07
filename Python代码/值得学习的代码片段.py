def use_logging(func):
    loging.warn("%s is running" % func.__name__)  #函数还有这个属性！
    func()

class MyVector():       #类的括号内添的是类之间的继承关系
    def __init__(self,x,y):   #将参数传给内部变量
        self.x=x
        self.y=y
    def __add__(self, other_instance):
        new_vector=MyVector(self.x+other_instance.x,self.y+other_instance.y)
        return new_vector
    def  __str__(self):   #添加使之可以结构化输出语句
        return "x:{x},y:{}".format(x=self.x,y=self.y)
first_vec=MyVector(1,2)
second_vec=MyVector(2,3)
print(first_vec+second_vec)







