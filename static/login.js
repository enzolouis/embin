document.getElementById("password").addEventListener("input", function(event) {
    document.getElementById("password").value = document.getElementById("password").value.replace(' ', '');
});

document.getElementById("login").addEventListener('input', function(event) {
    document.getElementById("login").value = document.getElementById("login").value.replace(/[^a-zA-Z0-9]/g, '');
});


let isRegisterPasswordShow = false;

document.getElementById("hide-password").addEventListener("click", function() {
    let element = document.getElementById("hide-password");

    if (isRegisterPasswordShow) {
        element.innerHTML = '<i class="fa-solid fa-eye"></i>';
        document.getElementById("password").type = "password";
        isRegisterPasswordShow = false;
    } else {
        element.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
        document.getElementById("password").type = "text";
        isRegisterPasswordShow = true;
    }
})