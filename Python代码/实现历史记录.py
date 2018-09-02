# 问题提出
        # 如何实现用户的历史记录功能（最多N 条）
# 场景模拟
        # 浏览器
        # 视频播放器可以查看最近播放过的视频文件
        #shell可以查看用户输入过的命令

# 案例解析
        # 一个简单的猜数字小游戏，添加历史记录功能，显示用户最近猜过的数字

# 需要认真学习知识
        # pyhton的上下文管理器，with
        # 文件的读入权限，rb wb
        # python 的文件操作

# 备注
        # 这个程序现在没有完成，history的功能没有实现，对于Python文件的读写不了解，程序没有全部完成
# 游戏代码
from random import randint
from collections import deque
import pickle  # 可以将一个Python对象存入文件中，也可以从文件中读入这个Python对象
import os

number = randint(0, 100)
if os.path.exists('history') and open('history').read().__len__() != 0:
    file = open('history', 'rb')
    history = pickle.load(open('history'))
else:
    history = deque([], 10)


def guess(k):
    if k == number:
        print("真聪明")
        return True
    if k < number:
        print("低了")
    if k > number:
        print("高了")


while True:
    user_input = input("pleae input a number")
    print(user_input)
    if user_input.isdigit():  # 判断是否为一个数字，input默认返回字符串
        guess_number = int(user_input)  # 强行转化为int类型
        history.append(guess_number)
        if guess(guess_number):
            break
    # if guess(user_input):  #这样之所以不行，是因为input函数 默认返回的是字符串。字符串与int不能直接比较，需要化成int
    #     break
    elif user_input == 'history' or user_input == 'h?':  # 这种是在内存中的，一旦退出，记录就消失，需要将他保存在文件中
        print(list(history))
# 这段代码暂时不能运行，不知道如何每次运行时加载

pickle.dump(history, open('history'), 'wb')  # pickle.dump需要两个参数，第一个是需要保存的文件，第二个是一个文件对象.w参数给他一个可写的权限

# 下一次运行程序的时候，需要一个反向操作，pickle.load(),python中凡是需要传入一个文件的，都需要open这个函数，比如要看，则是open（..).read()
# pickle.load(open('history'))
# 实现历史记录功能
#  解决方法
        # 使用标准库collections中的deque，它是一个双端循环队列
        # 双端循环队列特别重要
        # 若队列满时，则新进来的元素入队，第一个元素出队
        # 程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导出

# 使用deque
from collections import deque

history1 = deque([], 10)  # 如果需要限制容量的话，则需传入第二个参数，若不需要直接deque(),直接生成一个就可以，deque的参数，第一个为队列的初始值，第二个为初始的容量

# 保存到文件中的pickle
