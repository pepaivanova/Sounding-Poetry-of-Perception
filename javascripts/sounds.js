var mySound = new buzz.sound( "http://home.rdrlab.com:85/other/freeSounds/01/100390.wav", {
    // formats: [ "mp3", "ogg", "aac" ],
    preload: true,
    autoplay: true,
    loop: false
});

mySound.play()
    .fadeIn();
/*
    .fadeIn()
    .bind( "timeupdate", function() {
       var timer = buzz.toTimer( this.getTime() );
       document.getElementById( "timer" ).innerHTML = timer;
    });
*/
