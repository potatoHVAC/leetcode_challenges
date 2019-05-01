# Duplicate Emails
# https://leetcode.com/problems/duplicate-emails/
# Completed 5/1/19

SELECT DISTINCT(Email) 
FROM Person 
WHERE id not in (
    SELECT MIN(id) as id 
    FROM Person 
    GROUP BY email
);
