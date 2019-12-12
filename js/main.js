// navbar function 
let navButton = document.getElementById("navButton");
let navbar = document.getElementById("nav");
navButton.addEventListener("click", ()=>{
  if (navbar.style.display == ""){
    navbar.style.display = "block";
  }
  else {
      navbar.style.display = "";
  }
})