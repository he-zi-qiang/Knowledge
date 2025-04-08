//本文以小写字母来书写，因为小写字母很直观
![alt text](image.png)
[toc]
# 表结构的定义和修改
//多条DDL用，号隔开


## 1.数据库表的创建 create
### S表的创建
```SQL
use tms
go
create table  S
(
    sno char(10) 
    not null   
    constraint pk_sno primary key clustered
    check (sno like '201800[0-9][0-9]'),
    //列名sno 类型为char 列级完整性约束： 非空值约束not null 主键约束pk_sno 检查约束check
    //每个，号隔开的是每个列的设置完毕
    sname char(8) 
    not null,
    sex char(2),
    birthyear int,
    sdept varchar(20),
    sclass varchar(20)

)
go
```
### C表的创建
```SQL
use tms
go
create table C
(
    cno char(10)
    not null
    constraint pk_cno primary key clustered,
    cname varchar(20)
    not null,
    cnature varchar(20)
    check(cnature='必修'or cnature='选修'),
    credit char(2),
    precno char(4),
    cdept varchar(20),
)
go
```
### SC表的创建
```SQL
use tms 
go
create table SC
(
    sno char(10)
    not null,
    cno char(5)
    not null,
    grade real 
    null,
    primary key(sno,cno),
    //设置主键 sno cno
    foreign key(sno) references S(sno),
    //设置外键sno 参照S表中的sno
    foreign key(cno) references C(cno)
    //设置外键cno 参照C表中的cno
)
go
```
## 2.表结构的修改 alter  
### 修改列的定义 alter column
### 增加新列或约束 add /add constraint
### 删除新列或约束 drop column /drop constraint
```SQL
use tms 
go
alter table S

alter column sanme char(8) null
//删除表S中sname列不能取空值的约束
add addr char(30)
//增加一个地址列，类型为char（30）

go
```
## 3.删除表的定义 drop
```SQL
use tms
go
drop table S
go
```
