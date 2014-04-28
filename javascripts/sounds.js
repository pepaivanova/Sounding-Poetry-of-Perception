var mySound = new buzz.sound( "/sounds/rain-01", {
    formats: [ "ogg", "mp3", "aac" ],
    preload: true,
    autoplay: true,
    loop: false
});

mySound.play()
    .fadeIn()
    .bind( "timeupdate", function() {
       var timer = buzz.toTimer( this.getTime() );
       document.getElementById( "timer" ).innerHTML = timer;
    });
