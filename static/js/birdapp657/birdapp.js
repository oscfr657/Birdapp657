

var prevScrollpos = window.pageYOffset;
var currentScrollPos = window.pageYOffset;
var wrapers = document.getElementsByClassName("bird_top_wraper");
var transparent = wrapers[0].classList.contains('transparent');
var active_menu = true;

window.onscroll = function() {
    currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        if (!active_menu) {
            active_menu = true;
            wrapers[0].style.top = '0px';
            if (transparent) {
                wrapers[0].classList.remove('transparent');
            }
        }
    } else {
        if (active_menu) {
            wrapers[0].style.top = '-114px';
        }
        active_menu = false;
    }
    if (currentScrollPos == 0 & prevScrollpos != currentScrollPos) {
        if (transparent) {
            wrapers[0].classList.add('transparent');
        }
        active_menu = true;
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
