import sqlite3
conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

select_students = """