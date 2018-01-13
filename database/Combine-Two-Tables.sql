-- 就是简单的左联结。
SELECT FirstName, LastName, City, State from Person LEFT JOIN Address ON Person.PersonId = Address.PersonId;