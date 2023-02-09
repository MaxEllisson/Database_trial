from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class

Base = declarative_base()


# Sets up a Person table, this references "activities" via the person_activities table

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String, nullable=False)

    last_name = Column(String, nullable=False)

    # Gives a representation of a Person (for printing out)

    def __repr__(self):
        return f"<Person({self.first_name} {self.last_name})>"

    # Include a method:

    def greeting(self):
        print(f'{self.first_name} says "hello"!')
