import os.path as p

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#default_db_file = p.join(p.dirname(__file__), 'sounds.db')
default_db_file = p.abspath(p.join(p.dirname(__file__), 'sounds.db'))


db_session = None
engine = None

Base = declarative_base()

class Sound(Base):
    __tablename__ = 'sounds'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    filepath = Column(String(50), )

def connect_db(db_file=None):
    if db_file is None:
        db_file = default_db_file
    global engine, db_session
    engine = create_engine('sqlite:////%s' % (db_file, ), convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))

def init_db():
    connect_db()
    Base.metadata.create_all(bind=engine)