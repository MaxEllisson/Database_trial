import sqlite3
conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

select_students = """
SELECT id, firstname, lastname
FROM students
WHERE age >= 15 """