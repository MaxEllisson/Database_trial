import sqlite3
from faker import Faker
import random
conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()
parameterised_insert_query = """
INSERT INTO
    students (firstname, lastname, age, gender)
VALUES 
    (?,?,?,?)
"""
fake = Faker('en_GB')
random.seed(4232)
fake.random.seed(4232)
for _ in range(10):
    f_name = fake.first_name()
    l_name = fake.last_name()
    age = random.randint(11, 18)
    gender = random.choice(('male', 'female'))
    cursor.execute(parameterised_insert_query,
                   (f_name, l_name, age, gender))

conn.commit()
