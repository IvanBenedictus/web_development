let timeoutId;
const nav = document.querySelector("#nav");

function showNav(){
    nav.classList.add("show");
}

function hidewNav(){
    nav.classList.remove("show");
}

var currPos = window.scrollY;

document.addEventListener("scroll", () => {
    if (window.scrollY <= currPos) {
    //scroll up
        hidewNav();
    } else {
    //scroll down
        showNav();
    }
    currPos = window.scrollY;
});

document.addEventListener("click", () => {
    timeoutId = setTimeout(() => {
        hidewNav();
    }, 1000);
})