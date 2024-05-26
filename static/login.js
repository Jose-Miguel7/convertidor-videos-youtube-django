
const verLogin = () => {
    const changeView = () => {
        document.querySelector('.content-responsive').classList.toggle('content-responsive-transition')
        document.querySelector('.content-responsive-login').classList.toggle('content-responsive-transition')
        setTimeout(() => {
            document.querySelector('.content-responsive').classList.toggle('content-responsive-transition')
            document.querySelector('.content-responsive-login').classList.toggle('content-responsive-transition')
        }, 10)

        document.querySelector('.nav-login').classList.toggle('nav-login-invert');
        document.querySelector('.content-responsive').classList.toggle('content-responsive-invert');
        document.querySelector('.presentation-container').classList.toggle('presentation-container-invert');
        document.querySelector('.copyright').classList.toggle('copyright-invert');
        document.querySelector('.login').classList.toggle('display-none');
        document.querySelector('.register').classList.toggle('display-none');
    }

    if (!login || (login && document.querySelector('.nav-login').className.includes('nav-login-invert'))) {
        changeView()
    }
}
verLogin();


const loginBtn = document.querySelector('#login-btn');
const registerBtn = document.querySelector('#register-btn');

loginBtn.addEventListener('click', () => {
    login = true;
    verLogin();
})

registerBtn.addEventListener('click', () => {
    login = false;
    verLogin();
})

const spinner = document.querySelector('#spinner');
const contentsButton = document.querySelector('.content-buttons');
const buttonEmail = document.querySelector('#email');
const registerForm = document.querySelector('#register-form');

buttonEmail.addEventListener('click', () => {
    spinner.classList.toggle('display-none');
    contentsButton.classList.toggle('display-none');
    setTimeout(() => {
        spinner.classList.toggle('display-none')
        registerForm.classList.toggle('display-none')
    }, 1000)
})