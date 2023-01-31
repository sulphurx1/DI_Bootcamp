function calcualteTip() {
    let bill = prompt(`What is the amount of bill?`);

    if(bill < 50) {
        console.log(`bill: ` + bill + ` + tip: ` + (0.2 * bill))
    }

    else if(bill >= 50 && bill <= 200) {
        console.log(`bill: ` + bill + ` + tip: ` + (0.15 * bill) )
    }
    else{
        console.log(`bill: ` + bill + ` + tip: ` + (0.1 * bill) )
    }
}

calcualteTip();