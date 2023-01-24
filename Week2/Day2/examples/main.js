
debugger;
//let raining = false, really = false, value;

//let str = 'raining today';

//value = ((raining || really) && str) || 'xyz';

//value = (raining || really) ? str : 'xyz';

//console.log(value);
 //let person = {
 //   name: 'Bob',
 //   age: 18,
 //    job: false
 //};

 //console.log(person);


//  let age = prompt(`What is your age?`);

//  if(age < 18){
//     alert('"Sorry, you are too young to drive this car. Powering off');
//  }
//  else if(age === 18){
//     alert('"Congratulations on your first year of driving. Enjoy the ride!')
//  }
//  else{
//     alert('"Powering On. Enjoy the ride!"')
//  }

//  let person = {
//     firstName: 'John',
//     lastName: 'Doe',
//     age: 50,
//     eyeColor: 'blue'
//  };

//  // person.age = undefined;
//  delete person.age; 

//  console.log(person);
//  console.log(person.firstName);
//  console.log(person['firstName']);
//  console.log(person.age);


// let info = {
//     username: "username",
//     password: 4567
// };
// console.log(info);

// let database = [
//     info
// ];
// console.log(database);

// let newsfeed = [
//     {
//         username: "username",
//         password: 4567
//     },
//     {
//         username: "username",
//         password: 4567
//     },
//     {
//         username: "username",
//         password: 4567
//     }
// ]
// console.log(newsfeed);

// console.log(typeof(newsfeed)) // even it is an array js consider it as an object

let str = `Happy Birthday`;
// let pattern = new RegExp(`birthday`, i);
let pattern = /birthday/i;

let result = str.match(pattern);

console.log(result)

if(result){
    console.log('Yes')
}
else {
    console.log('No')
};


let regex = /^.+@.+\..+$/;
console.log(regex.test('johndoe@gmail.com'));