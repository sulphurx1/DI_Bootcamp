const people = ["Greg", "Mary", "Devon", "James"];

people.shift();
console.log(people);

people.splice(2,1,`Jason`);
console.log(people);

people.push(`David`);
console.log(people);

console.log(people[0]);

const copy = people.slice(1);
console.log(copy);

//console.log(indexOf(`Foo`)) // because "Foo" is not in array so indexof cant find the first element in the array

let last = people.slice(3);
console.log(last);

for(const person of people){
    console.log(person)
}

for(const newPerson of people){
    console.log(newPerson)
    if(newPerson === 'Jason'){break}
}