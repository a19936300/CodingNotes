1. 索引结构
b+树
```
https://blog.csdn.net/zhuanzhe117/article/details/78039692
```

hash
```
https://www.cnblogs.com/juicejuice/p/14705277.html
```

2. 最左侧匹配
   1. 经常被查区分度高的做索引
   2. 最左侧原则
   3. 回盘排序
   4. 覆盖索引
   5. 小表驱动大表


3. explain工具

关键字：

type:
system > const > eq_ref > ref > fulltext > ref_or_null > index_merge > unique_subquery > index_subquery > range > index > all
至少到range

extra:
Using filesort :表示mysql会对结果使用一个外部索引排序，而不是从表里按索引次序读到相关内容，可能在内存或者磁盘上进行排序，mysql中无法利用索引完成的排序操作成“文件排序”
Using temporary: 表示Mysql在对查询结果排序时使用临时表，常见于排序order by和分组查询group by