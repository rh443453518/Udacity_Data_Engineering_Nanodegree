# Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

* This database will help the startup called Sparkify to analyze the data they've been collecting on songs and user activity on their new music streaming app. It can help analyst on analyzing what songs users are listening to. It creates a star schema database and uses ETL pipeline that transfers data from json log files in two local directories into these tables in Postgres using Python and SQL.


# Content in the repository.

* data: json files of songs and logs.
* etl.ipynb: Extract, transform, load process to create the database.
* test.ipynb: Help examine the content in the database.
* create_table.py: Reset the current database to an empty database.
* etl.py: Production code of etl.ipynb.
* sql_queries.py: SQL queries referenced in other scripts.


# How to Use.

1. Run create_tables.py from terminal to set up database and tables.
2. Run etl.py from terminal to process and load data into database.
3. Run example queries in test.ipynb to validate the content of tables created.


# State and justify your database schema design and ETL pipeline.

* The databse is composed of five tables: songplay_table, user_table, song_table, artist_table, time_table. This database uses star schema. The fact table is songplay_table. Other tables are dimension tables. The fact table has foreign keys from other dimensions tables. Data is extracted from two types of JSON source files. The JSON files are read into pandas dataframes, processed and uploaded into the database using psycopg2. Data table is created aligned with schema rules. Finally each record is inserted into the table created.