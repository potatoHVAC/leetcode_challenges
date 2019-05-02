# Customers Who Never Order
# https://leetcode.com/problems/customers-who-never-order/
# Completed 5/1/19

SELECT Name AS Customers
From Customers AS customer_table
WHERE id NOT IN (
    SELECT DISTINCT(CustomerId)
    FROM Orders
);
