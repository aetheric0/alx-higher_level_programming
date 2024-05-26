-- Imports a Table from an sql file
-- run with command:
SOURCE temperatures.sql;
SELECT `city`, `value` AS avg_temp FROM temperatures ORDER BY `avg_temp` DESC;
