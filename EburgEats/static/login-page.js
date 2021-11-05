const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;
    console.log('heello')
    // check for approprate length 
    // Username and Password <= 25 characters
    // Email <= 35 characters

    // check for '@cwu.edu' extension
    // prompt user to re enter information until valid

    if (username === "user" && password === "password") {
        alert("You have successfully logged in.");
        // send user back to home page after sucessful login (use the name of the page)
        location.href = 'home';
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})