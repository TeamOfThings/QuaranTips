import datetime as dt
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Start the DB engine with the desired DBMS
engine = create_engine('sqlite:///thoughts.db', echo=True)
Base = declarative_base()

# Main table
class Thought(Base):
    __tablename__ = 'thoughts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text(2000))  # around 400 (English) words
    author_id = Column(Integer)
    date = Column(DateTime)

    def __init__(self, *args, **kw):
        super(Thought, self).__init__(*args, **kw)

    def get_id(self):
        return self.id

    def get_author_id(self):
        return self.author_id

def create_tables():
    """ Instantiate DB tables """
    Base.metadata.create_all(engine)