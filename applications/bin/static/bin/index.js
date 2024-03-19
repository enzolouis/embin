function deleteLoginOrRegisterSucceedGetURL() {
    var url = window.location.href;

    if (url.indexOf('loginSucceed=') !== -1 || url.indexOf('registerSucceed=') !== -1) {
        var newURL = url.replace(/([?&])(loginSucceed|registerSucceed)=[^&]+(&|$)/, '$1');
        
        window.history.replaceState({}, document.title, newURL);
    }
}

deleteLoginOrRegisterSucceedGetURL();


function ajaxAddBinToFavorite(event, binCode) {
	let csrftoken = getCookie('csrftoken');
	
	$.ajax({
		type:"POST",
		url:"./addtofav",
		data:"code=" + binCode,

		headers: {
            'X-CSRFToken': csrftoken
        },

		success:function(data) {
			if (data === "add") {
				Array.from(document.getElementsByClassName(binCode)).forEach(function(item, index) {
				    item.children[0].innerHTML = '<i class="fa-solid fa-star"></i>';
				    item.children[0].children[0].style.transform = "scale(1.5)"
				    item.children[0].classList.add("favorite")
		            setTimeout(() => {
		                item.children[0].children[0].style.transform = "none"},
		            100);
		            itemToClone = item.cloneNode(true)
		            itemToClone.children[0].children[0].style.transform = "none"
				});
				document.getElementById("list-bin-favorites").appendChild(itemToClone.cloneNode(true));
			} else if (data === "remove") {
				Array.from(document.getElementsByClassName(binCode)).forEach(function(item, index) {
				    item.children[0].innerHTML = '<i class="fa-regular fa-star"></i>';
				    item.children[0].children[0].style.transform = "scale(1.5)"
				    item.children[0].classList.remove("favorite")
		            setTimeout(() => {
		                item.children[0].children[0].style.transform = "none"},
		            100);
				});

				console.log(document.getElementById("list-bin-favorites").children)
				Array.from(document.getElementById("list-bin-favorites").children).forEach(function(item, index) {
					if (item.classList.contains(binCode)) {
						item.remove()
					}
				});
			}
		}
	});
}

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