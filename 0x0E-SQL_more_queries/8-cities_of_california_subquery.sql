-- create database if doesn't exist
SELECT id,
	name
from cities
WHERE (
		SELECT id
		from states
		WHERE (
				cities.state_id = states.id
				AND states.name = 'California'
			)
	)
ORDER BY cities.id;
