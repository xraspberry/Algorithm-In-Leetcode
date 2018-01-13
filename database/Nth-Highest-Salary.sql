-- 这道题有几个知识点

-- 创建自定义函数的语法
-- `DECLARE variable_name type` 声明一个变量
-- `SET variable_name=expression` 为变量设置值
-- `LIMIT 2, 1` 其中第一个参数指的是结果集的开始记录位置，第二个参数是结果集中包含的记录数，记录位置从0开始。

-- 所以该题的解法如下：

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1 
  );
END