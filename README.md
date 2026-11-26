# CSV to SQLite User Importer

A small Python script that reads user records from a CSV file and stores them in a SQLite database. It then prints every record in the database.

## Features

- Creates the SQLite database and `users` table automatically if they don't exist
- Reads user data from `users.csv` using Python's built-in `csv` module
- Uses parameterized queries (`?` placeholders) to prevent SQL injection
- Skips duplicate users, since `email` is unique and the insert uses `INSERT OR IGNORE`
- Prints all stored users after the import

## Project Structure

```
.
├── import_users.py   # Import script
├── users.csv         # Sample input data
├── users.db          # SQLite database (created/updated by the script)
└── README.md
```

## Requirements

- Python 3.6+
- No external packages needed (uses only the standard library: `csv`, `sqlite3`)

## Usage

```bash
python import_users.py
```

Run the script from the folder that contains `users.csv`. The database `users.db` is created in the same folder.

## CSV Format

`users.csv` must have a header row with these columns:

```csv
name,email,age
Harsh Kumar,harsh@example.com,24
Rahul Sharma,rahul@example.com,23
Priya Singh,priya@example.com,25
Amit Kumar,amit@example.com,22
Sneha Patel,sneha@example.com,24
```

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS users (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age   INTEGER
);
```

## Example Output

```
Users imported successfully!

(1, 'Harsh Kumar', 'harsh@example.com', 24)
(2, 'Rahul Sharma', 'rahul@example.com', 23)
(3, 'Priya Singh', 'priya@example.com', 25)
(4, 'Amit Kumar', 'amit@example.com', 22)
(5, 'Sneha Patel', 'sneha@example.com', 24)
```

Running the script again will not create duplicates, because rows with an existing email are ignored.

## Inspecting the Database

```bash
sqlite3 users.db "SELECT * FROM users;"
```

## Possible Improvements

- Accept the CSV path as a command-line argument
- Validate rows (empty names, invalid emails, non-numeric ages) and report skipped rows
- Wrap the import in a `try/finally` or `with` block so the connection always closes
- Add unit tests

## License

This project is open source and available under the [MIT License](LICENSE).
