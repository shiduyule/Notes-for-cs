```python
three control structures
1. sequence structure 顺序结构  正常的代码就是
3. selective /condition 选择结构 if条件语句
3. cycle  loop 循环结构 while for
```

```python
if 
    注意缩进 同一个缩进代表同一级
    if (condition):
        block1
    else:
        block2
```

```python
2.1 while
    2.1.1 定义
    while condition：
        block
        change used to stop loop
    
    2.1.2 中断
    break + continue
        if condition:
            break 全局中断
        if condition:
            continue 跳出本次循环 

2.2 for 
    2.2.1 range function
        for i in range (number):
            print(list[i])
    2.2.2 do it with for
        for x in list:
            print(x)
```



```python
three useful templates
for i in range (N):
    do something using "i" as index 


i = 0
while i < N:
    do something using i as index:
    change the cycle variable


do something with every element in the sequence data
    for representator in sequence_data:
        do something with the represenetation
```

```python
with 语句作为try/finally 编码范式的一种替代,
 适用于对资源进行访问的场合，
 确保不管使用过程中是否发生异常都会执行必要的”清理”操作，释放资源，
 比如文件使用后自动关闭、线程中锁的自动获取和释放等

```

```python
 with open(file, "w") as f:
        f.write("hello python")
```
open 方法的返回值赋值给变量 f，当离开 with 代码块的时候，系统会自动调用 f.close() 方法， with 的作用和使用 try/finally 语句是一样的