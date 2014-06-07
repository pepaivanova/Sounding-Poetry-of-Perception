## Requirements

 * node.js
 * express

## Install

Install latest version of node.js. Instructions for different OS:

[https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager)

```
sudo npm install express -g
```

```
cd sounding && npm install
```

'package.json' contains information about the application.

## Install 'vegas' and 'buzz' java script libraries

```
cd sounding/public/javascripts
git clone https://github.com/jaysalvat/vegas.git
git clone https://github.com/jaysalvat/buzz.git
```

## Usage

run the app:

```
Sounding-Poetry-of-Perception/src/sounding/$ DEBUG=sounding node app
Sounding-Poetry-of-Perception/src/sounding/$ npm start
```

type in browser:

```
localhost:3000/test.html
```

## CouchDB

Follow the instructions on
[CouchDB](http://docs.couchdb.org/en/latest/install/index.html) website to
install database.

Check if CouchDB is installed on [localhost:5984/_utils](localhost:5984/_utils)

Using [LightTable](http://www.lighttable.com) edit source code and test in browser.
