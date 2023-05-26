DROP DATABASE IF EXISTS test_db;
CREATE DATABASE test_db;
USE test_db;

DROP TABLE IF EXISTS user;

CREATE TABLE user (id INT, name VARCHAR(10));

INSERT INTO user (id, name) VALUES (1,"tama");
INSERT INTO user (id, name) VALUES (2,"pochi");
INSERT INTO user (id, name) VALUES (3,"ten");
INSERT INTO user (id, name) VALUES (4,"yume");
INSERT INTO user (id, name) VALUES (5,"momo");