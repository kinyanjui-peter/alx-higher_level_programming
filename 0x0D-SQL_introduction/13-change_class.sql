-- script that removes all records with a score <= 5 in
--the table second_table of the database hbtn_0c_0 in your MySQL server.

--The database name will be passed as an argument of the mysql command


DELETE FROM hbtn_0c_0.second_table WHERE score <= 5;
SELECT * FROM hbtn_0c_0.second_table;
