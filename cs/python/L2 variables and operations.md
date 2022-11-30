# 变量
##### 变量名要求：
```python
1. 只有 字母 数字 下划线 _
2. 字母开头
3. 避开关键字 True False 等等
```
## int 整型
```python
1. 加 减 乘 除 次方 + - * / **
2. 相除取整 //    相除取模 mod
3. 1_000_000 代表 1000000
```
## float 浮点型 (同上)

## string 字符串

```python
1. a = '123jins'  中间的内容是它的值
   b = "hello world"
2. 标准输出  <-----------重要---------------->
    a = 1
    b = 0.1
    c = "hello"
    
    output = "this is a = %d,b = %f,c = %s " % (a,b,c)
    print (output)
3. 字符串的操作
    "hello" + "world" 
    "helloworld"
4. 转义字符
    \n 换行
    \" 双引号内实现双引号
5. 多行字符串 ```  ```
6. len(str)  返回字符串长度
```
## bool 布尔型
```python
1.comparison 比较
    a = True
    b = False
    c = 1 > 2
    d = 1 == 2
    e = 1 != 2 
2. 逻辑运算 and or not 
```
## list 列表
```python
1. list = [1, 1.0, "hello", True]  可变
   tuple = (1, 1.0, "hello", True) 元组是常量不能变
2. 操作
     2.1 索引
        list[0] 第一个
        list[-1] 倒数第一
    2.2.1 切片
        list[0:-1] 左闭右开
    2.2.2 高级切片
        list[start:end:step] 同样是左闭右开 步长可以为负
        list[::-1] 倒序。           
    2.3.1 赋值
        list[0] = 1
        ps: 这里的赋值具有传递性
        e.g. 
        list1 = [1,2]
        list2 = list
        list2[0] = 100 之后 list1 也会被改成[100,2]
    2.3.2 隔离赋值
        list2 = list1.copy()
    2.4 追加元素
        list.append(item)
    2.5 插入元素
        list.insert(index,item)
    2.6 移除元素
        list.remove(item)
    2.6 删除元素
        del list[index]
    2.7 弹出最后一个元素
        list.pop()
    2.8 清空
        list.clear()
    2.9 +
        list3 = list1 + list2
    2.10 in 用于判断元素是否在列表之内
        bool = 1 in list1
```

## dictionary 字典 
```python
1. 无序的键值对的集合
    dict = {key1:value1,key2:value2...}
2. 操作
    2.1 获取值
        item1 = dict[key1]
    2.2 改变值
        dict[key1] = item1
    2.3 增加值
        dict[new_key] = new_value
    2.3 移除
        dict.remove[key]
        del dict[]
    2.4 清除
        dict.clear()
    2.5 复制
        dict2 = dict1.copy()
``` 