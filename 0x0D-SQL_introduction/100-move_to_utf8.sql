-- lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server
use hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table
MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
