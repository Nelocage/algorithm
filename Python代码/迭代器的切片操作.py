#问题提出
        #如何对迭代器做切片操作


#低级解决方法
        #使用文件的readline
file=open('history')
lines=file.readline()#可以将文件的每一行读入到列表中
#然后再对那个列表进行切片操作   熟悉列表的切片操作
print(lines[1:2])   #但是readline函数默认读取整个文件到内存中 ，需要较大的空间

for line in file:   #直接使用文件的迭代器即可
    print(line)

#解决方案
    #使用标准库中的itertools.islice,他能返回一个迭代器对象切片的生成器
from itertools import islice   #返回一个生成器或者迭代器，就可以使用for语句来进行不断迭代
for line in islice(file,100,300):  #参数依次为可迭代对象，起始点，结束点，步长。若是只有两个参数，则第二个是结尾值
    print(line)                    #(islice(file,500))前500个，islice(file,100,None) 100 到最后

#islice()会记录迭代的位置，所以每次使用都需要重新申请，[1,2,3,4,5,6,7,8],islice(file,1,2),再调用的时候就是相当于（2,3）的作用