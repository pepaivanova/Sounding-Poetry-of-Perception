Dependencies
------------

 * sqlite3
 * python2.7
 * pip
 * virtualenv
 * flask
 * sqlalchemy

Installation
------------

To deploy the webapp initially:
```
# install sqlite3
sudo pt-get install sqlite3

# install python-pip
sudo apt-get install python-pip

# install virtualenv
sudo pip install virtualenv

# checkout the code
git clone https://github.com/pepaivanova/Sounding-Poetry-of-Perception.git
cd Sounding-Poetry-of-Perception/web

# create your virtualenv (in sounding-poetry-of-perception/web)
virtualenv virtual

# activate it, install requirements
source virtual/bin/activate
pip install -r requirements.txt
```

To run the application:

```
source virtual/bin/activate
python createSoundsDB.py
python app.py
```

Database
--------

Connecting to a local sqlite database following instructions at
http://flask.pocoo.org/docs/patterns/sqlalchemy/#declarative

