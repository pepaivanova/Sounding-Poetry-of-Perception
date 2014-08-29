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

// variables
var word2urlArray = [];
var db = 'sounding';
var view = 'by_word';
var word = 'pista';
var limitValue = 10;

var word2url = function(key_, value_) {
	word2urlArray.push({key:key_, value:value_});	
	//console.log(key+':'+value);
};

// request to db
sounding.view( db, view, { startkey: word, limit: limitValue },
    function(err, body) {
    if (!err) {

	// for each row execute word2url function 
	body.rows.forEach(function(doc) {
	    word2url( doc.key, doc.value[0]);
	});

	// event trigger - word search finished ! TODOs
	console.log(word2urlArray);
    }
    else { console.log(err); }
});

