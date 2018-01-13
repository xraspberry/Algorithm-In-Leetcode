-- 这道题意思是在记录中找到第二大的记录，如果没有就是NULL。
-- 这里加DISTINCT的原因是，如果有两条300是最大的，然后有一条200，那么第二大的是200.
SELECT (
    SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1
) AS SecondHighestSalary;