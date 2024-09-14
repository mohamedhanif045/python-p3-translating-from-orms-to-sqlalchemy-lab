from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

# Create a base class for our models to inherit from
Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

# Set up the engine to connect to the SQLite database
engine = create_engine('sqlite:///dogs.db')

# Create all tables in the database (this is equivalent to "Create Table" in SQL)
Base.metadata.create_all(engine)
