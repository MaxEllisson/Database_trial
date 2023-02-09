from sqlalchemy import create_engine

from models import Base


engine = create_engine('sqlite:///activities.db', echo=True)

Base.metadata.create_all(engine)

