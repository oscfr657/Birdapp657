var prevScrollpos = window.scrollY;
var currentScrollPos = window.scrollY;
const darkThemeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
var darkTheme = false;
var header = document.getElementsByTagName("header")[0];
var nav = document.getElementsByTagName("nav")[0];
var menu = nav.getElementsByClassName("bird_menu")[0];
var menu_list = nav.getElementsByClassName("bird_menu_list");
var transparent = document.body.classList.contains('transparent_header');
var bodyTag = document.body;
var active_menu = true;
var active_dropdown = false;

window.onload = function(e) {
    if (darkThemeMediaQuery.matches) {
        darkTheme = true;
        bodyTag.classList.add("darkTheme");
    } else {
        darkTheme = false;
        bodyTag.classList.remove("darkTheme");
    }
    darkThemeMediaQuery.addEventListener("change", e => {
        if (e.matches) {
            darkTheme = true;
            bodyTag.classList.add("darkTheme");
        } else {
            darkTheme = false;
            bodyTag.classList.remove("darkTheme");
        }
    });
}

window.onscroll = function(e) {
    if (active_dropdown) {
        e.preventDefault();
        return false;
    }
    currentScrollPos = window.scrollY;
    if (prevScrollpos > currentScrollPos) {
        //console.log('scroll up');
        if (!active_menu) {
            active_menu = true;
            header.style.visibility = 'visible';
            header.style.opacity = 1;
            nav.style.visibility = 'visible';
            nav.style.opacity = 1;
            bodyTag.classList.add("scrollUp");
        }
        active_menu = true;
    } else {
        //console.log('scroll down');
        if (active_menu) {
            header.style.visibility = 'hidden';
            header.style.opacity = 0;
            nav.style.visibility = 'hidden';
            nav.style.opacity = 0;
        }
        active_menu = false;
        bodyTag.classList.remove("scrollUp");
    }
    if (currentScrollPos == 0 && prevScrollpos != currentScrollPos) {
        bodyTag.classList.remove("scrollUp");
        active_menu = true;
    } 
    prevScrollpos = currentScrollPos;
}

document.getElementById("bird_mobile_menu_dropdown").onclick = function() {
    if (!active_dropdown) {
        active_dropdown = true;
        bodyTag.classList.add("mobile_menu");
        document.getElementById("bird_mobile_menu_dropdown").classList.add('active');
    } else {
        console.log('active_dropdown');
        active_dropdown = false;
        bodyTag.classList.remove("mobile_menu");
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
        //console.log('myInitCode');
        let heroSliders = document.getElementsByClassName('hero-slider');
        for (let i = 0; i < heroSliders.length; i++) {
            let slides = heroSliders[i].getElementsByClassName('hero');
            heroSliders[i].setAttribute("data-slideindex", 1);
            showSlide(slides, 1)
        }
        let heros = document.getElementsByClassName('hero');
        for (let i = 0; i < heros.length; i++) {
            let hero = heros[i];
            let hero_video = hero.getElementsByTagName('video')[0];
            let hero_player = hero.getElementsByClassName('hero-player')[0];
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
    }
    catch(err) {
        console.log(err);
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

function minusDivs(b) {
    slideIndex = parseInt(b.parentNode.dataset.slideindex) - 1;
    slides = b.parentNode.getElementsByClassName('hero');
    slideIndex = showSlide(slides, slideIndex);
    b.parentNode.setAttribute("data-slideindex", slideIndex);
}
function plusDivs(b) {
    slideIndex = parseInt(b.parentNode.dataset.slideindex) + 1;
    slides = b.parentNode.getElementsByClassName('hero');
    slideIndex = showSlide(slides, slideIndex);
    b.parentNode.setAttribute("data-slideindex", slideIndex);
}
function showSlide(slides, slideIndex) {
    if (slideIndex > slides.length) {slideIndex = 1};
    if (slideIndex < 1) {slideIndex = slides.length};
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex-1].style.display = "flex";
    return slideIndex
}
