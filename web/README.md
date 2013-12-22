

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
git clone https://github.com/pepaivanova/sounding-poetry-of-perception.git
cd sounding-poetry-of-perception/web

# create your virtualenv (in sounding-poetry-of-perception/web)
virtualenv virtual

# activate it, install requirements
source virtual/bin/activate
pip install -r requirements.txt
```

To run the application:

```
source virtual/bin/activate
python app.py
```

Database
--------

Connecting to a local sqlite database following instructions at
http://flask.pocoo.org/docs/patterns/sqlalchemy/#declarative

