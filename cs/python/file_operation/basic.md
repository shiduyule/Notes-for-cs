
```python
my_file = open(file, mode, buffering, encoding, errors, newline, closefd, opener)  # 打开文件
...  # 读写操作。省略

my_file.colse()  # 释放文件


open函数必须搭配.close()方法使用，先用open打开文件，然后进行读写操作，最后用.close()释放文件。open函数有八个参数，如下。

```

file：文件路径或文件描述符。如为文件路径则是str类型，如是文件描述符，则是一个非负整数。文件描述符使用较少，通常情况下都传入文件路径。file参数和closefd参数有关，closefd为True则file既可以传入文件路径，又可以传入文件描述符。closefd为False，则file只能传入文件描述符。这里的文件描述符应拓展理解为Unix、Linux系统的文件描述符和Windows系统的句柄。可以简单理解为，在Unix、Linux系统下叫文件描述符，在Windows系统下叫句柄。打开或新建文件时，操作系统内核会返回一个非负整数，可以用来访问指定文件，这个非负整数就是文件描述符。在Python中可以使用os模块的open函数获取其文件描述符。下面是一个例子。


mode：操作模式，可选，str类型，默认为r。可选值包括r、r+、w、w+、a、a+、x、x+、rb、wb、ab、xb、rt、at、wt、xt这16种。乍一看比较乱，其实很好理解。基本操作模式有四种，r、w、a、x，分别代表读、写、追加、创建新文件

t: 文本类型 (默认是rt 即只读文本 txt log csv)
b: 二进制类型




encoding：打开文件所用的编码，可选，str类型，默认为None。encoding参数仅可在采用文本方式（即mode值带t）读写数据的情况下有效，二进制方式下不可指定。文本编码有很多，常用的有utf-8、ascii、gbk等。mode参数采用文本方式的情况下，若encoding指定为None，则编码为locale.getpreferredencoding(False)这行代码的返回值。在Windows下，这行代码一般返回值为cp936,。cp936指的就是gbk


