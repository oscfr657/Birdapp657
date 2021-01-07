

var prevScrollpos = window.pageYOffset;
var currentScrollPos = window.pageYOffset;
var wraper = document.getElementsByClassName("bird_top_wraper")[0];
var wraper_list = wraper.getElementsByClassName("bird_menu_child");
var transparent = document.body.classList.contains('transparent_header');
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
            wraper.style.visibility = 'visible';
            wraper.style.opacity = 1;
            wraper.style.backgroundColor = 'white';
            if (transparent) {
                document.getElementById("bird_mobile_menu_dropdown").style.border = 'solid 5px black';
                wraper.getElementsByClassName("bird_logo")[0].getElementsByTagName('a')[0].style.color = 'black';
                for (let el of wraper_list) {
                    el.getElementsByTagName('a')[0].style.color = 'black';
                    if (el.getElementsByClassName('active').length > 0) {
                        el.getElementsByClassName('active')[0].style.setProperty('color', 'white');
                    }
                    el.addEventListener('mouseover',function(){
                        el.getElementsByTagName('a')[0].style.color = 'white';
                        el.getElementsByTagName('a')[0].style.backgroundColor = 'black';
                        if (el.getElementsByClassName('active').length > 0) {
                            el.getElementsByClassName('active')[0].style.color = 'white';
                            el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                        }
                    })
                     el.addEventListener('mouseleave',function(){
                        el.getElementsByTagName('a')[0].style.color = 'black';
                        el.getElementsByTagName('a')[0].style.backgroundColor = 'white';
                        if (el.getElementsByClassName('active').length > 0) {
                            el.getElementsByClassName('active')[0].style.color = 'white';
                            el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                        }
                    })
                }
            }
        }
    } else {
        if (active_menu) {
            wraper.style.visibility = 'hidden';
            wraper.style.opacity = 0;
        }
        active_menu = false;
    }
    if (currentScrollPos == 0 & prevScrollpos != currentScrollPos) {
        if (transparent) {
            wraper.style.backgroundColor = 'transparent';
            wraper.getElementsByClassName("bird_logo")[0].getElementsByTagName('a')[0].style.color = 'white';
            document.getElementById("bird_mobile_menu_dropdown").style.border = 'solid 5px white';
            for (let el of wraper_list) {
                el.getElementsByTagName('a')[0].style.color = 'white';
                el.getElementsByTagName('a')[0].style.backgroundColor = 'transparent';
                if (el.getElementsByClassName('active').length > 0) {
                    el.getElementsByClassName('active')[0].style.color = 'white';
                    el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                }
                el.addEventListener('mouseover',function(){
                    el.getElementsByTagName('a')[0].style.color = 'white';
                    el.getElementsByTagName('a')[0].style.backgroundColor = 'black';
                    if (el.getElementsByClassName('active').length > 0) {
                        el.getElementsByClassName('active')[0].style.color = 'white';
                        el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                    }
                })
                 el.addEventListener('mouseleave',function(){
                    el.getElementsByTagName('a')[0].style.color = 'white';
                    el.getElementsByTagName('a')[0].style.backgroundColor = 'transparent';
                    if (el.getElementsByClassName('active').length > 0) {
                        el.getElementsByClassName('active')[0].style.color = 'white';
                        el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                    }
                })
            }
        }
        active_menu = true;
    }
    prevScrollpos = currentScrollPos;
}

document.getElementById("bird_mobile_menu_dropdown").onclick = function() {
    if (!active_dropdown) {
        active_dropdown = true;
        wraper.style.backgroundColor = 'white';
        wraper.getElementsByClassName("bird_logo")[0].getElementsByTagName('a')[0].style.color = 'black';
        document.getElementById("bird_mobile_menu_dropdown").style.border = 'solid 5px black';
        document.getElementById("bird_mobile_menu_dropdown").classList.add('active');
        for (let el of wraper_list) {
            el.getElementsByTagName('a')[0].style.color = 'black';
            el.getElementsByTagName('a')[0].style.backgroundColor = 'white';
            if (el.getElementsByClassName('active').length > 0) {
                el.getElementsByClassName('active')[0].style.color = 'white';
                el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
            }
            el.addEventListener('mouseover',function(){
                el.getElementsByTagName('a')[0].style.color = 'white';
                el.getElementsByTagName('a')[0].style.backgroundColor = 'black';
                if (el.getElementsByClassName('active').length > 0) {
                    el.getElementsByClassName('active')[0].style.color = 'white';
                    el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                }
            })
             el.addEventListener('mouseleave',function(){
                el.getElementsByTagName('a')[0].style.color = 'black';
                el.getElementsByTagName('a')[0].style.backgroundColor = 'white';
                if (el.getElementsByClassName('active').length > 0) {
                    el.getElementsByClassName('active')[0].style.color = 'white';
                    el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                }
            })
        }
    } else {
        active_dropdown = false;
        if (transparent && currentScrollPos == 0) {
            document.getElementById("bird_mobile_menu_dropdown").style.border = 'solid 5px white';
            wraper.style.backgroundColor = 'transparent';
            wraper.getElementsByClassName("bird_logo")[0].getElementsByTagName('a')[0].style.setProperty('color', 'white');
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
