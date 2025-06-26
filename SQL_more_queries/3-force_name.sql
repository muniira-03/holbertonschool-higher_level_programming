-- 3-force_name.sql
-- Creates the table force_name with NOT NULL name field.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
