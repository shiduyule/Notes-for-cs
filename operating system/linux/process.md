```bash
ps (process status)  查看进程状态
D 不可中断 uninterruptible sleep (usually IO)
R 运行 runnable (on run queue)
S 中断 sleeping
T 停止 traced or stopped
Z 僵死 a defunct (”zombie”) process

-e  显示所有进程                            everyone 
-a 显示终端上的所有进程，包括其他用户的进程。  all
-f 全格式                                   full  
-h 不显示标题
-l 长格式。
-w 宽输出。

-r 只显示正在运行的进程。
-x 显示没有控制终端的进程。
```



```bash
ps -af|grep shiduyu
在所有进程中  通过正则表达式搜索是否含有该字符串的进程  
```


```bash
kill  
kill 默认等价于 kill 15 = sigterm
kill + PID 可以 中断指定进程
```