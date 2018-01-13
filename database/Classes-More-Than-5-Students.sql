-- 看到这种题就是分组聚合，不过这题有毒，居然student列可以重复。。那么可以指定对分组的不同值计数，指定DISTINCT参数

SELECT class FROM courses GROUP BY class HAVING COUNT(DISTINCT student) >= 5;