-- 查找两个关联的表，在一个表中没有，这种一般都是外联结。

SELECT Name AS Customers FROM Customers LEFT JOIN Orders ON Customers.Id = Orders.CustomerId WHERE Orders.CustomerId is NULL;

-- 或者可以使用子查询

SELECT Customers.Name as 'Customers'
FROM Customers
WHERE Customers.id not in
(
    SELECT CustomerId FROM Orders
);