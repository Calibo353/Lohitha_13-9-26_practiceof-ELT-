Iris ETL Project – Simple Explanation

Our project is about taking flower data, preparing it, and storing it in a MySQL database.

1. Extract – Get the data

We use Python and Seaborn to get the Iris dataset.

It contains 150 flower records and 5 columns.

2. Transform – Change the data

The species names are converted into numbers:

setosa → 0

versicolor → 1

virginica → 2

3. Validate – Check the data

We check whether there are missing values and whether the species values are correctly converted.

4. Load – Store the data

We load the processed data into MySQL.

Database: iris_db

Table: iris

5. Verify – Check in SQL

We use SQL queries to check whether the data was successfully stored.

For example:

SELECT COUNT(*) FROM iris;

It should return 150 if all records were loaded.
