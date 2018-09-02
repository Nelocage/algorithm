#include <bits/stdc++.h> // 可以代替很多库的引用，写算法题必备的头文件
#include <iostream>  //写算法题不要用cout ,和cin, 这两个函数运行速度慢，一般都需要用printf 和scanf,所以不要引用这个库
#include <stdio.h>  //必备的头文件


//大部分STL 都是这样定义的，vector<typename> ...
//typename可以是任何类型，例如int double char 结构体 或者其他STL标准容器
//如果是个标准容器，要在>>之间加上空格

using namespace std; // 使用STL必须加的一句话


//迭代器的基本使用
int my_vector() {
    vector<int> name;
    //vector<int> name1[10];
    for (int i = 1; i <= 5; i++)   //输入1,2,3,4,5
    {
        name.push_back(i);  //在容器后面添加一个元素，时间复杂度O(1)
    }
    vector<int>::iterator it = name.begin(); //迭代器   vector<int>::iterator为类型



    for (int i = 0; i < 5; i++)  //输出1，2,3,4,5   注意两个循环条件的区别
    {
        printf("%d", *(it + i));  //注意迭代器的使用
        //printf("%d\n",name[i]);   /这两种写法是等价的

    }

    for (vector<int>::iterator it = name.begin(); it != name.end(); it++) //迭代器的正确使用方法，迭代器不能it<name.end()
        // 所以只能使用it!=name.end()
        printf("%d", *(it)); //注意迭代器的使用


//在常用的数据STL中只有vector和string中，才允许使用name.begin()+3,这种迭代器加整数的的使用方法


    for (int i = 0; i < name.size(); i++)  //使用size函数来获取vector的容量,进而进行输出
        printf("%d", name[i]);

    name.pop_back();   //删除队尾元素，O(1)
    //name.clear();    //清除所有元素，O(N)，N为元素个数
    name.insert(name.begin() + 3, -1); //insert(it ,x),向任意迭代器it处，添加元素x,O(N)

    //erase有两种用法，点删除和区间删除，均为O(N)
    name.erase(name.begin() + 2);    //删除迭代器it处的元素，点删除。erase（it)
    name.erase(name.begin() + 1, name.begin() + 4); //区间删除.erate(first,last),删除[first，last）的所有元素
    //由此可知，删除一个vector中所有的元素，可以有两种写法
    name.erase(name.begin(), name.end()); //name.end()正是指向尾元素的下一个地址，另一种常规写法即调用clear（）

    //vector的使用用途
    // 1）可以作为元素个数不确定的数组使用
    //2)以邻接表的形式储存图
}

int my_set() {
    //set 译为集合，是一个内部自动有序且不含重复元素的容器，在考试中，有可能出现需要去掉重复元素的情况，而且有可能因这些元素
    //比较大或者类型不是int型而不能直接开散列表，在这种情况下就可以用set保留元素本身，而不考虑它的个数。
    //set的两个最重要的特点：内部自动有序，不含重复元素

    set<int> name;  //单独定义一个set
    //set只能通过迭代器进行访问
    set<int>::iterator it;  //通过*it进行访问
    //除了vector和string之外的STL容器，都不支持*（it+i)的访问方式，因此set只能枚举
    //name.insert() 可将X 插入set中，并自动递增排序和去重，时间复杂度O(logN),N为元素个数
    //find（value）返回set中对应值为value的迭代器，时间复杂度同上
    //erase两种用法，点删除与区间删除，点输出可以配合find函数使用，与vector类似

    name.erase(name.find(100));
    //size 和clear

    //set最主要的用途是自动去重并按升序排序，因此碰到需要去重但是不方便直接开数组的情况，可以尝试用set解决
    //set中元素是唯一的，如果需要处理不唯一的情况，则需要使用multiset,另外C++11中还增加了unordered_set,
    //以散列代替set内部的红黑树（一种自平衡查找树）实现，使其可以用来处理只去重但不排序的需求
    //速度比set快很多
    //
}

int set_enum()    //set的迭代器使用
{
    set<int> st;
    st.insert(3);
    st.insert(5);
    st.insert(2);
    st.insert(3);

    for (set<int>::iterator it = st.begin(); it != st.end(); it++)  //不支持it<st.end()这种写法,学习STL的输出语句
    {
        printf("%d", *it);
    }
}


