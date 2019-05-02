# Employees Earning More Than Their Managers
# https://leetcode.com/problems/employees-earning-more-than-their-managers/
# Completed 5/1/19
# Copied logic from discussion section

SELECT Employee1.Name as Employee
FROM Employee AS Employee1, Employee AS Employee2
WHERE Employee2.Id = Employee1.ManagerID
AND Employee2.Salary < Employee1.Salary
;
	
