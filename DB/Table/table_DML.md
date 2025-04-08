//本文以小写英文书写，更直观
![alt text](image-1.png)
[toc]
# 表中的数据更新 
//多条DML用；号隔开
## 插入表数据 insert
```SQL
use tms
go
insert into S
values('20181103','姜鹏飞','男',1998,'交通','交通18');
go
```

## 修改表数据 update
```SQL
use tms
go
update SC  //指定更新的表
set grade =85   //更新数据
where sno='20180001'and cno='0121';  //确定更新数据的位置
go
```

## 删除表数据 delete
```SQL
use tms
go
delete from SC;  
delete S
where sname='张坤'；
go
```