# Duplicate Emails
# https://leetcode.com/problems/duplicate-emails/
# Completed 5/1/19

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1
;
