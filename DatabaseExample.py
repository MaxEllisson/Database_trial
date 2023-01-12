import sqlite3

conn = sqlite3.connect("student.sqlite")

cursor = conn.cursor()

create_students_table = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    age INTEGER,
    gender TEXT
);
"""
cursor.execute(create_students_table)

conn.close()
