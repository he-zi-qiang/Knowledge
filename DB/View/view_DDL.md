
![alt text](image.png)
[toc]
## 视图DDL
### 视图的创建
```sql
create view c_g(sno,c_num,avg_grade)
//视图中的列的使用名称
as 
select sno,count(*),avg(grade)
from sc
where grade is not null
group by sno
（with check option）
//保证更新插入或删除时的行满足视图where子句的表达式，提交修改后仍可通过视图看到数据
```
### 视图的修改
```sql
alter view v_ma
as 
select_statement
```
### 视图的删除
```sql
drop view v_ma
```