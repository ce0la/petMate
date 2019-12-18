let pet = localStorage.getItem('pet');

console.log(pet);
let petImage = document.querySelector('.row-2 img');
let petImageSrc = petImage.attributes[0];
petImageSrc.value = pet;
console.log(petImage)