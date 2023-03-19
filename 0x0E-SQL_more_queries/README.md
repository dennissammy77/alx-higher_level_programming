0x0E. SQL - More queries

Learning Objectives
How to create a new MySQL user
How to manage privileges for a user to a database or table
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve datas from multiple tables in one request
What are subqueries
What are JOIN and UNION

_How To Create a New User and Grant Permissions in MySQL_

To create a new user and grant permissions in MySQL, follow these steps:

Log in to the MySQL server using a user account that has administrative privileges. You can do this using the following command:
css
Copy code
mysql -u root -p
This will prompt you for the root user password.

Create a new user using the following command:
sql
Copy code
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
Replace "newuser" with the desired username and "password" with the desired password.

Grant privileges to the new user using the following command:
sql
Copy code
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
This grants all privileges to the user on all databases and tables in the MySQL server.

Flush the privileges to apply the changes using the following command:
Copy code
FLUSH PRIVILEGES;

_MySQL constraints_
Constraints are placed on columns or tables. They limit the data that can be inserted into tables.

We have the following constraints:

NOT NULL
UNIQUE
PRIMARY KEY
FOREIGN KEY
ENUM
SET
Other databases also have the CHECK constraint, which places a condition on a valid data. MySQL parses this constraint, but it is not enforced.

1. NOT NULL constraint:- A column with a NOT NULL constraint, cannot have NULL values.
CREATE TABLE People(Id INTEGER, LastName TEXT NOT NULL,
    ->                     FirstName TEXT NOT NULL, City VARCHAR(55));

2. UNIQUE constraint
The UNIQUE constraint ensures that all data are unique in a column.
CREATE TABLE Brands(Id INTEGER, BrandName VARCHAR(30) UNIQUE);

Basic query operation: the join
In SQL, the JOIN function is used to combine rows from two or more tables based on a related column between them. There are different types of JOINs available in SQL, including:

INNER JOIN: Returns only the matched rows from both tables.
LEFT JOIN: Returns all rows from the left table and matching rows from the right table, and NULL values for non-matching rows.
RIGHT JOIN: Returns all rows from the right table and matching rows from the left table, and NULL values for non-matching rows.
FULL OUTER JOIN: Returns all rows from both tables, with NULL values for non-matching rows.
The basic syntax for JOIN function in SQL is as follows:

vbnet
Copy code
SELECT columns
FROM table1
JOIN table2
ON table1.column = table2.column;
Here, columns represents the columns you want to select from the combined tables, table1 and table2 represent the tables you want to join, and column represents the common column between the tables.

For example, to combine the customers and orders tables based on the customer_id column, you can use the following SQL statement:

vbnet
Copy code
SELECT *
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;
This will return all columns from both tables where the customer_id values match.