int set_find() {
    set<int> st;
    for (int i = 1; i < 3; i++)
        st.insert(i);
    set<int>::iterator it = st.find(2);
    printf("%d", *it);
    //以上两句可以写为
    printf("%d", *(st.find(2)));
}

int my_string() {
    string str = "abcd";   //string的定义
    /*string 元素的访问两种方式，下标或者迭代器
    //string和vector一样支持直接对迭代进行加减某个数字
     string可以直接使用  +=  将两个string拼接起来或赋值
     也可以使用==    ！=    <  <= > >=来比较大小，比较顺序为字典序
     insert有多种写法
     1）insert（pos,string),在pos号位置插入字符串string
     2）inser（it，it2，it3），it为原字符串的欲插入位置，it2，it3为待插字符串的首尾迭代器，用来表示串[it2,it3]
        将被插在it的位置上
    erase函数与vector的相同，但是区间删除有另外一种写法
        erase（pos,length)
    clear 函数
    substr(pos,len)返回从pos号位开始，长度为len的字符串，O（len)
     string::npos是一个常数，其本身的值为-1，但由于是unsigned_int类型，因此实际上也可以认为是unsigned_int 类型的最大
     的最大值，string::npos用以作为find函数失配时的返回值，可认为string::npos等于-1或者4294967295
     find()函数：
        find(str2),当str2是str的子串时，返回其在str中第一次出现的位置，如果str2不是str的子串，那么返回string::npos
        find(str2,pos),从str的pos号位开始匹配str2,返回值与上相同，时间复杂度O（mn)
    replace(pos,len,str2)把str从pos号位开始，长度为len的子串，替换为str2
    replace(it1,it2,str2)把str的迭代器[it1,it2)范围的子串替换为str2,两者的时间复杂度为O（str.length())

    */
}

int string_access1()  //通过下标访问
{
    string str = "abcd";
    for (int i = 0; i < str.length(); i++)   //string size和length都可以
        printf("%c", str[i]);

    //若是要读入和输出整个字符串，则只能使用cin和cout，无法使用printf
    cin >> str;
    cout << str;
    //若要使用printf来输出string，则用c_str()将string类型转化为字符数组来输出
    printf("%s", str.c_str());
}

int string_access2()  //通过迭代器访问
{
    //一般使用下标即可满足访问的要求，但有些函数比如insert和erase则要求以迭代器为参数，因此还要学
    //由于string不像其他STL容器那样需要参数，因此可以直接如下定义
    string::iterator it;

}

int my_string_nops() {
    if (string::npos == -1)
        cout << "-1 is true " << endl;
    if (string::npos == 4294967295)
        cout << "4294967295 is also true" << endl;
}

int my_set_find() {
    string str = "thank you for smile";
    string str2 = "you";
    string st3 = "me";
    if (str.find(str2) != string::npos)
        cout << str.find(str2) << endl;  //若找到则返回子串
    if (str.find(str2, 7) != string::npos)
        cout << str.find(str2, 7) << endl;
}

int my_map() {
    /*map翻译为映射，可以将任何基本类型（包括STL容器）映射到任何基本类型（包括STL容器）
     * 掌握hash_table的用法，map可解决过大，导致不能使用hash_table的情况
     */
    //map<typename1,typename2>mp;单独定义一个map，map需要确定映射前类型（键key)和
    //映射后的类型（值 value）
    map<string, int> mp;  //如果是字符串到整形的映射，必须使用string 而不能用char数组
    map<set<int>, int> np;

    //两种访问方式，下标和迭代器
    //map中的键是惟一的，会被覆盖
    map<string, int>::iterator it;//map的迭代器定义与其他迭代器相同
    //但是迭代器的使用和其他迭代器不同，因为map的每一对映射都有两个typename，这决定了必须通过
    //一个it来同时访问键和值，事实上，map可以使用it->first 来访问键，使用it->second来访问值
    map<char, int> qp;
    qp['m'] = 20;
    qp['r'] = 30;
    qp['a'] = 40;
    for (map<char, int>::iterator it = qp.begin(); it != qp.end(); it++)  //STL的迭代器基本都这样使用
        printf("%c %d", it->first, it->second);
    /*map会以键从大到小的顺序自动排序，这是由于map内部是使用红黑树实现的（set也是),在建立映射的过程中会自动实现从大到小的排序功能
     map 常用函数
     1) find(key)返回键为key的映射的迭代器，时间复杂度为O（logN)
     erase()函数的参数都是迭代器，可进行点删除和区间删除
        erase(it),it为需要删除的元素的迭代器，时间复杂度为O（1）
        erase（key).key 为欲删除的映射的键，时间复杂度为O（logN)
        erase(first,last)
    size,clear

     map的常见用法：
     1）需要建立字符（或字符串）与整数之间映射的题目，使用map可以减少代码量
    2）判断大整数或者其他类型数据是否存在的题目，可以把map当成bool数组用
     3）字符串和字符串的映射也有可能会遇到
     4）map的键和值是唯一的，而如果一个键需要对应多个值，就只能用multimap，另外，还增加了
     unordered_map,以散列代替map内部的红黑树实现，使其可以用来处理只映射而不按key排序的需求，
     速度比map要快得多
    */
}

