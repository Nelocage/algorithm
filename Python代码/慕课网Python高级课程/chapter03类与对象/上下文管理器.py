# try:
#     print('code start ')
#     raise KeyError
# except KeyError  as e:   #捕获异常
#     print("key  error")
# finally:  #无论上述代码有无运行，finally代码都会运行
#     print('finally')


#上下文管理器  也属于Python中的协议，协议即与魔法函数有关（原始版）
class my_with():
    def __enter__(self):
        print('enter')
        #获取资源
        return self

    def do_something(self):
        print('doing something')

    def __exit__(self, exc_type, exc_val, exc_tb):  #在结束后会自动调用这个方法
        #释放资源
        print('exit')


with my_with() as with1:  #调用需要加括号，只有传值才只是名字，with语句
    with1.do_something()

#更简单的方式
#不需要自己定义类，使用contextlib（高效版）
#例子
import contextlib

@contextlib.contextmanager #可以将函数变成上下文管理器,要求被他修饰的函数必须是一个生成器
def open_file():
    print('open file')      #yield之前的代码可以看做是enter函数
    yield {}
    print("file end ")      #yield之后的代码可以看做是exit函数


with open_file() as my_open:
    pass