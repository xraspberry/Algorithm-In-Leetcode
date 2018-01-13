-- 联结，子查询

SELECT
    d.Name AS Department, e.Name AS Employee, e.Salary AS Salary
FROM (SELECT DepartmentId, MAX(Salary) AS Salary FROM Employee GROUP BY DepartmentId) n1 JOIN Employee e JOIN Department d
    ON n1.DepartmentId = d.Id AND e.DepartmentId = d.Id AND n1.Salary = e.Salary;