# Not Boring Movies
# https://leetcode.com/problems/not-boring-movies/
# Completed 5/8/19

SELECT *
FROM cinema
WHERE (id%2) != 0 AND LOWER(description) NOT LIKE '%boring%'
ORDER BY rating DESC;
