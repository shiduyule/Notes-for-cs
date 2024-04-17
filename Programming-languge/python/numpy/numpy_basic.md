### 数组格式
##### 数组维度 a.ndim 中括号的层数决定
##### 数组行数和列数 np.shape(data2d) (variable窗口的size)
```python 
Numpy.array 同质运算方便  
list中 数据的类型可以不一样  
维度的判定是中括号的层数

创建 numpy 数组 务必使用 np.array() 来声明变量类型 

0. 0D
a = np.array(1)  # 圆括号内部是a的真实值 array = 数组
a = [1]  

1. 1D
a = np.array([1,2,3]) 
a.ndim  　#　数组维度  

2. 2D  注意：数组的行数和列数可以不等 
a = np.array([
    [12,3,5,7],
    [11,2,4,6],
    [10,8,6,7]]) 

3. 3D 
a = np.array([
       [[ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9]],

       [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]],

       [[19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]]])
```


## 增
```python
生成指定范围内的一组有序的一维数组
t = np.linspace(0, 2 * np.pi, 1024)
t = np.linspace(起始值包括在内，结束值包括在内，采样数目=数组长度)  
步长 = (end - start)/num-1
t = np.arange(起始值，结束不包括，步长默认为1)
```
```python
生成空数组
x = np.empty([3,2], dtype = int) 
```
```python
随机生成数组
data2d = np.random.random((1000,1000))
```
```python
数组 升维度
x[:, np.newaxis]  放在后面，会给列上增加维度
x[np.newaxis, :]  放在前面，会给行上增加维度

data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
data
```
```python
数组 合并
array2D = np.array([data1,data2])
```


```python
数组整体计算
def function_theta_strain(x):
    a0 =   7.363e-05 
    a1 =  -8.187e-05 
    b1 =  -2.305e-05 
    a2 =   7.352e-06 
    b2 =   1.373e-05 
    a3 =   9.547e-07 
    b3 =  -1.768e-06 
    w =       1.798  
    S21output =  a0 + a1 * np.cos(x*w) + b1 * np.sin(x*w) + a2 * np.cos(2*x*w) + b2 * np.sin(2*x*w) + a3 * np.cos(3*x*w) + b3 * np.sin(3*x*w)
    return (S21output)

data2d = function_theta_strain(data2d)
```
## 查
```python
1. data1d[a,b] = 左闭右开  
2. 二维数组的切片
  data2d[:,0]  索引第一列  对于二维数组使用逗号

```
```python
3. 获取数组的大小
data2dshape = np.shape (data2d) 这是一个元组
i = data2dshape[1]   索引
j = data2dshape[2]   
```

# 改
```python
插入数组
a = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
b = np.array([2,5,8])
# 2代表下标，这里代表插入到第三列，axis=1，插入一列，axis=0，插入一行
a =np.insert(a, 2, b, axis=1)
# 2代表下标，这里代表插入到第三列，axis=1，axis=0，插入一行
a =np.insert(a, 2, b, axis=0)

#插入多列
c = np.array([[1,4,7],[2,5,8]]).T
np.insert(a, [0,1], c, axis=1)
 
输出：
[[1 2 2 3]
 [4 5 5 6]
 [7 8 8 9]]
 
[[1 1 2 2 3]
 [4 4 5 5 6]
 [7 7 8 8 9]]

```
```python
数组转置
t6 = t5.transpose()
二维数组  行翻转
data2d = data2d[::-1]
二维数组  列翻转
arr = np.fliplr(arr)
```



