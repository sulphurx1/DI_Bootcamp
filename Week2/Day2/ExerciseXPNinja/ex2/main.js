let zipcode = prompt(`Please enter your zipcode`);

if(zipcode.length < 5){
    alert(`Error`)
    alert(`Should consist of 5 numbers`)
}
else if(zipcode.match(/[a-zA-z]/i) && zipcode.indexOf(' ') == -1){
    alert(`Error`)
    alert(`Should consist of only numbers`)
}

else if(zipcode.indexOf(' ') >= 0){
    alert(`Error`)
    alert(`Must not contain spaces`)
}

else if(zipcode.length > 5){
    alert(`Error`)
    alert(`Must not be greater than 5 digits in length`)
}

else{
    alert(`Success`)
}