import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
age INTEGER
)
""")

# Read CSV file
# Read CSV file
with open("users.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Insert data into database
for row in rows:
    cursor.execute("""
        INSERT OR IGNORE INTO users (name, email, age)
        VALUES (?, ?, ?)
    """, (row["name"], row["email"], int(row["age"])))

# Save changes
conn.commit()

# Display records
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print("Users imported successfully!\n")

for user in users:
   print(user)

# Close database connection
conn.close()