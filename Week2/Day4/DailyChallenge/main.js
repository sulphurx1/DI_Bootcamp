let input = prompt(`Please enter words with commas`) ;
arr = input.split(`,`);

let arrayTrim = arr.map(elements => {
  return elements.trim();
});

let longest = arrayTrim[0].length;
arrayTrim.forEach(str => {
  str.length >= longest ? longest = str.length : longest;
  return longest;
});

const createSpacesNeeded = spacesNeeded => {
  let spaces = ``;
  for(let i = 0; i < spacesNeeded; i++) {
    if(i < spacesNeeded) {
      spaces += ` `;
    }
  }
  return  spaces;
}

console.log(`**`+`*`.repeat(longest)+`**`);

for(const word of arrayTrim) {
  if(word.length === longest) {
    console.log(`*`+` `+`${word}`+` `+`*`);
  }
  else{
    let spacesNeeded = longest - word.length;
    spaces = createSpacesNeeded(spacesNeeded);
    console.log(`*`+` `+`${word}`+`${spaces}`+` `+`*`)
  }
}
console.log(`**`+`*`.repeat(longest)+`**`);