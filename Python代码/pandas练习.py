# pandas的一些代码
import pandas as pd

path1 = "../input/dataset.tsv"  # 导入数据集
dataset = pd.read_cav(path1, set='\t')  # 存入数据集
dataset.head(10)  # 查看前十行的内容
dataset.shape[1]  # 有多少列
dataset.colums  # 打印出全部的列名称
