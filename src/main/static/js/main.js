function OpenNav() {
	const navIcon = document.querySelector('#nav-icon');
	const nav = document.querySelector('#nav-links');
	const navLinks = document.querySelectorAll('#nav-links li a.animation');
	nav.classList.toggle('nav-active');

	// Animate Links
	navLinks.forEach((link, index) => {
		if (link.style.animation) {
			link.style.animation = '';
		} else {
			link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.4}s`;
		}
	});
	// NavIcon Animation
	navIcon.classList.toggle('toggle');
}

let inputs = document.querySelectorAll("input, textarea");

inputs.forEach((input) => {
    input.addEventListener("focus", () => {
        input.setAttribute("data-placeholder", input.placeholder);
        input.placeholder = "";
    });
    input.addEventListener("blur", () => {
        input.placeholder = input.getAttribute("data-placeholder");
        input.setAttribute("data-placeholder", "");
    });
});

let dropdown = document.querySelector("li.dropdown, .dropdown ul");

if (document.body.contains(dropdown)) {
    dropdown.addEventListener("click", (event) => {
        event.preventDefault();
        if (!dropdown.classList.contains("opened")) {
            dropdown.classList.add("opened");
            dropdown.querySelector("ul").style.display = "block";
        } else {
            dropdown.classList.remove("opened");
            dropdown.querySelector("ul").style.display = "none";
        }
    });
    
    dropdown.addEventListener("click", (event) => {
        event.preventDefault();
        dropdown.classList.add("opened");
        dropdown.querySelector("ul").style.display = "block";
    }, {once : true});
    
    dropdown.addEventListener("mouseover", () => {
        dropdown.classList.add("opened");
        dropdown.querySelector("ul").style.display = "block";
    });
    
    dropdown.addEventListener("mouseout", () => {
        dropdown.classList.remove("opened");
        dropdown.querySelector("ul").style.display = "none";
    });
}

let dynamicInputs = document.querySelectorAll(".login-input");

dynamicInputs.forEach((input) => {
    input.addEventListener('focus', () => {
        let inputid = input.getAttribute("id");
        document.querySelector(`.${inputid}`).setAttribute('data-color', document.querySelector(`.${inputid}`).style.color);
        document.querySelector(`.${inputid}`).style.color = "#fff";
    });
    input.addEventListener('focusout', () => {
        let inputid = input.getAttribute("id");
        document.querySelector(`.${inputid}`).style.color = document.querySelector(`.${inputid}`).getAttribute('data-color');
    });
});