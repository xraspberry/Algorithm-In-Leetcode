-- 日期相加函数`DATE_ADD(CURRENT_DATE(), INTERVAL 5 DAY)`

SELECT Id FROM Weather w WHERE w.Temperature > (SELECT w1.Temperature FROM Weather w1 WHERE w1.Date = DATE_ADD(w.Date, INTERVAL -1 DAY));