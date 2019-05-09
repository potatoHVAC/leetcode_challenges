# Big Countries
# https://leetcode.com/problems/big-countries/
# Completed 5/8/19

SELECT name, population, area
FROM World
WHERE population > 25000000 OR area > 3000000
;
