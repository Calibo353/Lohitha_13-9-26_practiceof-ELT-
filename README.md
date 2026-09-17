Iris ETL Pipeline Using Python and MySQL
📌 Project Overview

This project demonstrates an ETL (Extract, Transform, Validate, and Load) pipeline using the Iris dataset.

The main objective is to extract Iris data, transform and prepare the data using Python, validate the data, and load it into a MySQL database.
🛠️ Technologies Used
Python
Pandas
Seaborn
SQLAlchemy
PyMySQL
MySQL Workbench
Git and GitHub
📊 Dataset Information
Dataset: Iris
Total rows: 150
Total columns: 5

The dataset contains measurements of Iris flowers from three different species.

Columns
sepal_length
sepal_width
petal_length
petal_width
species
⚙️ Data Transformation

The species column contains categorical values. These values are converted into numerical values:

setosa      → 0
versicolor  → 1
virginica   → 2

The transformation is performed using Python.

✅ Data Validation

The pipeline validates the transformed data by checking:

Whether any NULL values are present.
Whether the species column contains only valid encoded values.
Whether the data is ready to be loaded into the database.

If the validation is successful, the pipeline displays:

Validation Passed
🗄️ MySQL Database

The transformed Iris data is loaded into the following database and table:

Item	Name
Database	iris_db
Table	iris
Expected records	150
SQL Queries
USE iris_db;

SHOW TABLES;

SELECT COUNT(*) FROM iris;

SELECT * FROM iris LIMIT 10;

DESCRIBE iris;
📂 Project Structure
ETL2/
├── extract.py
├── transform.py
├── Validate.py
├── load.py
├── config.py
└── pipeline.py
▶️ How to Run the Project
1. Install Dependencies
pip install pandas seaborn sqlalchemy pymysql
2. Configure MySQL

Set your MySQL connection details in config.py.

Do not upload your actual MySQL password to GitHub.

3. Run the Pipeline

From the project's parent folder:

python ETL2/pipeline.py

On Windows PowerShell:

python ETL2\pipeline.py
📌 Expected Output
Extracted 150 rows, 5 columns
Transformed Shape: (150, 5)
Validation Passed
Loaded 150 rows into 'iris' table
🎯 Learning Outcomes

Through this project, I learned how to:

Extract data using Python.
Work with the Iris dataset.
Transform categorical data.
Encode species values into numerical values.
Validate data before loading.
Connect Python with MySQL.
Load data into a MySQL table.
Verify data using SQL queries.
Build a basic ETL pipeline.
Organize an ETL project using GitHub.

⭐ This project is part of my Data Engineering learning journey.
