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

let petsContainer = document.querySelectorAll('section.pets article');
petsContainer.forEach(pets=>{
    pets.addEventListener('click', ()=>{
    let imgSrc = pets.children[0].src;
    console.log(imgSrc);
    localStorage.setItem('pet', imgSrc);
    location.replace('pet-preview.html')
  });
})
