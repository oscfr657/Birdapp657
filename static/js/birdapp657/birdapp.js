var prevScrollpos = window.scrollY;
var currentScrollPos = window.scrollY;
const darkThemeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
var darkTheme = false;
var wraper = document.getElementsByClassName("bird_top_wraper")[0];
var wraper_list = wraper.getElementsByClassName("bird_menu_child");
var transparent = document.body.classList.contains('transparent_header');
var active_menu = true;
var active_dropdown = false;

window.onscroll = function(e) {
    if (darkThemeMediaQuery.matches) {
        darkTheme = true;
    } else {
        darkTheme = false;
    }
    darkThemeMediaQuery.addEventListener("change", e => {
        if (e.matches) {
            darkTheme = true;
        } else {
            darkTheme = false;
        }
    });

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
            if (darkTheme) {
                wraper.style.backgroundColor = 'black';
            } else {
                wraper.style.backgroundColor = 'white';
                wraper.style.backgroundImage = 'none';
            }
            if (transparent) {
                if (darkTheme) {
                    wraper.getElementsByClassName("bird_logo")[0].firstElementChild.style.color = 'white';
                } else {
                    wraper.getElementsByClassName("bird_logo")[0].firstElementChild.style.color = 'black';
                }
                for (let el of wraper_list) {
                    if (darkTheme) {
                        el.firstElementChild.style.color = 'white';
                    } else {
                        el.firstElementChild.style.color = 'black';
                    }
                    for (let sv of el.getElementsByTagName('svg') ) {
                        for (let child of sv.children) {
                            if (darkTheme) {
                                child.style.stroke = 'white';
                            } else {
                                child.style.stroke = 'black';
                            }
                        }
                    }
                    if (el.getElementsByClassName('active').length > 0) {
                        if (darkTheme) {
                            el.getElementsByClassName('active')[0].style.color = 'black';
                            el.getElementsByClassName('active')[0].style.backgroundColor = 'white';
                        } else {
                            el.getElementsByClassName('active')[0].style.color = 'white';
                            el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                        }
                    }
                    el.addEventListener('mouseover',function(){
                        if (darkTheme) {
                            el.firstElementChild.style.color = 'black';
                            el.firstElementChild.style.backgroundColor = 'white';
                            if (el.getElementsByClassName('active').length > 0) {
                                el.getElementsByClassName('active')[0].style.color = 'black';
                                el.getElementsByClassName('active')[0].style.backgroundColor = 'white';
                            }
                            for (let sv of el.getElementsByTagName('svg') ) {
                                for (let child of sv.children) {
                                    child.style.stroke = 'black';
                                }
                            }
                        } else {
                            el.firstElementChild.style.color = 'white';
                            el.firstElementChild.style.backgroundColor = 'black';
                            if (el.getElementsByClassName('active').length > 0) {
                                el.getElementsByClassName('active')[0].style.color = 'white';
                                el.getElementsByClassName('active')[0].style.backgroundColor = 'black';
                            }
                        }
                    })
                     el.addEventListener('mouseleave',function(){
                        if (darkTheme) {
                            el.firstElementChild.style.color = 'white';
                            el.firstElementChild.style.backgroundColor = 'black';
                            if (el.getElementsByClassName('active').length > 0) {
                                el.getElementsByClassName('active')[0].style.color = 'black';
                                el.getElementsByClassName('active')[0].style.backgroundColor = 'white';
                            }
                            for (let sv of el.getElementsByTagName('svg') ) {
                                for (let child of sv.children) {
                                    child.style.stroke = 'white';
                                }
                            }
                        } else {
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
    if (currentScrollPos == 0 && prevScrollpos != currentScrollPos) {
        if (transparent) {
            if (darkTheme) {
                wraper.style.backgroundColor = 'black';
            } else {
                wraper.style.backgroundImage = 'linear-gradient(to bottom, black, #00000052, transparent)';
            }
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
                    for (let sv of el.getElementsByTagName('svg') ) {
                        for (let child of sv.children) {
                            child.style.stroke = 'white';
                        }
                    }
                })
                 el.addEventListener('mouseleave',function(){
                    el.firstElementChild.style.color = 'white';
                    el.firstElementChild.style.backgroundColor = 'transparent';
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
        if (currentScrollPos == 0 && transparent) {
            wraper.style.backgroundColor = 'transparent';
        }
        document.getElementById("bird_mobile_menu_dropdown").classList.remove('active');
    }
    return false;
}

if (document.readyState !== 'loading') {
    console.log('document is already ready, just execute code here');
    myInitCode();
} else {
    document.addEventListener('DOMContentLoaded', function () {
        console.log('document was not ready, place code here');
        myInitCode();
    });
}
function myInitCode() {
    try {
        console.log('myInitCode');
        let hero_video = document.getElementsByClassName('hero')[0].getElementsByTagName('video')[0];
        let hero_player = document.getElementsByClassName('hero')[0].getElementsByClassName('hero-player')[0];
        if (hero_player != null && hero_video.autoplay == true) {
            hero_player.getElementsByClassName('hero-play')[0].style.display = 'none';
            hero_player.getElementsByClassName('hero-pause')[0].style.display = 'block';
        } else if (hero_player != null) {
            hero_player.getElementsByClassName('hero-play')[0].style.display = 'block';
            hero_player.getElementsByClassName('hero-pause')[0].style.display = 'none';
        }
        if (hero_player != null && hero_video.muted == true ) {
            hero_player.getElementsByClassName('hero-muted')[0].style.display = 'block';
            hero_player.getElementsByClassName('hero-sound')[0].style.display = 'none';
        } else if (hero_player != null) {
            hero_player.getElementsByClassName('hero-muted')[0].style.display = 'none';
            hero_player.getElementsByClassName('hero-sound')[0].style.display = 'block';
        }
    }
    catch(err) {
        console.log('No video on this page.');
    }
};

function birdPlay(element) {
    element.parentNode.parentNode.getElementsByTagName('video')[0].play();
    element.nextElementSibling.style.display = 'block';
    element.style.display = 'none';
}
function birdPause(element) {
    element.parentNode.parentNode.getElementsByTagName('video')[0].pause();
    element.previousElementSibling.style.display = 'block';
    element.style.display = 'none';
}
function birdSound(element) {
    element.parentNode.parentNode.getElementsByTagName('video')[0].muted = false;
    element.nextElementSibling.style.display = 'block';
    element.style.display = 'none';
}
function birdMute(element) {
    element.parentNode.parentNode.getElementsByTagName('video')[0].muted = true;
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