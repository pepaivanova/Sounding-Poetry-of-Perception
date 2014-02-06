Sounding poetry of perception
=============================

## Description

As time goes by the project is getting clearer. Actually the Sounding Poetry is
a device, where anyone could describe his visual perception on given art in
written form. The device takes the input text as a raw data and generates
unique soundscape according the text. At the end small thermal printer prints
the message on a paper.

## Hardware

* This project uses old laptop Asus AspireOne + Thermal Printer COM-10438

## Motivation

In Sounding Poetry, textual descriptions become a score for sound compositions,
where different words correspond to field recordings and sounds. The created
soundscape is composed by one’s interpretation of his/her own visual experience
into words.

## Goals

* Create simple web server for interaction with PD.
* Use Pure Data to mix .mp3 files.
* Create simple database with .mp3 files.
* Synchronise database with soundcloud or other web platform. - OSC?
* Use Pure Data to stream soundscapes from web platform and mix them.
* Automatic synchronisation between web platform and local database.?!

## Status - development

(Just started, Development, Testing, Production)

## Dependencies

* Python > 2.7
* [Pure Data (pd-extended)](http://puredata.info/downloads/pd-extended)
* [Flask](http://flask.pocoo.org)
* [SQLite3](http://www.sqlite.org)
* [SQLAlchemy](http://www.sqlalchemy.org)
* [java > 1.7](http://openjdk.java.net/install/)
* [normalize](http://normalize.nongnu.org)
* [Websocket-server-patch-extended](http://puredata.hurleur.com/sujet-10062-websocket-server-patch-extended-demo)

## Special thanks to:

[Kiril Zyapkov](https://github.com/kzyapkov)

[Ruslan Velkov](https://github.com/zubenelacribi)

[Mircho Mirev](https://dontknow.com)

[Miller Puckette](http://en.wikipedia.org/wiki/Miller_Puckette) (Pure Data)

[Guido van Rossum](http://en.wikipedia.org/wiki/Guido_van_Rossum) (Python)

[Armin Ronacher](https://twitter.com/mitsuhiko) (Flask)

[Dwayne Richard Hipp](http://en.wikipedia.org/wiki/D._Richard_Hipp) (SQLite)

[Michael Bayer](https://twitter.com/zzzeek) (SQLAlchemy)

[yairEO](https://github.com/yairEO/fancyInput) (fancyInput)

[Nicolas Lhommet](http://puredata.hurleur.com/profil-47995-nicolas-lhommet)
(Websocket)