int map_find_erase() {
    map<char, int> mp;
    mp['a'] = 10;
    mp['b'] = 20;
    mp['c'] = 30;
    map<char, int>::iterator it = mp.find('b');
    printf("%c", it->first, it->second); //先是键，后是值
    mp.erase(it); //删除 b 20
    //mp.erase('b');
    for (map<char, int>::iterator it = mp.begin(); it != mp.end(); it++)
        printf("%c %d", it->first, it->second);
}

int my_queue() {
    /*queue 翻译为队列，在STL中主要则是实现一个先进先出的容器，可按人排队这种模型理解，由于queue本身是个先进先出的限制性数据结构
     * 在STL中只能通过front（）来访问队首元素，或是通过back（）来访问队尾元素
     *常用函数：
     * 1）push，将元素进行入队，front，back
     *2）pop，令队首元素出队，
     * 3）empty（）判断queue是否为空
     * 4）size
     *
     * queue常用的用途：
     * 1）当需要实现广度优先搜索时，可以不用自己手动实现一个队列，而是用queue来代替，以提高程序的准确性
     * 2）使用front，和pop函数前，必须用empty（）判断队列是否为空，否则可能因为队空而出现错误
     * 3）STL中还有两种容器跟队列有关，分别是双端队列（deque)和优先队列（priority_queue），前者是首尾皆可
     * 插入和删除的队列，后者是使用堆实现的默认将当前队列最大元素置于队首的容器
     */
    queue<int> q;  //queue的定义，STL里中的typename可以是基础数据类型或者其他STL容器
}

int queue_access() {
    queue<int> q;
    for (int i = 1; i <= 5; i++)
        q.push(i);
    printf("%d %d", q.front(), q.back());

}

int my_priority_queue() {
    /*priority_queue又称为优先队列，其底层是用堆来进行实现的，在优先队列中，队首元素一定是
     * 当前队列中优先级最高的那一个，可以在任何时候往优先队列里面push元素，而优先队列底层的数据结构
     * 堆（heap）会随时调整结构，使得每次的队首元素都是优先级最大的
     *常用函数：
     * 1）push，时间复杂度O（logN)
     * 2)pop,empty,size
     */

    priority_queue<int> q;  //和队列不一样的是，优先队列没有front，back函数，而只能通过top()来
    //访问队首元素（也可以称为堆顶元素），也即是优先级最高的元素
}

/*
 * 优先队列优先级的设置（基本数据类型）
 *此处指的是int，double，char等，优先队列对他们的优先级设置一般是数字大的优先级越高，因此队首元素就是优先
 * 队列内元素最大的那个（char，则是字典序最大的），对基本数据类型来说，下面两种优先队列的定义是等价的（int为例，注意最后>>之间有一个空格
 *
 * 常见用途：
 * priority_queue可以解决一些贪心问题，也可以对dijkstra 算法进行优化（因为优先队列的本质是堆
 * 需要注意的是，使用top函数前 ，必须用empty判断优先队列是否为空
 *
 */
