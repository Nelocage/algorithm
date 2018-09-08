class A():
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')
        super().__init__()#直接调用父类即可

if __name__ == '__main__':
    b=B()

# super函数的调用顺序，在多继承时应该格外注意，super并不是调用父类中的类，这种说法不准确，正确的
# # 应该是调用MRO算法中的下一个点
#Python不推荐使用多继承，设计不好的话，极易造成继承关系的混乱，Python推荐多继承使用mixin模式

# Mixin模式特点：
#       1）Mixin类功能单一
#       2）不和基类关联，可以和任意基类组合，基类可以不和mixin关联就能初始化成功
#         3）在Mixin中不要使用super这种用法
#         名字最好以Mixin结尾，一种规范

