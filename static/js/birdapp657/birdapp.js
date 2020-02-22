

var prevScrollpos = window.pageYOffset;
var wrapers = document.getElementsByClassName("bird_top_wraper");
var transparent = wrapers[0].classList.contains('transparent');
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        wrapers[0].style.top = '0px';
        if (transparent) {
            wrapers[0].classList.remove('transparent');
        }
    } else {
        wrapers[0].style.top = '-114px';
    }
    if (currentScrollPos == 0 & prevScrollpos != currentScrollPos) {
        if (transparent) {
            wrapers[0].classList.add('transparent');
        }
    }
    prevScrollpos = currentScrollPos;
}
