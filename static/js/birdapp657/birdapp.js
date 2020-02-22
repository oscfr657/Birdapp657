

var prevScrollpos = window.pageYOffset;
var currentScrollPos = window.pageYOffset;
var wrapers = document.getElementsByClassName("bird_top_wraper");
var transparent = wrapers[0].classList.contains('transparent');
var active_menu = false;

window.onscroll = function() {
    currentScrollPos = window.pageYOffset;
    if (active_menu) return;
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

document.getElementById("bird_mobile_menu_dropdown").onclick = function() {
    if (!active_menu) {
        active_menu = true;
        if (transparent) {
            wrapers[0].classList.remove('transparent');
        }
        document.getElementById("bird_mobile_menu_dropdown").classList.add('active');
    } else {
        active_menu = false;
        if (transparent && currentScrollPos == 0) {
            wrapers[0].classList.add('transparent');
        }
        document.getElementById("bird_mobile_menu_dropdown").classList.remove('active');
    }
    return false;
}
