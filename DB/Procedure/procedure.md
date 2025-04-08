//本文以小写英文书写，更直观
![alt text](image.png)
[toc]
# 存储过程
## 预备知识
### 变量    //只讨论局部变量
#### 变量的声明 declare
```SQL
declare @x int  //声明一个int型的局部变量 X
```
#### 变量的赋值 set select
```SQL
declare @X int, @Y int,@Z int,@var1 varchar(20)
set @X=100
set @Y=200
set @Z=@X+@Y

select @var1='王珊'     //属于增加列，无列名，会在结果中显示
select @var1 as 'name'  //把无列名改为name
```
### 流程控制
#### if...else
#### while
#### begin..end
#### return
#### case
## 创建存储过程 （变量的应用）
```SQL
//查询某位同学某门课的成绩
create procedure pv_grade   //创建名为 pv_grade的存储过程 
@s_name char(20),@c_name varchar(20)='软件工程',@s_grade real output
// 声明输入参数（执行时未输入实参，则使用默认参数，有实参，则覆盖默认参数），output指示参数为输出参数，所以要有个实参来保存输出参数
as      //写SQL语句
select @s_grade=grade
from S join SC on s.sno=sc.sno
join C on sc.cno=c.cno
where sname=@s_name and cname=c_name
```
## 执行存储过程
```SQL
declare @s_grade real   //创建实参@s_grade
exec pv_grade '王珊','数据库原理与应用',@s_grade output
//参数写入顺序格式要和定义一样
print '王珊的数据库成绩为：'+str(@s_grade)   
//因为print后面只能加 字符串表达式 函数名 局部变量名 所以要用str（）函数把real类型改为string
```
## 查看存储过程
```SQL
exec sp_helptext pv_grade   //查看存储过程的内容
exec sp_help pv_grade          //查看存储过程的名称 拥有者 类型和时间
```
## 修改存储过程
```SQL
alter procedure 
```
## 删除存储过程 drop
```SQL
drop procedure ps_grade
```