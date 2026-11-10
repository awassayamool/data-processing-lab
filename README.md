# OOP Data Processing Lab

## Lab Overview
This lab turns a procedural data-processing script into an object-oriented
design. It loads city data from a CSV file, stores it in a Table object, and
supports filtering rows and aggregating values (average, max, count of unique
values).

## Project Structure
data-processing-lab/
├── README.md              # This file
├── Cities.csv             # The dataset
└── data_processing.py     # The analysis code (DataLoader and Table classes)

## Design Overview

### DataLoader
- Attribute: `base_path` - the folder where the CSV files are located
  (defaults to the folder of the script)
- `load_csv(filename)` - reads a CSV file and returns a list of dictionaries,
  one dictionary per row

### Table
- Attributes:
  - `table_name` - the name of the table (string)
  - `table` - the data, a list of dictionaries (one per row)
- `filter(condition)` - takes a function (e.g. a lambda) and returns a new
  Table containing only the rows where the condition is True
- `aggregate(aggregation_function, aggregation_key)` - collects the values of
  one column, converts numbers to float, and applies the given function
  (e.g. sum, max, len(set(...)))
- `__str__()` - prints the table name and its rows

## How to Test and Run
1. Install Python 3.
2. Put `Cities.csv` and `data_processing.py` in the same folder.
3. Open a terminal in that folder and run:
   python data_processing.py
4. The test code at the bottom of the file prints the average temperature,
   cities in Germany, cities in Spain above 12°C, the number of unique
   countries, and the average and max temperatures for Germany and Italy.