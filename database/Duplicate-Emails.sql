-- 分组和聚合，可以按照EMAIL分组，这样相同的就是一组，然后count大于1的就是在数据库中有重复的记录。
-- 刚开始我的思路是自联结，但是最后还是需要GROUP BY，而且这样查询很low

SELECT p.Email FROM Person p JOIN Person po ON p.Email = po.Email AND p.id != po.id GROUP BY p.Email;

-- 比较好的方法，要注意筛选条件有聚合函数的时候，需要使用HAVING子句而不是WHERE

SELECT Email FROM Person GROUP BY Email HAVING COUNT(*) > 1;