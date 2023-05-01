#Q1. What is a database? Differentiate between SQL and NoSQL databases.
# What is a database?
# A database is a structured collection of data that is stored and organized in a way that allows for efficient retrieval, manipulation, and management. A database management system (DBMS) is a software system that is used to manage and manipulate databases. The DBMS provides tools for defining, creating, querying, updating, and administering databases.

# SQL databases
# SQL(Structured Query Language) databases are relational databases that are based on the relational model. In SQL databases, data is stored in tables, and the relationships between tables are defined using keys. SQL databases use SQL, a declarative query language, to manipulate and query data.

# NoSQL databases
# NoSQL(Not only SQL) databases are non-relational databases that are based on a variety of data models. NoSQL databases are designed to be highly scalable and flexible, and are often used for big data and real-time web applications.

#Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
#DDL is data definition language. It is a set of SQL commands used to define and manipulate the structure of a database. DDL statements are used to create, modify, and delete database objects such as tables, indexes, views, and procedures.#DDL is data definition language. It is a set of SQL commands used to define and manipulate the structure of a database. DDL statements are used to create, modify, and delete database objects such as tables, indexes, views, and procedures.

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

#CREATE
## The CREATE statement is used to create new database objects such as tables, indexes, views, and procedures. Here's an example of how to create a new table:
mycursor.execute("CREATE DATABASE if not exists Assignment")

mycursor.execute("CREATE TABLE Assignment.test_table(c1 INT , c2 VARCHAR(50) , c3 FLOAT , C4 VARCHAR(50))")

#ALTER
# The ALTER statement is used to modify an existing database object such as a table, index, view, or procedure. Here's an example of how to add a new column to an existing table:
mycursor.execute("ALTER TABLE Assignment.test_table ADD COLUMN C5 INT")

#TRUNCATE
# The TRUNCATE command deletes all the data inside a table.
mycursor.execute("TRUNCATE TABLE Assignment.test_table")

#DROP
# The DROP statement is used to delete an existing database object such as a table, index, view, or procedure. Here's an example of how to drop a table:
mycursor.execute("DROP TABLE Assignment.test_table")
mydb.close()

#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.

# DML stands for Data Manipulation Language, which is used to manipulate the data stored in a database. It includes operations such as inserting, updating, and deleting data
# INSERT: This statement is used to insert new rows of data into a table. 
# UPDATE: This statement is used to modify existing data in a table. 
# DELETE: This statement is used to delete data in the table

#Q4. What is DQL? Explain SELECT with an example.

# DQL(Data Query Language) is used to retrieve data from a database. The most commonly used DQL command is SELECT, which retrieves data from one or more tables in a database.

#Q5. Explain Primary Key and Foreign Key.

# In a relational database, a primary key is a unique identifier for a row in a table. It is a column or a combination of columns that uniquely identifies each row in the table. Primary keys ensure that each row in a table is unique and identifiable.
# A foreign key, on the other hand, is a column in a table that refers to the primary key of another table. It is used to establish a relationship between two tables in a database. The foreign key column in one table contains values that match the primary key column in another table. This relationship is known as a referential integrity constraint, and it ensures that the data in the two tables is consistent.

#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

# We then create a cursor object using the cursor() method of the database connection object. The cursor is used to execute SQL statements and fetch the results.
# The execute() method of the cursor object is used to execute a SQL statement. It takes a SQL statement as a parameter and returns the number of affected rows.

#Q7. Give the order of execution of SQL clauses in an SQL query.

# FROM clause: This clause specifies the table(s) from which the data will be selected.
# JOIN clause: This clause is used to combine data from two or more tables based on a related column between them.
# WHERE clause: This clause is used to filter data based on a specific condition.
# GROUP BY clause: This clause is used to group data based on one or more columns.
# HAVING clause: This clause is used to filter data based on a specific condition after the data has been grouped using the GROUP BY clause.
# SELECT clause: This clause is used to select the columns to be retrieved from the table(s).
# DISTINCT clause: This clause is used to retrieve unique values of a column.
# ORDER BY clause: This clause is used to sort the result set based on one or more columns.
# LIMIT clause: This clause is used to limit the number of rows returned by the query.