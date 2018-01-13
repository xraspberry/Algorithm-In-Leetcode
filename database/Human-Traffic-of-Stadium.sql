-- 这道题，首先要找到三个或者以上连续大于100的行，那么至少得找三行其人数大于100，至于4行，5行或者更多的行，那么可以通过这三行来组合，比如4行，1，2，3，4，那么1，2，3首先是可以找到的，那么下面会找到2，3，4。只要来一个选项，DISTINCT就可以输出,1,2,3,4。

select distinct t1.*
from stadium t1, stadium t2, stadium t3
where t1.people >= 100 and t2.people >= 100 and t3.people >= 100;

-- 现在来考虑下可能的情况，在连续三行中，t1可能在的位置有三个，那么对这三个位置分别写入筛选条件，这样就可以将所有的可能的行都查询出来。因为SELECT的是`t1.*`

SELECT DISTINCT t1.* FROM stadium t1 JOIN stadium t2 JOIN stadium t3 
    ON t1.people >= 100 AND t2.people >= 100 AND t3.people >= 100
WHERE (
    t1.id = t2.id - 1 AND t2.id = t3.id - 1 OR
    t1.id = t3.id - 1 AND t2.id = t1.id - 1 OR
    t2.id = t3.id - 1 AND t3.id = t1.id - 1
) ORDER BY id;