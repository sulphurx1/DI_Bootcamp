const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let x = ' ';

for(const name of names.sort()) {
    console.log(name);
    x += name[0];
}

console.log(x);