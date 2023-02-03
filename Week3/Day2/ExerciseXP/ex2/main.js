const form = document.querySelector('form');
let firstElement = document.getElementById('fname');
let secondElement = document.getElementById('lname');

const button = document.getElementById('submit');


function logFormInput(event) {
    event.preventDefault();
    const firstName = document.getElementById('fname').value;
    const secondName = document.getElementById('lname').value;

    console.log(firstName, secondName);

    if (firstName === '' || secondName === '') {
        alert('Please fill both first name and second name please!')
    }

    else {
        let userAnswer = document.querySelector('.usersAnswer');
        let firstLi = document.createElement('li');
        let secondLi = document.createElement('li');

        firstLi.innerHTML = firstName;
        secondLi.innerHTML = secondName;
        userAnswer.append(firstLi, secondLi);
    }


}

button.addEventListener('click', logFormInput);