int my_priority_basic_data_type() {
    /*
     * 可以看出来第二种定义方式的尖括号内多出了两个参数：其中vector<int>填写的是承载底层数据结构堆的容器
     * 如果第一个参数是double或char,则此处只需要填写vector<double>,vector<char>,最后一个参数less<int>
     * 则是对第一个参数的比较类，less<int>表示数字大的优先级越大，而greater<int> 表示数字小的优先级越大
     */
    priority_queue<int> q;
    priority_queue<int, vector<int>, less<int> > p;
}

struct fruit {
    string name;
    int price;

    friend bool operator<(fruit f1, fruit f2) {
        return f1.price < f2.price;  //运算符重载

    };
} f1, f2, f3;    //优先队列的这个函数与sort中的cmp函数的效果是相反的
//如果结构体内的数据较为庞大（例如出现了字符串或者数组）。建议使用引用来提高效率，此时比较类的参数中需要加上“const”，“&”，比如这样
struct fruit1 {
    friend bool operator<(const fruit1 &f1, const fruit1 &f2) {};
};

int my_stack() {
    /*
     * stack 本身就是后进先出（类似子弹弹夹）的数据结构，stack只能使用top来访问栈顶元素
     * 常用函数：push，top，pop，empty，size，
     */
}

int my_pair() {
    /*
     * pair是一个很实用“小玩意”，当想要将两个元素绑在一起作为一个合成元素的，又不想因此定义结构体的使用，可以使用pair
     * pair 可以看做是一个内部拥有两个元素的结构体，且这两个元素的类型是可以指定的
     * 因此pair相当于如下代码
     * struct pair{
     *      typename first；
     *      typename second；
     * }；
     * pair的定义为pair<typename1，typename2>name;
     * pair 元素的访问，pair只有两个元素，分别first 和second，只需要按正常结构体的方式去访问
     * p.first ,p.second
     *
     * pair 比较操作数，可以使用< > 等 ，比较规则是先以first的大小作为标准，只有当first大小相等时才去比较second的大小
     *
     * pair的常见用途：
     * 1）用来代替二元结构体及其构造函数，可以节省编码时间
     * 2）作为map的键值对来进行插入，用法参照下面pair_map
     */
    pair<string, int> p;  //pair的定义，如果想在定义时进行初始化，则如下所示
    pair<string, int> p1("hahha", 5);

    /*若要临时构建一个pair，如下
    1)pair<string,int>("hahah",5)
     2)使用自带的make_pair函数  make_pair("hahh",5)
     */
}

int pair_map() {
    map<string, int> mp;
    mp.insert(make_pair("heihei", 5));
    mp.insert(pair<string, int>("haha", 5));
    for (map<string, int>::iterator it = mp.begin(); it != mp.end(); it++)
        cout << it->first << " " << it->second << endl;  //map的键和值  为first和second，记住访问方式

}

int my_algorithm() {
    /*
     * algorithm头文件的常用函数
     * max,min ,参数必须是两个，可以是浮点数，若要返回三个数的最大值，写法为max(x,max(y,z))
     * abs,返回绝对值，参数必须为整数，若是浮点型的绝对值，为fabs
     * swap(x,y)交换值
     * reverse(it1,it2)可以将数组指针[it1,it2)之间的元素或容器的迭代器[it1,it2)范围内的元素进行反转
     * next_permutation()给出一个序列在全排列中的下一个序列
     * fill（）可以把数组或容器中某一段区间赋为某个相同的值，和memset不同，这里的赋值可以是数组类型对应范围内中的任意值
     * sort（）：
     *      sort（首元素地址(必填)，尾元素地址的下一个地址（必填），比较函数(非必填，默认递增)）
     *      第三个函数就是compare函数(一般写作cmp函数），用来实现这个规则
     *
     *
     * sort函数cmp的实现
     * 1）基本数据类型数组的排序，默认升序，如果要让大小关系反过来，则要告诉cmp函数，如下sort_cmp_basic
     *      从小到大排序，用“<”
     *      从大到小，用“>”
     * 2）结构体数组的排序
     */
}

bool cmp(int a, int b) {
    return a > b;
}

int sort_cmp_basic()        //这样即可降序
{
    int a[] = {3, 1, 4, 2};  //C++的数组应该这样定义
    sort(a, a + 4, cmp);
}



