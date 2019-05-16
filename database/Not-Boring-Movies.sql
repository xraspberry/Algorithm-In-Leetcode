-- 继续考察了筛选条件的使用

-- 取模：`%`或者`mod`函数
-- 字符串匹配: `%`匹配任意多字符，`_`匹配一个字符

SELECT * FROM cinema WHERE (SELECT id % 2) = 1 AND description NOT LIKE '%boring%' ORDER BY rating DESC;
SELECT * FROM cinema WHERE id % 2 = 1 AND description NOT LIKE '%boring%' ORDER BY rating DESC;
SELECT * FROM cinema WHERE mod(id, 2) = 1 AND description NOT LIKE '%boring%' ORDER BY rating DESC;