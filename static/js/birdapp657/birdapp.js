

var prevScrollpos = window.pageYOffset;
var currentScrollPos = window.pageYOffset;
var wrapers = document.getElementsByClassName("bird_top_wraper");
var transparent = wrapers[0].classList.contains('transparent');
var active_menu = true;
var active_dropdown = false;

window.onscroll = function(e) {
    if (active_dropdown) {
        e.preventDefault();
        return false;
    }
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
        active_dropdown = false;
    }
    if (currentScrollPos == 0 & prevScrollpos != currentScrollPos) {
        if (transparent) {
            wrapers[0].classList.add('transparent');
        }
        active_menu = true;
        active_dropdown = true;
    }
    prevScrollpos = currentScrollPos;
}

document.getElementById("bird_mobile_menu_dropdown").onclick = function() {
    if (!active_dropdown) {
        active_dropdown = true;
        if (transparent) {
            wrapers[0].classList.remove('transparent');
        }
        document.getElementById("bird_mobile_menu_dropdown").classList.add('active');
    } else {
        active_dropdown = false;
        if (transparent && currentScrollPos == 0) {
            wrapers[0].classList.add('transparent');
        }
        document.getElementById("bird_mobile_menu_dropdown").classList.remove('active');
    }
    return false;
}
