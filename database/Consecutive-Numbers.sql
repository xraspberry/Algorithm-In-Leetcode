-- 暴力解决方案

SELECT 
    DISTINCT l1.Num AS ConsecutiveNums 
FROM Logs l1 JOIN Logs l2 JOIN Logs l3
    ON l1.Num = l2.Num AND l2.Num = l3.Num AND l1.Id = l2.Id - 1 AND l2.Id = l3.Id - 1; 