-- CASE表达式，判断逻辑，聚合函数，仔细点

SELECT 
    CASE
        WHEN id % 2 = 1 AND id != counts THEN id + 1
        WHEN id % 2 = 1 AND id = counts THEN id
        ELSE id - 1
    END id, student
FROM
    seat, (SELECT COUNT(*) AS counts FROM seat) AS seat_counts
ORDER BY id;