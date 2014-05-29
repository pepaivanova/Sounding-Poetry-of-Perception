var request = require('request');

var agentkeepalive = require('agentkeepalive');
var myagent = new agentkeepalive({
        maxSockets: 50
        , maxKeepAliveRequests: 0
        , maxKeepAliveTime: 30000
        });

var nano = require('nano')(
        { "url"              : "http://localhost:5984"
        , "request_defaults" : { "agent" : myagent }
        });


// clean up the database we created previously
nano.db.destroy('sounding', function() {
    // create a new database
    nano.db.create('sounding', function() {
        // specify the database we are going to use
        var sounding = nano.use('sounding');
        // and insert a document in it
        sounding.insert({ "id": 100250 }, function(err, body, header) {
           if (err) {
              console.log('[sound1] ', err.message);
             return;
           }
           console.log('you have inserted id');
           console.log(body);
           console.log(header);
        });
        sounding.insert({ "tags": ["birds", "field-recording", "gibbon",
            "jungle", "macaque", "monkey", "rainforest", "wind", "zoo"],
            "id": 100250
            },
            'sound1', function(err, body, header) {
               if (err) {
                  console.log('[sound1] ', err.message);
                  return;
               }
               console.log('you have inserted sound1');
               console.log(body);
               console.log(header);
            });
        });
    });

// read folder from my server and print it
url = 'http://home.rdrlab.com:85/other/freeSounds/01/';
// http://scotch.io/tutorials/javascript/scraping-the-web-with-node-js
request(url, function(error, response, body) {
    if (!error && response.statusCode == 200) {
        console.log(body);
    }
});
