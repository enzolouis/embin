let secure8letters = false;
let secureCapital = false;
let secureSpecial = false;
let secureNumber = false;
var isValidPassword = false;
var isValidPasswordVerify = false;
var isValidLogin = false;


document.getElementById("password").addEventListener("input", function(event) {
    let content = document.getElementById("password").value;
    document.getElementById("password").value = document.getElementById("password").value.replace(' ', '');
    content = document.getElementById("password").value;
    

    let formatSpecial = /^[a-zA-Z0-9]*$/
    let formatCapital = /[A-Z]/
    let formatNumber  = /[0-9]/

    secure8letters= content.length >= 8
    secureCapital = formatCapital.test(content);
    secureSpecial = !formatSpecial.test(content);
    secureNumber  = formatNumber.test(content);

    document.getElementById("secure-8letters").style.display = secure8letters ? 'none' : 'block'
    document.getElementById("secure-capital").style.display  = secureCapital  ? 'none' : 'block'
    document.getElementById("secure-special").style.display  = secureSpecial  ? 'none' : 'block'
    document.getElementById("secure-number").style.display   = secureNumber   ? 'none' : 'block'

    let sumSecure;

    if (content.length == 0) {
        sumSecure = 0;
        document.getElementById("secure-password-details").style.height = "0";
    } else {
        sumSecure = secure8letters * 20 + 20 + secureCapital * 20 + secureSpecial * 20 + secureNumber * 20;
        if (sumSecure == 100) {
            isValidPassword = true;
            document.getElementById("secure-password-details").style.height = "0";
        } else {
            isValidPassword = false;
            document.getElementById("secure-password-details").style.height = "40px";            
        }
    }

    let barWidth = sumSecure+"%";
    let barColor;

    if (sumSecure <= 20) {
        barColor = "rgb(192, 57, 43)";
    } else if (sumSecure <= 40) {
        barColor = "rgb(231, 76, 60)";
    } else if (sumSecure <= 60) {
        barColor = "rgb(230, 126, 34)";
    } else if (sumSecure <= 80) {
        barColor = "rgb(241, 196, 15)";
    } else {
        barColor = "rgb(46, 204, 113)";
    }

    document.getElementById("secure-password").style.color = barColor;
    
    let style = document.getElementById("passwordDiv").style;
    style.setProperty('--register-bar-password-color', barColor);
    style.setProperty('--register-bar-password-width', barWidth);

    passwordVerifyEventListener()
});


document.getElementById("password-verify").addEventListener("input", function() {
    passwordVerifyEventListener()
});

function passwordVerifyEventListener() {
    let contentPassword = document.getElementById("password").value;
    let contentPasswordVerify = document.getElementById("password-verify").value;
    document.getElementById("password-verify").value = contentPasswordVerify.replace(' ', '');
    contentPasswordVerify = document.getElementById("password-verify").value;

    let style = document.getElementById("passwordVerifyDiv").style;

    if (contentPasswordVerify.length == 0) {
        style.setProperty('--register-bar-password-verify-width', '0%');
        document.getElementById("secure-password-verify-details").style.height = "0";
    } else {
        style.setProperty('--register-bar-password-verify-width', '100%');
        document.getElementById("secure-password-verify-details").style.height = "15px";            
    }

    if (contentPassword == contentPasswordVerify) {
        if (isValidPassword) {
            isValidPasswordVerify = true;
            style.setProperty('--register-bar-password-verify-color', 'rgb(46, 204, 113)');
            document.getElementById("secure-password-verify-details").style.height = "0";
        } else {
            isValidPasswordVerify = false;
            style.setProperty('--register-bar-password-verify-color', 'rgb(231, 76, 60)');
        }
        
    } else {
        isValidPasswordVerify = false;
        style.setProperty('--register-bar-password-verify-color', 'rgb(231, 76, 60)');
    }

    if (isValidPassword) {
        document.getElementById("message-valid-verify").innerHTML = "&#8226 Password does not match"
    } else {
        document.getElementById("message-valid-verify").innerHTML = "&#8226 Password not valid yet"
    }
}   

document.getElementById("username").addEventListener('input', function(event) {
    document.getElementById("username").value = document.getElementById("username").value.replace(/[^a-zA-Z0-9]/g, '');

    let username = document.getElementById("username").value;
    let csrftoken = getCookie('csrftoken');

    $.ajax({
        type: 'POST',
        url: '../userExists',
        data: {
            username: username,
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function(data) {
            if (data === "exist") {
                isValidLogin = false;
                document.getElementById("secure-login-details").style.height = "15px";
            } else {
                isValidLogin = true;
                document.getElementById("secure-login-details").style.height = "0";
            }
        }
    })
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Récupérer le jeton CSRF du cookie nommé 'csrftoken'
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
/*
document.getElementById("form-reg").addEventListener("submit", function(e) {
    if (isValidPassword && isValidPasswordVerify && isValidLogin) {
        return true;
    }
    e.preventDefault();
})*/


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

let isRegisterPasswordVerifyShow = false;
document.getElementById("hide-password-verify").addEventListener("click", function() {
    let element = document.getElementById("hide-password-verify");

    if (isRegisterPasswordVerifyShow) {
        element.innerHTML = '<i class="fa-solid fa-eye"></i>';
        document.getElementById("password-verify").type = "password";
        isRegisterPasswordVerifyShow = false;
    } else {
        element.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
        document.getElementById("password-verify").type = "text";
        isRegisterPasswordVerifyShow = true;
    }
})