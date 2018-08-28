#include <bits/stdc++.h> // 可以代替很多库的引用，写算法题必备的头文件
#include <iostream>  //写算法题不要用cout ,和cin, 这两个函数运行速度慢，一般都需要用printf 和scanf,所以不要引用这个库
#include <stdio.h>  //必备的头文件
using namespace std;
//迭代器的基本使用
int main() {
    vector<int> name;
    //vector<int> name1[10];
    for(int i=1;i<=5;i++)   //输入1,2,3,4,5
    {
        name.push_back(i);
    }
    vector<int>::iterator it=name.begin(); //迭代器   vector<int>::iterator为类型



    for( int i=0;i<5;i++)  //输出1，2,3,4,5   注意两个循环条件的区别
    {
        printf("%d" ,*(it+i));  //注意迭代器的使用
        //printf("%d\n",name[i]);   /这两种写法是等价的

    }

    for(vector<int>::iterator it=name.begin();it!=name.end();it++) //迭代器的正确使用方法，迭代器不能it<name.end()
                                                                    // 所以只能使用it!=name.end()
        printf("%d",*(it)); //注意迭代器的使用
    return 0;
}
//在常用的数据STL中只有vector和string中，才允许使用name.begin()+3,这种迭代器加整数的的使用方法