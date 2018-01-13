-- 子查询，注意表名的区分。

SELECT e.Name AS Employee FROM Employee e WHERE e.Salary > (SELECT me.Salary FROM Employee me WHERE me.Id = e.ManagerId);

-- 或者使用自联结

SELECT
     a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary;