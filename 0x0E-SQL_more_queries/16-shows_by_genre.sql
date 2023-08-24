-- A script that lists all shows, and all genres linked to that show
-- Results are in ascending order by the show title and genre name
SELECT t.`title`, g.`name`
FROM `tv_shows` AS t
	LEFT JOIN `tv_show_genres` AS ts
	ON t.`id` = ts.`show_id`

	LEFT JOIN `tv_genres` AS g
	ON ts.`genre_id` = g.`id`
ORDER BY t.`title`, g.`name`;
