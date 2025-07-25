-- 9-cities_by_state_join.sql
-- List all cities with their state names using a JOIN

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
