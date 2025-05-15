## create a generator that streams rows from an SQL database one by one.

Python script `seed.py` used to generate database, it caontains the follwing functions;
-  `def connect_db()` :  connects to the databsase
- `def create_database(connection)`: create database if not already exxist.
- `def connect_to_prodev()`: connects to the database
- `def create_table(connection):`: creates table if not exist
- `def insert_data(connection, data):` insert data into the database.
