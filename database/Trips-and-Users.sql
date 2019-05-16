-- 表的联合。主要在于如何计算比例，使用了条件逻辑。

SELECT t.Request_at AS Day, ROUND(SUM(CASE WHEN t.Status like 'cancelled%' THEN 1 ELSE 0 END) / COUNT(*), 2) AS 'Cancellation Rate'
FROM 
    Trips t JOIN Users u ON t.Client_Id = u.Users_Id 
WHERE 
    u.Banned != 'Yes' AND t.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.Request_at;