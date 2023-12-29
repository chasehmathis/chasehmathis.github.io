SELECT A.name AS Customers FROM Customers A
WHERE A.id NOT IN(SELECT B.customerId FROM Orders B)
