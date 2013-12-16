Sounding poetry of perception
=============================

## Description

In Sounding Poetry, textual descriptions become a score for sound compositions, where different words correspond to field recordings and sounds. The created soundscape is composed by one’s interpretation of his/her own visual experience into words.

## Motivation

## Goals

* Use Pure Data to mix .mp3 files.
* Create simple database with .mp3 files.
* Synchronise database with soundcloud. - OSC?
* Use Pure Data to stream soundscapes from soundcloud and mix them.
* Create simple web server for interaction with PD.
* Automatic synchronisation between soundcloud and local database.?!

## Status - just started

(Just started, Development, Testing, Production)

## Dependencies

* Python 2.7
* [Pure Data (pd-extended)](http://puredata.info/downloads/pd-extended)
* [SQLAlchemy](http://www.sqlalchemy.org)
* [Flask](http://flask.pocoo.org)

## Temporary links

* [Simple pd-extended webclient](http://puredata.info/docs/tutorials/SimplePdExtendedWebclient)
* [Make Python and Pure Data communicate on the Raspberry Pi](http://guitarextended.wordpress.com/2012/11/03/make-python-and-pure-data-communicate-on-the-raspberry-pi/)
* [Using Forms in python](http://raspberrywebserver.com/cgiscripting/web-forms-with-python.html)

## Considerations

There are many options for communication with Pure Data and we should consider the best way for the project.
Few available options are:

1. Pure Data + Python
2. Pure Data + Node.js
3. Pure Data + Jython

Links to projects that look good as a starting point:

3. [port](https://github.com/thisconnect/port/blob/master/readme.md)
4. [mxdublin](http://www.le-son666.com/software/mxdublin/download.html)

