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
let pet_name = document.querySelectorAll(".pet_name");
let pet_breed = document.querySelectorAll(".pet-breed");
let pet_location = document.querySelectorAll(".pet_location");
let pet_gender = document.querySelectorAll(".gender");
let pet_status = document.querySelectorAll(".status");
console.log(pet_gender, pet_status)
petsContainer.forEach((pets, index)=>{
    pets.addEventListener('click', ()=>{
    let imgSrc = pets.children[0].src;
    let petName = pet_name[index].innerHTML;
    let petBreed = pet_breed[index].innerHTML;
    let petLocation = pet_location[index].innerHTML;
    let petGender = pet_gender[index].innerHTML;
    let petStatus = pet_status[index].innerHTML;
    console.log(imgSrc,petName, petBreed, petLocation);
    localStorage.setItem('pet', imgSrc);
    localStorage.setItem("petName", petName)
    localStorage.setItem("petBreed", petBreed)
    localStorage.setItem("petLocation", petLocation)
    localStorage.setItem("petGender", petGender)
    localStorage.setItem("petStatus", petStatus)
    location.assign('pet-preview.html')
  });
})
