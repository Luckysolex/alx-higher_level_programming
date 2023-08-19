-- Command to select record from second_table
-- score should be >= 10
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
