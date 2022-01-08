# 准备条件

数据：150w
表：
```
create table tmp_table
(
    id int default 0 not null
        primary key,
    a  int           null,
    b  int           null,
    c  int           null,
    d  int           null,
    e  int           null,
    f  int           null
);

```

## 问题一：如果a索引，a,b索引，abc索引

1. a和b单独建立索引

explain select * from tmp_table where c = 92607 and a=7732;
type:index_merge  

2. 