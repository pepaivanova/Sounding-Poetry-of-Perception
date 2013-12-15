import os.path as p

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
db_file = p.abspath(p.join(p.dirname(__file__), 'sounds.db'))

engine = create_engine('sqlite:////%s' % (db_file, ), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()

def create_db():
    Base.metadata.create_all(bind=engine)


class Sound(Base):
    __tablename__ = 'sounds'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    filepath = Column(String(50), )


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    sound_id = Column(Integer, ForeignKey('sounds.id'))



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def play_poetry():
    # TODO: process poetry here, send to PD

    redirect('/')





if __name__ == '__main__':
    app.run()