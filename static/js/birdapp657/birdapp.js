

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
            wrapers[0].style.visibility = 'visible';
            wrapers[0].style.opacity = 1;
            if (transparent) {
                wrapers[0].classList.remove('transparent');
            }
        }
    } else {
        if (active_menu) {
            wrapers[0].style.visibility = 'hidden';
            wrapers[0].style.opacity = 0;
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

function birdPlay(element) {
    //console.log('birdPlay');
    //console.log(element.parentNode.parentNode.getElementsByTagName('video')[0]);
    element.parentNode.parentNode.getElementsByTagName('video')[0].play();
    element.nextElementSibling.style.display = 'block';
    element.style.display = 'none';
}
function birdPause(element) {
    //console.log('birdPause');
    //console.log(element.previusSibling);
    element.parentNode.parentNode.getElementsByTagName('video')[0].pause()
    element.previousElementSibling.style.display = 'block';
    element.style.display = 'none';
}
