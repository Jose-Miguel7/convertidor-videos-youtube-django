const menuOpen = document.querySelector('.nav-menu');
const itemsContainer = document.querySelector('.nav-items-container');

menuOpen.addEventListener('click', () => {
    menuOpen.classList.toggle('nav-menu__active');
    itemsContainer.classList.toggle('nav-items-container__active');
});

window.addEventListener('resize', () => {
    console.log(window.innerWidth > 670)
    if ((window.innerWidth > 670) && (menuOpen.className.includes('__active'))) {
        menuOpen.classList.toggle('nav-menu__active');
        itemsContainer.classList.toggle('nav-items-container__active');
    }
})