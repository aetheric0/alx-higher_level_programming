-- Imports a Table from an sql file
-- run with command:
SOURCE temperatures.sql;
SELECT `city`, AVG(`value`) AS avg_temp FROM temperatures GROUP BY `city` ORDER BY `avg_temp` DESC;
