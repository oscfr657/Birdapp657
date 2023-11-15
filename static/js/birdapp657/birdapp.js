var prevScrollpos = window.scrollY;
var currentScrollPos = window.scrollY;
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
    currentScrollPos = window.scrollY;
    if (prevScrollpos > currentScrollPos) {
        if (!active_menu) {
            active_menu = true;
            wraper.style.visibility = 'visible';
            wraper.style.opacity = 1;
            wraper.style.backgroundColor = 'white';
            if (transparent) {
                wraper.getElementsByClassName("bird_logo")[0].firstElementChild.style.color = 'black';
                for (let el of wraper_list) {
                    el.firstElementChild.style.color = 'black';
                    for (let sv of el.getElementsByTagName('svg') ) {
                        for (let child of sv.children) {
                            child.style.stroke = 'black';
                        }
                    }
                    if (el.getElementsByClassName('active').length > 0) {
                        el.getElementsByClassName('active')[0].style.setProperty('color', 'white');
                    }
                    el.addEventListener('mouseover',function(){
                        el.firstElementChild.style.color = 'white';
                        el.firstElementChild.style.backgroundColor = 'black';
                        if (el.getElementsByClassName('active').length > 0) {
                            el.getElementsByClassName('active')[0].style.color = 'white';
                            el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                        }
                    })
                     el.addEventListener('mouseleave',function(){
                        el.firstElementChild.style.color = 'black';
                        el.firstElementChild.style.backgroundColor = 'white';
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
            for (let el of wraper_list) {
                el.firstElementChild.style.color = 'white';
                el.firstElementChild.style.backgroundColor = 'transparent';
                for (let sv of el.getElementsByTagName('svg') ) {
                    for (let child of sv.children) {
                        child.style.stroke = 'white';
                    }
                }
                if (el.getElementsByClassName('active').length > 0) {
                    el.getElementsByClassName('active')[0].style.color = 'white';
                    el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                }
                el.addEventListener('mouseover',function(){
                    el.firstElementChild.style.color = 'white';
                    el.firstElementChild.style.backgroundColor = 'black';
                    if (el.getElementsByClassName('active').length > 0) {
                        el.getElementsByClassName('active')[0].style.color = 'white';
                        el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                    }
                })
                 el.addEventListener('mouseleave',function(){
                    el.firstElementChild.style.color = 'white';
                    el.firstElementChild.style.backgroundColor = 'transparent';
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
        document.getElementById("bird_mobile_menu_dropdown").classList.add('active');
        for (let el of wraper_list) {
            el.firstElementChild.style.color = 'black';
            el.firstElementChild.style.backgroundColor = 'white';
            if (el.getElementsByClassName('active').length > 0) {
                el.getElementsByClassName('active')[0].style.color = 'white';
                el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
            }
            for (let sv of el.getElementsByTagName('svg') ) {
                for (let child of sv.children) {
                    child.style.stroke = 'black';
                }
            }
            el.addEventListener('mouseover',function(){
                el.firstElementChild.style.color = 'white';
                el.firstElementChild.style.backgroundColor = 'black';
                if (el.getElementsByClassName('active').length > 0) {
                    el.getElementsByClassName('active')[0].style.color = 'white';
                    el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                }
                for (let sv of el.getElementsByTagName('svg') ) {
                    for (let child of sv.children) {
                        child.style.stroke = 'white';
                    }
                }
            })
             el.addEventListener('mouseleave',function(){
                el.firstElementChild.style.color = 'black';
                el.firstElementChild.style.backgroundColor = 'white';
                if (el.getElementsByClassName('active').length > 0) {
                    el.getElementsByClassName('active')[0].style.color = 'white';
                    el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                }
                for (let sv of el.getElementsByTagName('svg') ) {
                    for (let child of sv.children) {
                        child.style.stroke = 'black';
                    }
                }
            })
        }
    } else {
        active_dropdown = false;
        if (currentScrollPos == 0 & transparent) {
            wraper.style.backgroundColor = 'transparent';
        }
        document.getElementById("bird_mobile_menu_dropdown").classList.remove('active');
    }
    return false;
}

function birdPlay(element) {
    element.parentNode.parentNode.getElementsByTagName('video')[0].play();
    element.nextElementSibling.style.display = 'block';
    element.style.display = 'none';
}
function birdPause(element) {
    element.parentNode.parentNode.getElementsByTagName('video')[0].pause()
    element.previousElementSibling.style.display = 'block';
    element.style.display = 'none';
}

function openSearch() {
  document.getElementById("BirdSearchOverlay").style.display = "block";
  document.getElementById("id_search_query").focus();
  return false;
}
function closeSearch() {
  document.getElementById("BirdSearchOverlay").style.display = "none";
  return false;
}