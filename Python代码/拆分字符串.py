# 问题描述
#         如何拆分具有多种分隔符的字符串
#         若是只由空白分隔，则可以直接使用split，不传入任何参数，直接进行分隔
# 解决方法
#         使用正则表达式的re.split()方法，一次性拆分字符串

import re
#正则表达式中的方括号，表示可以是方括号中出现的任意自读
#re.split(r'[,;\t |]+',)  #加号，代表方括号中的字符，至少有0个或者多个

def  my_spilt(s,ds):
    for x in ds:
        pass

ds='abcd'  #可以循环参数

#问题
        #如何判断字符串a是否以字符串b开头或结尾
#案例模拟
        #文件夹下有很多文件，编写程序给其中所有的.sh .py文件加上用户可执行权限

#解决方法：
        #使用字符串的str.startwith()和str.endwith()方法
        #注意：多个匹配时参数使用元组
import os
import re
string='ubuntu.py'
res=[]
#print(os.listdir('.'))   #os.listdir()方法可以列出指定路径下的所有文件，返回一个列表

#执行以下列表解析
res=[name for name in os.listdir('.') if name.endswith(('.py'))]
#string.endswith(('.sh','.py'))  #endwith函数可以接受一个元组，元组内只要满足一个即可返回真，但只可以接受一个元组，不支持列表
print(res)
print(oct(os.stat('history').st_mode))  #可以返回特定路径下文件的权限，返回一个十进制的数字，要变成八进制更好看,最后三位即为Linux下的权限代数
