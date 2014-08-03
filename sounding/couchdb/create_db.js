/*
 *  Authors: Radoslav, Mircho
 *  Purpose: Create initial DB for the application
 *
 *
 */

var request = require('request');
// Mircho addon for parsing .json files
var DOMParser = require( 'xmldom' ).DOMParser;
var config = {
	path : 'http://home.rdrlab.com:85/other/freeSounds/01/'
};

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
               //console.log('you have inserted sound1');
               //console.log(body);
               //console.log(header);
            });
        });
    });

// read folder from my server and print it
url = 'http://home.rdrlab.com:85/other/freeSounds/01/';
// http://scotch.io/tutorials/javascript/scraping-the-web-with-node-js
request(url, function(error, response, body) {
    if (!error && response.statusCode == 200) {
        // use regular expression to check if .json
        var testJSON = /.json/;
        // split body string into array from the lines
        body2 = body.split("\r\n");
        // remove first 4 rows - the header of the page
        body2.splice(0,4);
        // remove last 3 elements from the array
        body2.pop();
        body2.pop();
        body2.pop();
        //
        // find number of all elements in the array
        //
        //console.log("lenght of body2 (wav+json): " + body2.length);
        //
        // remove all .wav files from the array
        for (var i in body2) {
           // check if file ends with .json
           var test = testJSON.test(body2[i]);
           if (test) {
               // console.log(body2[i]);
               // console.log("test: " + test);
           }
           else {
               body2.splice(i,1);
               // console.log("test: " + test);
           }
        }
        // print type of body2
        //console.log("type of body2: " + typeof body2);
        // check if body 2 is array
        //console.log("is body2 array?: " + Array.isArray(body2));
        // print length of the array
        //console.log("length of body2 (json): " + body2.length);
        // print all .json files
        //console.log(body2);

    }
});

// Mircho's addon
request.get( config.path,
		function( error, response, body )
		{
			if( !error )
			{
				//here we have the body of the reponse
				var doc = new DOMParser().parseFromString( body, 'text/html' );
				var links = doc.documentElement.getElementsByTagName( 'a' );
				var href, name;
				//now we have all the links, we can go over them
				for( var i = 0, len = links.length; i < len; i++ )
				{
					href = links[ i ].getAttribute( 'href' );
					if( href.indexOf( '.json' ) !== -1 )
					{
						name = href.replace( '.json', '' );
						//console.log( name, href );
						//continue;
						request.get( config.path + href,
								function( error, response, body )
								{
									if( !error )
									{
										var json = JSON.parse( body );
										processFileWithTags( name, href, json.tags );
									}
								}
						);
					}
				}
			}
		}
);

function processFileWithTags( name, href, tags )
{
    // here should be placed the logic for the update of the DB
	console.log( name, href, tags );
}
