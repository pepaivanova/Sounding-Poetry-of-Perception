import sys
import os
import os.path as p
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = None
db_session = None

Base = declarative_base()

class Poetry(Base):
    __tablename__ = 'poetry'
    id = Column(Integer, primary_key=True)
    sounded_at = Column(DateTime)
    poetry = Column(String(200), unique=False)


def store_poetry(poetry):
    global db_session
    p = Poetry()
    p.sounded_at = datetime.utcnow()
    p.poetry = poetry
    db_session.add(p)
    db_session.commit()

def connect_db(db_file=None):
    if db_file is None:
        db_file = p.abspath(p.join(p.dirname(__file__), 'sounds.db'))

    global engine, db_session
    engine = create_engine('sqlite:////%s' % (db_file, ), convert_unicode=True)
    # check if db file existst, else create db
    if p.isfile(db_file) is False:
        create_db(engine)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def create_db(engine):
    Base.metadata.create_all(bind=engine, checkfirst=True)

if __name__ == '__main__':
    db_file = p.abspath(p.join(os.getcwd(), 'sounds.db'))
    if p.isfile(db_file):
        p.unlink(db_file)

    connect_db(db_file)
    print("Engine: ", engine)
    create_db(engine)

    store_poetry('to be or not to be')
    db_session.commit()

    all_poetry = db_session.query(Poetry).all()
    for pp in all_poetry:
        print("%s spoken at %s" % (pp.poetry, pp.sounded_at))

