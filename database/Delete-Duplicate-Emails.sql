-- 删除的SQL语句是 `DELETE FROM` 或者指定 `DELETE * FROM`

DELETE p FROM Person p JOIN Person p1 ON p.Email = p1.Email AND p.Id > p1.Id;