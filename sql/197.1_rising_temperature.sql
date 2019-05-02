# Rising Temperature
# https://leetcode.com/problems/rising-temperature/
# Completed 5/1/19

SELECT weather_1.id
FROM Weather AS weather_1
INNER JOIN weather AS weather_2
WHERE Datediff(weather_1.RecordDate, weather_2.RecordDate) = 1
AND weather_1.Temperature > weather_2.Temperature
;
