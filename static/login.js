function showPassword() {
	let eyesClasses = document.activeElement.children[0].classList
	let inputPassword = document.getElementById("password")


	// si l'input est de type password et l'oeil est fermé
	if (eyesClasses.contains("fa-eye-slash")) {
		eyesClasses.replace("fa-eye-slash", "fa-eye");
		inputPassword.type = "text";
	}
	// sinon si l'input est de type text et l'oeil est ouvert
	else { // if (eyesClasses.contains("fa-eye")) (and other)
		eyesClasses.replace("fa-eye", "fa-eye-slash");
		inputPassword.type = "password";
	}
}