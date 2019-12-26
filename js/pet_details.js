    let pet = localStorage.getItem("pet");
    let petName = localStorage.getItem("petName");
    let petBreed = localStorage.getItem("petBreed");
    let petLocation = localStorage.getItem("petLocation");
    let petGender = localStorage.getItem("petGender");
    let petStatus = localStorage.getItem("petStatus");

    let currentPet = document.querySelector(".pet_img img");
    let petImage = (currentPet.attributes[0]);
    petImage.value = pet;
    document.querySelector(".pet_type").innerHTML = petName;
    document.querySelector(".pet_breed").innerHTML = petBreed;
    document.querySelector(".pet_location").innerHTML = petLocation;
    document.querySelector(".gender").innerHTML = petGender;
    document.querySelector(".status").innerHTML = petStatus;
    

    //pair button function
let init = 0;
document.querySelector("#pair").addEventListener("click",function (){
(init ==0) ? alert("Listing Recorded") & (init=1) : confirm("You are listing your pet again!")
})