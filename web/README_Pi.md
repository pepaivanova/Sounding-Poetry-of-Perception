Dependencies
------------

 * python2.7
 * flask
 * sqlalchemy
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

Raspberry Pi
------------

Using Raspbian from: http://downloads.raspberrypi.org/raspbian_latest

Default login: 	pi / raspberry

Install pd-extended following the instructions from [here](http://puredata.info/downloads/pd-extended-0-43-3-on-raspberry-pi-raspbian-wheezy-armhf).

In summary:
```
sudo nano /etc/apt/sources.list
# -copy/paste this line to the list(right-click to paste):
deb-src http://archive.raspbian.org/raspbian wheezy main contrib non-free rpi
#ctrl+o, Enter (to save). ctrl+x (to exit)

sudo apt-get update
wget https://puredata.info/downloads/pd-extended-0-43-3-on-raspberry-pi-raspbian-wheezy-armhf/releases/1.0/Pd-0.43.3-extended-20121004.deb
sudo dpkg -i Pd-0.43.3-extended-20121004.deb
sudo apt-get -f install
# it should be installed. For root priorities:
sudo chmod 4755 /usr/bin/pd-extended 
```

Install puredata-utils (needed for 'pdsend' command)
```
sudo apt-get install puredata-utils
```

Install python virtualenv
```
sudo apt-get install python-virtualenv
```

Clone Sounding-Poetry-of-Perception repository
```
mkdir git
cd git
git clone https://github.com/pepaivanova/Sounding-Poetry-of-Perception.git
cd Sounding-Poetry-of-Perception
git checkout -m master
```

Create virutal environement in web folder:
```
cd web
virtualenv virtual
```

Install Flask and SQAlchemy
```
source virtual/bin/activate
pip install -r requirements.txt
```

Run pd-extended without gui (not tested yet)
```
pd-extended -nogui -noadc -alsa -open ../pd/startSoundFromPython.pd &
```

Run application without DB
```
source virtual/bin/activate
python appNoDb.py &
```

Check IP address of Raspberry Pi
```
ifconfig -a
```

I'm using wlan0 adapter and currently the IP is set to 192.168.1.105

In browser type url: http://192.168.1.105:5000


Edit pd-exteded patch on local computer via ssh
-----------------------------------------------

Pure data patches could be edited remotely if we use ssh with X issuing:
```
ssh -Y pi@192.168.1.105 pd-extended
```


Database
--------

Connecting to a local sqlite database following instructions at
http://flask.pocoo.org/docs/patterns/sqlalchemy/#declarative

