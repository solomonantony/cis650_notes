# Relational database
- A relational database stores data as a collection of tables
- Data in relational databases is stored in tables
- Each table has one or more named columns
- Each column has a particular data type
- Each row of data is a record
# SQL
- SQL is the standard language for working with relational databases.  
- SQL can be used to query databases, as well be used for a wide range of database activities (e.g., create/change/delete table structure, update data, manage user access, group database actions)
# SQLite :Database system used in this lesson
- SQLite is a unique relational database, easy to use
- Included as part of standard Python distribution
- Requires no setup or special process to run
- A SQLite database is stored in one file
# Creating an SQLite database
- You can prototype with SQLite, then migrate to another SQL database type
- Alternatives for getting started with a SQLite database:
- https://www.sqlite.org/download.html
- Create your own database using the sqlite3 tool
  - https://sqlitebrowser.org/
  - https://sqlitestudio.pl/
- Use a Python program to create a SQLite database
- Copy a SQLite database file that has already been created
# Overview of working with Python and SQL database
- Python has a standard interface for working with relational database
- Python can be used in combination with SQL
- SQL statements can be represented as Python strings
- Python statements can send SQL strings to a database via a connection
- Python statements can then access and process the results
# Example tables used in this lesson
- The sqlite database ecars.db has annual sales of electric cars for selected countries and years.
- The database has two tables:
-- countries: country, continent
-- sales: country, year, sales
# Steps used in database interaction
- Import the package for working with the database
- Establish a Connection between your program and the database
- The Connection variable is a handshake between program and database
- Similar in concept to a file variable returned from an open()
- Get a Cursor variable
- The Cursor lets you submit requests, access results
- Use the Cursor variable to submit a request
- Use the Cursor variable to access and process the results
# bulk import
- You can create a series of insert statements and run each of them
- Alternatively, if the data is in a list of tuples use the cursor's executemany() method

