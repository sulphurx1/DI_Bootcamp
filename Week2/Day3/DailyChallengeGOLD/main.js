const numbers = [5,0,9,1,7,4,2,6,3,8];

for(let i = 0; i < numbers.length; i++) {
    //console.log(numbers[i]);
    

    for(let j = 0; j < numbers.length; j++)   {
        //console.log(numbers[j])

        if(numbers[j] > numbers[j + 1]) {
            let temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
        }
    } 
  }
console.log(numbers);