# Lecture 1.2 different programming languages
## assembly languages 
- are more human readable compared to binary instructions for CPU
## C 1969~1972
## C++ 1979
- as an extension of the programming language
- C with classes
- Now it is C++++++++++++
## java  1995
- i hate memory management in C/C++, java use automatic memory management  
- i want "write once, run anywhere", not "write once complie anywhere"  
- grammar is similar with C++  
- A java compiler generates *.class files, not executable files
## python 1990
- i hate strict grammar
- i hate too many data types
## scrach 2002
- i do not like to type a keyboard
## advantages of C/C++
- Development language of most fundemantal computer system
1. linux windows 操作系统
2. MySQL 数据库系统
3. OpenCV  计算机视觉库
4. backend of Tensorflow , PyTorch 深度学习的框架底层的模块还是C/C++
- high efficiency  高效率
1. widely optimized compilers  编译器好
2. access memory directly  直接访问内存
3. excellent on computing   
4. important language for AI algorithm implementation







# Lecture 1.3: Compile and link 
```C
#include <iostresm>
using namespace std;
int mul (int a, int b)
{
    return a * b
}
int main()
{
    int a, b;
    int result;
    cout << "Please input two integers:";
    cin >> a;
    cin >> b;

    result = mul(a,b);
    cout <<

}
```
![](images/2023-04-08-22-24-48.png)

先将源文件编译成.o 文件  之后再将 .o 文件链接成 可执行文件
## we have two types files  .cpp and .hpp
- mul.cpp have statements and body of functions
- mul.hpp only have statements of functions
- main.cpp have main functions

> steps to run a cpp program
```bash
compile
$ g++ -c main.cpp
$ g++ -c mul.cpp

link
$ g++ main.o mul.o -o mul
```


# Lecture 1.4: Preprocessor



# Lecture 1.5: Simple input and output

