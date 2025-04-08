![alt text](image.png)
[toc]
### 创建索引
```sql
create unique (clustered|nonclustered) index index_name
on sc(cno asc,grade desc)
```
## 删除索引
```sql
drop index i_cname on c
```