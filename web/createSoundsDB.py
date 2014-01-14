import sys
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Poetry(Base):
    __tablename__ = 'poetry'
    id = Column(Integer, primary_key=True)
    sounded_at = Column(DateTime)
    poetry = Column(String(50), unique=False)

# Create engine that stores data in sounds.db
engine = create_engine('sqlite:///sounds.db')

# Create all tables in the engline
Base.metadata.create_all(engine)
