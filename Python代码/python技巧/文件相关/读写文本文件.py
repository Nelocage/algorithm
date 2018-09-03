#python 中open函数encoding指定编码格式

#打开二进制文件，比如影音文件
# 'rb'，'wb'表示以二进制的方式进行读写
#文件对象的seek方法，可以移动文件的指针
#jetbrain 代码整体左移，全选然后按tab+shift；整体右移，全选然后按tab
#文件的缓冲
        #问题提出
                # 将文件内容写入到硬件设备时，使用系统调用，这类IO操作的时间很长，为了减少IO 操作的次数，文件通常使用缓冲区
                # (有足够多的数据才进行系统调用)，文件的缓冲行为，分为全缓冲，行缓冲，无缓冲
                # 如何设置Python中文件对象的缓冲行为,改变缓冲区的大小

        # 改变缓冲区的大小f=open('demo.txt','w')
        # f.write('hello,world!')
        # f.close()

        #解决方案
                # 全缓冲：open函数的buffering 设置为大于1的整数n，n 为缓冲区大小
                # 行缓冲：open函数的buffering 设置为1
                # 无缓冲：open函数的buffering 设置为0
#问题提出
        #如何将文件映射到内存中
#解决方法
        #使用标准库中mmap模块的mmap()函数，他需要一个打开的文件描述符作为参数

#问题提出
        #如何访问文件的状态
        #类型，访问权限，修改时间，大小

#解决方法
        #方法一（系统调用）：标准库中os模块下的三个系统调用stat，fstat,lstat获取文件状态(应该舍弃）
        #flast需要传递一个文件描述符，open函数配合fileno方法可以用来生成文件描述符
        #方法二（快捷函数）：标准库中os.path下的一些函数，使用起来更加简洁（推荐）
import os
print(os.stat('demo.txt'))

#返回的值可以利用stat下面的方法进行解析
import stat
print(stat.S_ISDIR(os.stat('demo.txt').st_mode))  #判断是否为一个文件夹

print(os.path.isdir('demo.txt'))

#问题描述
        #如何使用临时文件
        #临时文件不用命名，且关闭后会自动被删除
# 解决方法

        #使用标准库中的templefile下的temporaryfile，namedtemporaryfile

#问题描述
        #如何读写CSV数据
#解决方法
        #使用标准库中CSV模块，可以使用其中reader和writer完成CSV文件读写

import csv
tem=open('iris.csv','rb')  #要使用二进制来读入
reader=csv.reader(tem)  #返回一个迭代器，迭代器只能调用next方法或者通过for循环，进行访问

#问题描述
        #读写json 数据
#解决方法
        #使用标准库中的json模块，其中loads,dumps函数可以完成json数据的 读写

import json
res=[1,2,'abc',{'name':'bob','age':12}]
print(res)
print(json.dumps(res))  #可以将Python对象转化为json数据
json.loads()#可以将json数据转化为Python对象

#问题描述
        #解析简单的XML文档
#解决方法
        #使用标准库中的xml.etree.elementtree ,其中parse函数可以解析xml数据


