# Employees Earning More Than Their Managers
# https://leetcode.com/problems/employees-earning-more-than-their-managers/
# Completed 5/1/19

SELECT Name AS Employee
FROM (
     SELECT *
     FROM Employee
     INNER JOIN (
          SELECT id AS ManId, Salary AS ManagerSalary
     	  FROM Employee
     ) AS Manager
     ON Employee.ManagerId = Manager.ManId
     HAVING Employee.Salary > Manager.ManagerSalary
) AS BigMoney;
