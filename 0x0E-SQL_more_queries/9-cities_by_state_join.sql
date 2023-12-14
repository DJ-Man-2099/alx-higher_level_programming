-- create database if doesn't exist
SELECT cities.id,
	cities.name,
	states.name
from cities
	JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
