//本文以小写英文书写，更直观
![alt text](image.png)
[toc]
## 触发器的创建
```SQL
//返回删除学生个数DML触发器
create trigger del_count    //创建触发器的名字
on S                //在哪个表中
after delete        //在哪个操作
as 
declare @count varchar(50)
select @count =str(@@rowcount)+'个学生被开除'
select @count 
return ;
```
```SQL
//限制成绩的DML触发器
create trigger tri_limited
on SC
instead of insert
as
if not exists(
    select *from inserted
    where grade<0 or grade >200
)
insert into SC select * from inserted
else print'学生成绩不在0～100'
```
```SQL
//DDL触发器
create trigger tms_limited
on database
after drop_table,alter_table
as
print'不允许对教学管理数据库的表进行修改和删除'

```
## 触发器的查看
```SQL
exec sp_helptext del_count //查看触发器的内容
exec sp_help del_count  //查看触发器的名称 拥有者 类型 创建时间
exec sp_helptrigger SC  //查看特定表存在的触发器
```
## 触发器的修改
```SQL
alter trigger 
```
## 触发器的删除
```SQL
drop trigger del_count
```