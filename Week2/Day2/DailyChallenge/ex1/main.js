let sentence = prompt(`How did you like the movie?`);

let wordNot = sentence.search(/not/);
console.log(wordNot)
let wordBad = sentence.search(/bad/);

if(wordBad < wordNot){
    alert(`"`+sentence.substring(0,13) + ` good`+(sentence.substring(26)))
}
else{
    alert(`"`+ sentence + `"`);
}