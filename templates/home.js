const navbarE1 = document.querySelector(".navbar");
const bottomContainerE1 = document.qyerySelector(".bottom-container");
console.log(navbarE1.offsetHeight);
console.log(bottomContainerE1.offsetTop);


window.addEventListener("scroll", () => {
    if (windows.scrollY > bottomContainerE1.offsetTop - navbarE1.offsetHeight - 50
    ) {
        navbarE1.classList.add("active");
    } else {
        navbarE1.classList.remove("active")
    }

});