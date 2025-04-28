```python
input_str=input()   #  将输入赋给input_str
word = input_str.strip().split(' ')  # .strip() 不依赖第三方库 
print(len(word[-1]))
```


```python
移除字符串开头和结尾的空白字符（如空格、换行符 \n、制表符 \t 等）
text = "   Hello World   \n"
stripped_text = text.strip()  # 结果: "Hello World"

扩展
text = "xxxyHello Worldxxx"
stripped_text = text.strip("x")  # 结果: "yHello World"
```


```python
text = "apple,banana,orange"
parts = text.split(",")  # 结果: ["apple", "banana", "orange"]

```



读取变量：
python   的变量读取是逐行读取    的，
input() 