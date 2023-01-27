function playTheGame() {
    const isPlayerReady = confirm(`Are you sure you want to play?`)
    if (!isPlayerReady) {
        alert(`No Problem, Goodbye!`)
        return
    }

    let number = prompt(`Please enter a Number`);
    let trialsNumber = 0;
    const computerNumber = randomValue();
    console.log(number, computerNumber);
    while(number != computerNumber) {
        trialsNumber += 1;
        if(trialsNumber === 3) {
            alert (`out of chances`)
            return
        }

        if(!isOnlyNumbers(number)) {
            alert(`Sorry Not a number, GoodBye!`)
            return
        }
        console.log(`We are playing the game`)
        if(!isNumberBetweenZeroAndTen(number)) {
            alert(`Sorry it’s not a good number, Goodbye`)
            return
        }
        if(number > computerNumber) {
            alert (`Your number is bigger then the computer’s, guess again`)
        }
        if(number < computerNumber) {
            alert (`Your number is smaller then the computer’s, guess again`)
        }
        number = prompt(`Please enter a Number`);
    }
    alert(`WINNER!!!`);

    

}

function isOnlyNumbers(str) {
    const regex = new RegExp(/^[0-9]*$/)
    return regex.test(str)
}

function isNumberBetweenZeroAndTen(num) {
    return num >= 0 && num <= 10
}

function randomValue() {
    return Math.floor(Math.random() * 11)

}
