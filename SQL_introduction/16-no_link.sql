-- Script to select only rows with non-empty name values, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
