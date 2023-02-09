from sqlalchemy import create_engine

from sqlalchemy.orm import Session

from models import Person

andrew = Person(first_name="Andrew", last_name="Dales")

people = [Person(first_name="Chris", last_name="Brolin"), Person(first_name='Vera', last_name="Malcova")]

# Connect to the activities database

engine = create_engine('sqlite:///activities.db', echo=True)

# Create a session and add the people to the database

with Session(engine) as sess:
    sess.add(andrew)

    sess.add_all(people)

    sess.commit()
