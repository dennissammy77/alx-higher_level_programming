SQL - Introduction

__Learning Objectives__
What’s a database
What’s a relational database
What does SQL stand for
What’s MySQL
How to create a database in MySQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries
How to use MySQL functions

_Data_
Is facts related to any object.
_Database_
Is a  systematic collection of data.
Makes data management easy
_DBMS-(Database Management System)_
Is a collection of programs which enables its users access database, manipulate data and help in representation of data.
Helps control access to data in a database.

_Types of DMS_
a. Hierarchical
Employs child parent relationship of storing data.
Structure is like a node.
b. Network 
Supports many to many dbms.
c. Relational 
Defines database relations in form tables.
Does not support many to many relations
eg. MySql, Oracle, MS SQL server
d. Object Oriented Relation
Supports storage of new data types.
Data to be stored is in form of objects.
Objects have attributes.
eg. Postgres 

_SQL(Structured Query Language)_
Is language for dealing with relational databses.
Can be used to insert, search, update, delete, database records.
Helps in maintenance and optimizing of databases.

Example of SQL Statement
eg. SELECT * from members where age > 30

Basic SQL statements: DDL & DML
SQL statements are divided into two major categories: data definition language (DDL) and data manipulation language (DML).

_Data definition language_
- DDL statements are used to build and modify the structure of your tables and other objects in the database.

In SQL (Structured Query Language), Data Definition Language (DDL) statements are used to define or modify the structure of a database. DDL statements are used to create, alter, or drop database objects such as tables, indexes, views, and procedures.

The most commonly used DDL statements include:

CREATE: This statement is used to create a new database object such as a table, view, or index. For example, "CREATE TABLE" statement is used to create a new table in the database.

ALTER: This statement is used to modify the structure of an existing database object. For example, "ALTER TABLE" statement is used to add a new column to an existing table.

DROP: This statement is used to delete an existing database object. For example, "DROP TABLE" statement is used to delete a table from the database.

TRUNCATE: This statement is used to remove all the data from a table while retaining the structure of the table.

DDL statements are usually used by database administrators or developers who are responsible for managing the database structure. These statements are executed using SQL commands in a database management system (DBMS) such as MySQL, Oracle, or Microsoft SQL Server.

It is important to note that DDL statements can be very powerful and can have significant impacts on the database structure and data. Therefore, it is important to use them with caution and ensure that appropriate backups and testing are done before executing any DDL statements in a production environment.

_Data Manipulation language_

In SQL, Data Manipulation Language (DML) statements are used to manipulate data stored in a database. DML statements are used to retrieve, insert, update, and delete data from database tables.

The most commonly used DML statements include:

SELECT: This statement is used to retrieve data from one or more tables. For example, the following statement retrieves all columns and rows from the "employees" table:
	SELECT * FROM employees;

INSERT INTO: This statement is used to insert new data into a table. For example, the following statement inserts a new employee record into the "employees" table:

INSERT INTO employees (emp_id, first_name, last_name, email, hire_date) 
VALUES (1, 'John', 'Doe', 'johndoe@example.com', '2022-03-16');

UPDATE: This statement is used to modify existing data in a table. For example, the following statement updates the email address of an employee with ID 1 in the "employees" table:

UPDATE employees SET email = 'newemail@example.com' WHERE emp_id = 1;

DELETE FROM employees WHERE hire_date < '2022-01-01';

Relational Algebra (RA):
Relational Algebra is a theoretical language used to describe operations on relational databases.
RA uses mathematical notation to represent operations such as projection, selection, union, intersection, and difference.

RA has a set of basic operations, including:

Selection: Retrieves a subset of rows from a table based on a specified condition.
Projection: Retrieves a subset of columns from a table.
Union: Combines the rows from two tables into a single table, removing duplicates.
Intersection: Returns only the rows that appear in both tables.
Difference: Returns the rows from one table that do not appear in the other.
Cartesian product: Combines every row in one table with every row in another table, creating a new table with all possible combinations.

SQL (Structured Query Language) technique functions are built-in functions provided by SQL that perform calculations or transformations on the data in a table or database. These functions can be used in SQL queries to modify or retrieve data. Here are some commonly used SQL technique functions with examples:

