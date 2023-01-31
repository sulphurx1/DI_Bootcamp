function changeEnough(itemPrice, amountOfChange) {
    const sum = summation(amountOfChange)

    if (sum > itemPrice) {
        
        console.log(`YES! YOU CAN BUY IT`);

        return true
    }
    else {

        console.log(`NO!You are poor m8`)

        return false
    }

}

const coins = {
    quarters: 0.25,
    dimes: 0.10,
    nickel: 0.05,
    penny: 0.01
}

function summation(arr) {
    let sum = 0;

    for(i = 0; i < arr.length; i++) {

        let coinValue;
        const theNumberOfCoins = arr[i];

        if(i === 0){coinValue = coins.quarters}
        else if(i === 1){coinValue = coins.dimes}
        else if(i === 2){coinValue = coins.nickel}
        else if(i === 3){coinValue = coins.penny}

        sum += (theNumberOfCoins * coinValue);
    }
    
    return sum
}

changeEnough(4.25, [25, 20, 5, 0])