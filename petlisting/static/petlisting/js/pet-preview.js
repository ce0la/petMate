let pet = localStorage.getItem('pet');
let petName = localStorage.getItem("petName");
let petBreed = localStorage.getItem("petBreed");
let petLocation = localStorage.getItem("petLocation");

console.log(pet, petName, petBreed, petLocation);
document.querySelector(".pet_name").innerHTML = petName;
document.querySelector(".pet_breed").innerHTML = petBreed;
document.querySelector(".pet_location").innerHTML = petLocation;
let petImage = document.querySelector('.row-2 img');
let petImageSrc = petImage.attributes[0];
petImageSrc.value = pet;
