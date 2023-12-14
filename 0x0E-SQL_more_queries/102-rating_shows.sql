-- create database if doesn't exist
SELECT tv_shows.title,
	SUM(tv_show_ratings.rate) as rating
from tv_shows
	JOIN tv_show_ratings ON (tv_shows.id = tv_show_ratings.show_id)
GROUP BY tv_shows.title
ORDER BY rating DESC;
