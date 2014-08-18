/*
 *  Main file for communication with CouchDB
 *
 *  Search for specific string using 'soundSearch' function.
 *  Return value has following syntax
 *      [ [ url + id + .wav, key ], [ url + id + .wav, key ] ]
 *  Example:
 *      [ [ 'http://home.rdrlab.com:85/other/freeSounds/10/159329.wav',
 *          'pera' ] ]
 */

// close communication with the web server
var agentkeepalive = require('agentkeepalive');
var myagent = new agentkeepalive({
        maxSockets: 50
        , maxKeepAliveRequests: 0
        , maxKeepAliveTime: 30000
        });

var nano = require('nano')(
        { "url"              : "http://home.rdrlab.com:5984"
        , "request_defaults" : { "agent" : myagent }
        });

// db to use
var sounding = nano.use('sounding');

// search for string in given db with return values limit
var a = soundSearch('sounding','by_word', "pepa", 1);
//console.log(a);

// returns key, url and id of the .wav file
function soundSearch( db, view, word, limitValue ) {
    var snd = [];
    sounding.view( db, view, { startkey: word, limit: limitValue },
            // snd = retValue(err, body, arr)
            function(err, body) {
            if (!err) {
                body.rows.forEach(function(doc) {
                    // console.log(doc.key, doc.value);
                    snd.push([doc.value[0] + doc.value[1] + ".wav", doc.key]);
                });
                console.log(snd);
                // return snd;
            }
            else { console.log(err); }
    });
}

