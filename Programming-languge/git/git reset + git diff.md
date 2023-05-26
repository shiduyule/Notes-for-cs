# git 撤销操作
## 只是修改 还没有 git add .
```bash
修改文件
$ git diff  查看修改之后的文件和暂存区文件的区别
$ git checkout <changed_file>  来恢复这个文件之前的状态
在新版本中可以使用 
$ git restore <changed_file>
```

## 修改完  并且 已经 git add .
```bash
$ git reset <changed_file>  将修改从暂存区移除 但是保存硬盘中的修改
或者git restore --staged <changed_file>  

$ git checkout HEAD <changed_files> 撤销掉所有修改 
// HEAD 表示最近一次的commit  这里也代表了init

```


## 已经 git commit 
```bash
$ git reset --soft HEAD~1  只是撤销commit
$ git reset HEAD~1 等价于使用 git reset --mixed HEAD~1
撤销commit  并且从暂存区拿掉
$ git reset --hard HEAD~1
撤销所有修改 包括在硬盘上的修改
```


## 如果想往回退两个commit 就将HEAD~1 改为 HEAD~2 以此类推

## git revert  反作用的commit  负commit
```bash
case 1
git revert HEAD   
git rever hash值   它的优势 可以撤销中间任意一个commit

case 2  推送到远端的公有分支
已经 git push 到远端的公有分支之后  公有分支本身只能增加commit 不能撤销commit  
不然别人的commit也会随之被撤销

这时候 只能使用 git revert 
git revert HEAD  +   git push 

case 3 推送到 远端的个人分支
可以使用
git reset --hard HEAD~1
git push  -f 
```