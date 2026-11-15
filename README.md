# OOP Data Processing Lab

## Lab Overview
This lab builds an object-oriented data-processing program in Python. It loads
CSV data (cities and countries) into Table objects, stores the tables in a
simple in-memory database (DB), and supports filtering rows, aggregating
values, and joining two tables on a common key.

## Project Structure
```
data-processing-lab/
├── README.md              # This file
├── Cities.csv             # Cities dataset
├── Countries.csv          # Countries dataset
└── data_processing.py     # DataLoader, DB and Table classes plus test code
```

## Design Overview

### DataLoader
- Attribute: `base_path` - folder containing the CSV files (defaults to the
  folder of the script)
- `load_csv(filename)` - reads a CSV file and returns a list of dictionaries,
  one per row

### Table
- Attributes:
  - `table_name` - name of the table (string)
  - `table` - the data, a list of row dictionaries
- `filter(condition)` - returns a new Table containing only the rows for which
  the condition function returns True
- `aggregate(aggregation_function, aggregation_key)` - collects the values of
  one column (numbers converted to float) and applies the given function,
  e.g. sum, min, max, len
- `join(other_table, common_key)` - returns a new Table that merges each row of
  this table with the rows of the other table that have the same value for the
  common key (inner join)
- `__str__()` - returns the table name and its rows as a string

### DB
- Attribute: `database` - a list of Table objects
- `insert(table)` - adds a Table to the database
- `search(table_name)` - returns the Table with that name, or None if not found

## How to Test and Run
1. Install Python 3.
2. Keep `Cities.csv`, `Countries.csv` and `data_processing.py` in the same folder.
3. Open a terminal in that folder and run:
   ```
   python data_processing.py
   ```
4. The test code at the bottom of the file prints the results. Compare them
   with the expected output provided in the assignment.