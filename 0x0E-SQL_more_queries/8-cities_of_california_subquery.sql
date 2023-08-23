-- A script that lists all the cities of California
-- Results are in ascending order of ID
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN
	(SELECT `id`
		FROM `states`
		WHERE `name` = "California")
ORDER BY `id`;
