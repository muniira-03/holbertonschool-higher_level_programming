-- 5-unique_id.sql
-- Create table unique_id with id default 1 and unique constraint.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
