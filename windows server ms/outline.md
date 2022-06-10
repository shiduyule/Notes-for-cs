## 总体流程
![](images/2022-05-09-19-52-30.png)
>1.搭建基底，对基地进行结构优化，计算基底能量

>2.优化吸附部分，计算吸附部分的能量

>3.搭建吸附模型，计算吸附部分的能量

一.
```bash
1.build --> surfaces -->  cleave surface 选择101  厚度再选的厚一点，两倍的厚度

2.build --> symmetry -->  supercell  扩成 3 乘 3

3.build --> crystal --> build vacuum slab  加上个15埃

4.Dmol3 Calculation --> 
	setup       task:geometry optimization //quality:customized // fuctional:GGA PBE
	electronic  basis set: DND // basis file:3.5
	properties  全不选

```
