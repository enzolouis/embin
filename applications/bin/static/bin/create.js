const submit = document.getElementById("submit");
const content = document.getElementById("content")

content.addEventListener("keydown", function(event) {
	if (event.keyCode != 9) return

	event.preventDefault();
	submit.classList.add("active");
	let start = this.selectionStart; // words before tab
	let end = this.selectionEnd; // words after tab

	this.value = this.value.substring(0, start) + "\t" + this.value.substring(end);

	// reset cursor at the good place
	this.selectionStart = start + 1;
	this.selectionEnd = start + 1;
});

function checkActive() {
	if (!content.value) {
		submit.classList.remove("menu-bottom__btn-create-enabled")
		submit.type = "button"
	} else {
		submit.classList.add("menu-bottom__btn-create-enabled")
		submit.type = "submit"
	}
}

window.onload = checkActive()
content.addEventListener("input", checkActive)


let tags = [];

let lstTagsDisplayed = false;

function showDefinedTags(event) {
	if (!lstTagsDisplayed) {
		document.getElementById('lst-defined-tags').style.visibility = "visible";
		setTimeout(() => {
            document.addEventListener('click', hideOnClickAtOtherPlace);
        }, 0);
	lstTagsDisplayed = true;
	}
}

function hideOnClickAtOtherPlace() {
	document.getElementById('lst-defined-tags').style.visibility = "hidden";
	lstTagsDisplayed = false;
	document.removeEventListener('click', hideOnClickAtOtherPlace)
}



function deleteTag(p) {
	p.remove();
	text = p.innerText
	// remove from tags
	let index = tags.indexOf(text);
	if (index !== -1) {
	    tags.splice(index, 1);
	}
	Array.from(document.getElementById('lst-defined-tags').children).forEach(function(item, index) {
		if (item.id == text) {
			item.style.display = "block";
		}
	})
}

function clickOnTag(li) {
	li.style.display = "none";
	let tag = li.innerText
	document.getElementById('lst-tags-tags').innerHTML += "<p onclick='deleteTag(this)' class='list-bin-tag "+tag+"'>"+tag+"</p>"
	tags.push(tag)
}

function fillTagsInHiddenInputOnSubmit(event) {
	document.getElementById('tags').value = tags.join(',')
}

