//本文以小写英文书写，更直观
![alt text](image.png)! ![alt text](image-1.png)
[toc]
## 声明游标
```SQL
declare s_cur insensitive// 
declare s_cur forward_only// 游标不支持滚动，只能从头到尾顺序提取
declare s_cur scroll// 游标可以进行滚动操作
for
read only //只读游标
update of//指定游标内可以更新的列

```
## 打开游标
```SQL
open s_cursor
```
## 读取游标
```SQL
fetch next//读取当前行的下一行，并挪到下一行
fetch prior//读取当前行的上一行，并挪到上一行
fetch first//读取结果集的第一行，并设此为当前行
fetch last  //读取结果集的最后一行，并设此为当前行
fetch absolute n //n为正，读取结果集头部开始的第n行，并将返回行为当前行
fetch relative n //n为正，读取当前行之后的第n行，并将返回行为当前行
from
into    //把读取的数据放入入多个变量里
@@fetch_status//全局变量返回上次执行fetch命令的状态
//0 成功 -1 失败或不在结果集里 -2 读取的行不存在
```
## 关闭游标
```SQL
close s_cursor
```
## 释放游标
```SQL
deallocate s_cursor
```
//游标s_cur读取学生表中男同学的信息，并将第三个男同学的专业改为机械
```SQL
declare s_cur scroll cursor 
for 
select * 
from S
where sex='男'
open s_cur
fetch absolute 3 from s_cur
update S
set sdept='机械'
where current of s_cur
close s_cur
deallocate s_cur
```
//声明一个查询王姓学生姓名和系的游标
```SQL
declare @sname char(10),@sdept varchar(20)
declare sname_cur scroll cursor 
for
select sname,sdept 
from S
where sanem like '王%'
open sname_cur
fetch next from sname_cur into @sname,@sdept
while @@fetch_status=0
begin
print @sanme+@sdept
fetch next from sname_cur into @sname,@sdept
end
close sname_cur
deallocate sname_cur
```