COUNT function:
The COUNT function is used to count the number of rows in a table that meet certain conditions. Here's an example:
sql
Copy code
SELECT COUNT(*) FROM orders WHERE status = 'complete';
This query will return the total number of orders that have a status of 'complete'.

SUM function:
The SUM function is used to calculate the sum of values in a column. Here's an example:
sql
Copy code
SELECT SUM(total_price) FROM orders;
This query will return the total sum of the 'total_price' column in the 'orders' table.

AVG function:
The AVG function is used to calculate the average of values in a column. Here's an example:
sql
Copy code
SELECT AVG(total_price) FROM orders WHERE status = 'complete';
This query will return the average value of the 'total_price' column for orders that have a status of 'complete'.

MIN function:
The MIN function is used to find the minimum value in a column. Here's an example:
sql
Copy code
SELECT MIN(total_price) FROM orders;
This query will return the minimum value of the 'total_price' column in the 'orders' table.

MAX function:
The MAX function is used to find the maximum value in a column. Here's an example:
sql
Copy code
SELECT MAX(total_price) FROM orders WHERE status = 'complete';
This query will return the maximum value of the 'total_price' column for orders that have a status of 'complete'.

CONCAT function:
The CONCAT function is used to concatenate (join together) two or more strings into a single string. Here's an example:
sql
Copy code
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customers;
This query will return the full name of each customer as a single string, with a space between the first and last names.

SUBSTRING function:
The SUBSTRING function is used to extract a portion of a string. Here's an example:
sql
Copy code
SELECT SUBSTRING(product_name, 1, 3) FROM products;
This query will return the first three characters of the 'product_name' column for each row in the 'products' table.

DATE functions:
There are several SQL technique functions that can be used to work with dates, such as DATE, YEAR, MONTH, DAY, and DATE_FORMAT. Here's an example:
sql
Copy code
SELECT DATE_FORMAT(order_date, '%m/%d/%Y') AS formatted_date FROM orders;
This query will return the 'order_date' column in a formatted date string (month/day/year) for each row in the 'orders' table.

These are just a few examples of the many SQL technique functions available for use in SQL queries. By using these functions, you can perform calculations, manipulate strings, and work with dates in your SQL queries to retrieve and modify data.

In SQL, a subquery is a query that is nested inside another query, which can be used to retrieve or modify data in a more complex way. Here are some examples of SQL technique subqueries:

Basic Subquery:
sql
Copy code
SELECT * FROM orders WHERE customer_id IN 
(SELECT customer_id FROM customers WHERE country = 'USA');
This query retrieves all orders where the customer is from the USA. The subquery selects the customer_id from the customers table where the country is 'USA', and the outer query uses that list of customer_ids to retrieve the orders from the orders table.

Subquery with Aggregate Function:
vbnet
Copy code
SELECT customer_id, COUNT(*) AS order_count FROM orders 
WHERE customer_id IN (SELECT customer_id FROM customers WHERE country = 'USA')
GROUP BY customer_id;
This query retrieves the count of orders for each customer in the USA. The subquery selects the customer_ids from the customers table where the country is 'USA', and the outer query uses those customer_ids to count the number of orders for each customer in the orders table.

Subquery with Multiple Tables:
sql
Copy code
SELECT * FROM products WHERE category_id IN 
(SELECT category_id FROM categories WHERE category_name = 'Electronics');
This query retrieves all products in the 'Electronics' category. The subquery selects the category_id from the categories table where the category_name is 'Electronics', and the outer query uses that list of category_ids to retrieve the products from the products table.

Subquery with EXISTS:
sql
Copy code
SELECT * FROM customers WHERE EXISTS 
(SELECT * FROM orders WHERE customers.customer_id = orders.customer_id);
This query retrieves all customers who have placed an order. The subquery checks if there is any order for each customer in the orders table, and the outer query retrieves the customers who have at least one order in the orders table.

Subquery with NOT IN:
sql
Copy code
SELECT * FROM products WHERE product_id NOT IN 
(SELECT product_id FROM order_items);
This query retrieves all products that have not been ordered. The subquery selects the product_id from the order_items table, and the outer query retrieves the products whose product_id is not in that list of ordered products.

These are just a few examples of the many ways SQL technique subqueries can be used to retrieve or modify data in a more complex way. By using subqueries, you can combine the power of multiple queries to retrieve or modify data that might be difficult to get with a single query.
