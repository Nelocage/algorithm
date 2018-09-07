class Cat():
    def say(selfs):
        print(' I am a cat ')

class Dog():
    def say(selfs):
        print(' I am a dog ')

class Duck():
    def say(selfs):
        print(' I am a duck ')

animal=Cat()  #注意这里是否添加括号,加括号表示调用，不加括号表示赋值
animal.say()

animal_list=[Cat,Dog,Duck]
for animal1 in animal_list:
    animal1().say()  #这里不加括号，则会报错,提示不知道哪个方法。因为三个类同时实现了一个方法名，我们就可以调用同一个方法

#只要定义了相同方法就可以完成多态，而不必想Java一样，定义共同父类，并在每个子类中重写该方法，Python中不需要继承任何类，包含相同的方法名即可
#比如某函数需要接受一个可迭代对象作为参数，只要某对象是一个可迭代对象就可以了
