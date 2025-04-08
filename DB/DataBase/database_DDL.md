//本文以小写英文字母书写，因为直观
![alt text](image.png)





 [toc]
# 数据库的创建
## 数据库的创建 create
 ```SQL
 create database tms
 on    //定义数据库文件
 primary   //定义主数据文件
 (
    name = tms,    //逻辑名称必须为一，且符合标识符规则
    filename='D:\tms\data\tms.mdf',
    size=5,     //定义文件初始大小，默认单位MB
    filegrowth=10%   //定义文件的递增方式
 )
 log on    //定义事务日志文件
 (
    name =tms_log,
    filename= 'D:\tms\data\tms_log.ldf',
    size=2,
    maxsize=100,  //设置数据库允许达到的最大长度，默认unlimited
    filegrowth=2
 )
 ```
## 数据库的查看
 ```SQL
 use tms 
 go
 exec sp_helpdb tms     //运用指定存储过程查看数据库信息
 go
 ```

## 数据库结构的修改  alter
### add 增加 file/log file/filegroup  
### modify 修改 file/filegroup/name
### remove 删除 file/filegroup
 ```SQL
use tms
go
alter database tms
add file(
   name = tms_dataT,
   filename='D:\tms\data\tms_dataT.ndf',
   size= 5,
   maxsize=50,
   filegrowth=1%
)
go
```
## 数据库的删除 delete
```SQL
use tms 
go
drop database tms 

go
```

