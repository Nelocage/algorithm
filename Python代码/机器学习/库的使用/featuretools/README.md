#featuretools

##一个执行自动特征工程的库

在使用Featuretools之前，我们要了解这个库的三个主要组件：
*实体Entities
深度特征合成Deep Feature Synthesis
特征基元Feature primitives
实体可看作是Pandas中数据帧的表征，多个实体的集合称为实体集Entityset。
深度特征合成（DFS）与深度学习无关。作为一种特征工程方法，它实际上是Featuretools库的核心。它支持从单个数据帧和多个数据帧中创建新特征。
DFS通过把特征基元应用于实体集中的实体关系来创建特征。这些基元经常被用来手动生成特征，比如，基元“mean”可在聚合级别找到变量均值。