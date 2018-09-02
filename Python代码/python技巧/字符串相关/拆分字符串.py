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

#问题描述
        #如何将多个小字符串拼接成一个大的字符串
#解决方案
        #方案一：迭代列表，连续使用'+'操作，一次拼接每一个字符串
        #方案二：使用str.join()方法，更加快速的拼接列表中所有的字符串（推荐）

#第一种方法
string0=['hello',',world！','I ',' want',' to',' be',' a',' data',' scientist']
string1='hello'
string2='world'
string3=string1+string2  #直接使用加操作即可直接实现字符串的拼接
res=''
for x in string0:
    res+=x
    print(res)

#由打印可以看出，开销巨大，每一次使用，都需要频繁的释放临时资源

#第二种方法
print(' '.join(string0))  #前面的字符串代表分隔符，join接受一个可迭代对象，然后利用前面的分隔符，将他们链接起来,只需要一个参数，若有多个需要链接的字符串应该放在列表中
print(''.join(string0))  #直接链接不加任何分隔符

#如果有一个列表中既有字符，又有比如数字等非字符型，也要把他们每一项都变成字符串。进而拼接在一起
l=['hello',123]

#方法一：可以使用列表解析,但是会生成一个列表，可能会占用资源
print(''.join([ str(x) for x in l ]))

#方法二：使用生成器表达式，生成器表达式类似于列表解析，只不过方括号，变为圆括号，
print( str(x) for x in l )  #返回一个生成器对象
print(''.join(str(x) for x  in l))

#问题描述
        #如何对字符串进行左，中，右居中对齐

#解决方法
        #方法一：使用字符串的ljust() ,rjust().center()方法
        #方法二：使用format方法，传递类似'>20'，'<20'，'^20'参数，分别代表右对齐，左对齐，居中对齐
        #python必须注意对齐，缩进的问题

#方法一：
#ljust等需要两个参数，分别是：最后对齐的宽度和填充的字符
string1='you'

print(string1.ljust(20,'#'))

#方法二
print(format(string1,'>10'))

#实际需求
        #对一个字典内的字符串施行对齐，增加可读性,字典包含着键值对
dict={
    'tom ':30,
    'ertyy':35,
    'yeeirnivjrnv':49
}
#先统计当前字典中最长的字符串长度，keys方法可以返回一个键的列表，然后用len ,得到其长度,返回一个map，用max求其最大值
print(max(map(len,dict.keys())))#一个映射，第一个参数可以为一个函数，第二个参数为序列，map可以对序列中的每个元素执行之前定义的函数
max_length=max(map(len,dict.keys()))
for x in dict:          #字典默认进行键迭代
    print((x.ljust(max_length)),':',dict[x])

#问题提出
        #如何去掉字符串中不需要的字符
# 解决方法
#         方法一：字符串strip,lstrip,rstrip方法去掉字符串两端字符
#         方法二：删除单个固定位置的字符，可以使用切片+拼接的方式
#         方法三：字符串的replace方法或正则表达式re.sub()删除任意位置字符
#         方法四：字符串translate（），可以同时删除多种不同字符

#第一种：strip方法，去掉两端字符，lstrip,rstrip分别去掉左右端的字符
s='    abc    123   '
print(s.strip())  #strip的参数可以指定任意字符，在两端进行删除，默认为空格
s1='----abc+++'
print(s1.strip('-+'))  #-+同时去掉，不用指定元组的方式

#第二种：使用切片+拼接
s2='abc:123'  #python字符用单引号即可
print(s2[:3]+s2[4:])

#第三种：
s3='#$%abc$123$xyz$r'
print(s3.replace('$','')) #将所有的t都替换为空串，也就是删除的意思，但是replace方法只能替换一种
#若有多种字符需要替换，则需要使用正则表达式
import re
print(re.sub('[#%$]','',s3))  #方括号表示任意一个即可，第二个参数为要替换的字符

#第四种方法
s4='abcxyz'
print(s4)
#s4.translate()  #将一个字符串映射到另一个字符串上，重点是映射的关系
#translate第一个参数需要一个映射表，使用maketrans方法来完成映射表
print(s4.translate(str.maketrans('abcxyz','xyzabc')))
#以上为translate的原始目的

#这块没有运行成功，教程是Python2的，Python3无法正确运行，日后改正
#translate第一参数若为none,则不做任何映射，变为删除字符，指定需要删除的字符
print(s4.translate(bytes.maketrans(None,'xyz')))




