-- run with cmd line: cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
-- ALTERS DATABASE encoding to UTF-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table MODIFY COLUMN `name` VARCHAR(256) COLLATE utf8mb4_unicode_ci;
