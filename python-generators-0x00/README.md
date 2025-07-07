# Python Generators – 0x00

This script connects to a MySQL database, creates a table, loads data from a CSV file, and streams data using Python generators.

## Files

- `seed.py`: Contains all logic to:
  - Connect to database
  - Create tables
  - Insert data from CSV
  - Stream data using a generator

- `user_data.csv`: Sample CSV data to load into MySQL

## Usage

1. Ensure MySQL server is running.
2. Update `seed.py` with your own MySQL credentials.
3. Run the script from a terminal or Jupyter notebook.
4. Call `stream_users(connection)` to yield one user at a time.
