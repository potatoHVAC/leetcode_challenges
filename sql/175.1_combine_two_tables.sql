# Combine Two Tables
# https://leetcode.com/problems/combine-two-tables/
# Completed 5/1/19

SELECT Person.FirstName, Person.LastName, Address.City, Address.State
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId
;
