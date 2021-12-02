const registerForm = document.getElementById("register-form");
const registerButton = document.getElementById("register-form-submit");

registerButton.addEventListener("click", (e) => {
    e.preventDefault();
    const email = registerForm.email.value;
    const username = registerForm.username.value;
    const password1 = registerForm.password1.value;
    const password2 = registerForm.password2.value;

    if (!(email != "" && username != "" && password1 != "" && password2 != "")) {
        alert("Please fill out all fields.");
    } else if (password1 === password2) {
        alert("Success! Please check your email to verify your account.");
        location.reload();
    } else {
        alert("Passwords do not match!");
    }
})