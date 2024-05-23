-- run using: cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 
-- shows tables in a database passed as an argument from tty
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, 'John', 10), (2, 'Alex', 3), (2, 'Bob', 14), (4, 'George', 8);
