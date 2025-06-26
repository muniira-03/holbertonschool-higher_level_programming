-- 6-states.sql
-- Creates database hbtn_0d_usa and a table states with auto-increment id.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
