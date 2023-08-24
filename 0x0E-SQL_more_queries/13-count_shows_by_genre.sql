-- A script that lists all genres from hbtn_0d_tvshows
-- Records are in descending order of number of shows
SELECT g.`name` AS `genre`,
	COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS g
	INNER JOIN `tv_show_genres` AS t
	ON g.`id` = t.`genre_id`
ORDER BY g.`name`
ORDER BY `number_of_shows` DESC;
