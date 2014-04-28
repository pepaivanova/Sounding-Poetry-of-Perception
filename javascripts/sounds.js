var mySound = new buzz.sound( "sounds/rain-01", {
    formats: [ "mp3", "ogg", "aac" ],
    preload: false,
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
