/*
 *  Authors: Radoslav, Mircho
 *  Purpose: Create initial DB for the application
 *
 *
 */

// configuration file with all variables
var fs = require('fs');
// file is included here:
eval(fs.readFileSync('config.js') + '');

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

// delete old database if exists and create new one
nano.db.destroy( dbName, function() {
	nano.db.create( dbName );
	console.log( 'New Database \'' + dbName + '\' created.' );
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
		var sounding = nano.use( dbName );
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
							// console.log( json );
							sounding.insert( json, function( err, body, header) {
								if (err) {
									console.log('[error]', err.message);
									return;
								}  
								console.log('Document inserted into \'' + dbName + '\' DB.');
								//console.log(body);
								//console.log(header);
							});
							//processFileWithTags( name, href, json.tags );
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

