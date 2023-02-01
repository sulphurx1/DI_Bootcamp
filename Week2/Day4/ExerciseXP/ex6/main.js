
hotelCost()

const cost = {
    london: '\$183',
     paris: '\$220',
     others: '\$300'
}

function hotelCost() {

    let answer;

    while(!isOnlyNumber(answer)) {
        answer = prompt('How many nights would you like to stay?');
    }

    const numberOfNights = Number(answer);
    const costPerNight = 140;
    const totalPrice = numberOfNights * costPerNight;

    console.log('Hotel price: \$' + totalPrice);

    return totalPrice
}

function isOnlyNumber(string) {
    const regex = new RegExp(/^[0-9]*$/);
    return regex.test(string);
}
const price1 = planeRideCost();
console.log('The plane price: ' + price1 )

function planeRideCost() {

    let input = '';

    while(!isTheAnswer(input)) {
        input = prompt('Where would you like to go?\n A. London\n B. Paris\n C. Others')
    }
    
    if(input === 'A') {
        return cost.london;
    }
    else if(input === 'B') {
        return cost.paris;
    }
    else {
        return cost.others;
    }
    
    }

function isTheAnswer(str) {
    const regex = new RegExp(/^[ABC]/g);
    return regex.test(str)
}
rentalCarCost()

function rentalCarCost() {

    let answer;

    while(!isOnlyNumber(answer)) {
        answer = prompt('How many days would you like to rent the car?');
    }

    const dailyPrice = 40;
    const numberOfDays = answer;
    let discount = 0;
    if(numberOfDays >= 10) {
        discount = 0.05;
    }

    const totalPrice = dailyPrice * numberOfDays *(1 - discount);
    console.log('Car price: \$' + totalPrice);
    return totalPrice
}

function totalVacationCost() {

    let carAnswer;
    let hotelAnswer;
    let planeInput = '';

    while(!isOnlyNumber(carAnswer)) {
        carAnswer = prompt('How many days would you like to rent the car?');
    }



    while(!isTheAnswer(planeInput)) {
        planeInput = prompt('Where would you like to go?\n A. London\n B. Paris\n C.Others')
    }
  

    while(!isOnlyNumber(hotelAnswer)) {
        hotelAnswer = prompt('How many nights would you like to stay?');
    }

    console.log(`Car Price ` + carAnswer(carAnswer) );
    console.log(`Hotel Price ` + hotelAnswer(hotelAnswer));
    console.log(`Plane Price ` + planeInput(planeInput) );


}