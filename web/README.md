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

Pip
---

If You get following error when using pip to install the requrements.txt:
```
Could not fetch URL https://pypi.python.org/simple/configobj/: There was a problem confirming the ssl certificate: <urlopen error [Errno 1] _ssl.c:504: error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed>
```
the simplest fix is here on the last comment:

https://groups.google.com/forum/#!topic/beagleboard/aSlPCNYcVjw

bdha...@gmail.com 	
9/6/13
The problem is the internal clock in the BBB. 
If you run 
```
ntpdate -b -s -u pool.ntp.org
```
you won't get the ssl error. However, you will have to do this every time you want to use pip. 


Database
--------

Connecting to a local sqlite database following instructions at
http://flask.pocoo.org/docs/patterns/sqlalchemy/#declarative


