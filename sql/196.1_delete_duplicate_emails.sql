# Delete Duplicate Emails
# https://leetcode.com/problems/delete-duplicate-emails/
# Completed 5/1/19

DELETE FROM Person
WHERE id NOT IN (
    SELECT id FROM (
        SELECT MIN(id) AS id
        FROM Person
        GROUP BY email
    ) as p1
);
    
