# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
WHERE w1.temperature > (
    SELECT w2.temperature
    FROM Weather w2
    WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1
);