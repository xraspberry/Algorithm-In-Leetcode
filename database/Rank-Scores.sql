-- 这道题想了许久，其实就是找到比当前行分数大的行数

SELECT s2.Score, (
    SELECT COUNT(DISTINCT s1.Score) + 1 
    FROM Scores s1 
    WHERE s1.Score > s2.Score
) AS Rank 
FROM Scores s2 
ORDER BY s2.Score DESC;