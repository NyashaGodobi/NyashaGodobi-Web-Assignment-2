//input fields
let subName = document.getElementById('name');
let subNumber = document.getElementById('number');
let email = document.getElementById('email');
let enquiry = document.getElementById('enquiry');

//errorFields
let nameError = document.getElementById('nameError');
let numberError = document.getElementById('numberError');
let emailError = document.getElementById('emailError');
let enquiryError = document.getElementById('enquiryError');


function validateMyForm() {
    //emptiness
    if(subName.value===""){
        nameError.innerText = "Name is empty";
    }
    else if(subNumber.value===""){
        numberError.innerText = "Number is empty";
    }
    else if(email.value===""){
        emailError.innerText = "Email is empty";
    }
    else if(enquiry.value===""){
        enquiryError.innerText = "Enquiry is empty";
    }
    //name
    else if(
        subName.value.match(/^[0-9]+$/)
    ){
        nameError.innerText = "Invalid Name";
    }
    //number
    else if(
        subNumber.value.match(/^[A-Za-z]+$/)
    ){
        numberError.innerText = "Invalid Number";
    }
    //email
    else if(
        !email.value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)
    ){
        emailError.innerText = "Invalid Email";
    }
    //information is valid
    else {
        alert("Enquiry successfully submitted!");
        clearForm();
    }

}

function clearForm() {
    subName.value = subNumber.value = email.value = enquiry.value = nameError.innerHTML = numberError.innerHTML = emailError.innerHTML = enquiryError.innerHTML = "";
}