function isDivisible(divisor) {
    let sum = 0;
    for(let i = 0; i <= 500; i++) {
        if(i % divisor === 0) {
            console.log(`list of divisible: ` + i);
            sum += i;
        }
    }

    console.log(`sum of divisible of `+`${divisor}` + ` is ` + `${sum}`);
}

isDivisible(23);
isDivisible(3);