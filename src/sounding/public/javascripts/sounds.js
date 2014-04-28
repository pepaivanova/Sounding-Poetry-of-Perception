var mySound = new buzz.sound( "http://192.168.1.1:85/other/freeSounds/01/101389.wav", {
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
