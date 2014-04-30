// load background images as backgrounds or slideshow
$(function() {
        $.vegas({
            preload: true,
            delay: 8000,
            fade: 4000,
            src:'images/background_Ljudmila.jpg'
        });
        $.vegas('overlay', {
            src:'/vegas/overlays/13.png'
        });
});
/*
$( function() {
    $.vegas( 'slideshow', {
        preload: true,
        delay: 8000,
        backgrounds: [
            { src: 'images/background1.jpg', fade: 4000 },
            { src: 'images/background2.jpg', fade: 4000 },
        ]
    } )('overlay');
});
*/

