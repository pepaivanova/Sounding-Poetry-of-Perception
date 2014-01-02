
Dependencies
------------

 * python2.7
 * flask
 * virtualenv

Installation
------------

To deploy the webapp initially:
```
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
python appNoDb.py
```

Database
--------

Connecting to a local sqlite database following instructions at
http://flask.pocoo.org/docs/patterns/sqlalchemy/#declarative


