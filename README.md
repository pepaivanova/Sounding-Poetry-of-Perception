Sounding poetry of perception
=============================

## Description

As time goes by the project get clearer. Actually the Sounding Poetry is a device, where anyone could describe his visual perception on given art in written form. The device takes the input text as a raw data and generates unique soundscape according the text. At the end small thermal printer prints the message on a paper.

## Hardware

* Raspberry Pi ([Raspbian](http://www.raspbian.org) + [pd-extended](http://puredata.info/downloads/pd-extended-0-43-3-on-raspberry-pi-raspbian-wheezy-armhf))
* 7'' TV/Monitor with A/V input
* bluetooth keyboard & mouse
* usb wifi adapter (realtek)

## Motivation

In Sounding Poetry, textual descriptions become a score for sound compositions, where different words correspond to field recordings and sounds. The created soundscape is composed by one’s interpretation of his/her own visual experience into words.

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
* [SQLAlchemy](http://www.sqlalchemy.org)
* Pure Data netsend for communication

## Special thanks to:

[Kiril Zyapkov](https://github.com/kzyapkov), [Miller Puckette](http://en.wikipedia.org/wiki/Miller_Puckette) (Pure Data), [Guido van Rossum](http://en.wikipedia.org/wiki/Guido_van_Rossum) (python), [Armin Ronacher](https://twitter.com/mitsuhiko) (Flask), [Michael Bayer](https://twitter.com/zzzeek) (SQLAlchemy)
