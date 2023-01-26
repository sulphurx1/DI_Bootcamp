let input = prompt(`Please enter words with comma`) ;
arr = input.split(`,`);

const longestString = strings => {
  let longest = strings[0].length;
  strings.forEach(str => {
    str.length >=  longest ? longest = str.length : longest;
  });
  return longest;
}

const createSpacesNeeded = spacesNeeded => {
  let spaces = '';
  for(let i = 0; i < spacesNeeded; i++) {
    if(i < spacesNeeded) {
      spaces = spaces + ' ';
    }
  }
  return spaces;
}
console.log('*' * longestString);hell

const stringsRecFrame = strings => {
  const longestStr = longestString(strings);

  
  let newLine = '\n';
  strings.forEach(str => {
    if(str.length === longestStr) {
      console.log(`*${str}* ${newLine}`);
    } else {
      let spacesNeeded = longestStr - str.length;
      
      let spaces = createSpacesNeeded(spacesNeeded);
    
      console.log(`*${str}${spaces}* ${newLine}`);
    }
  });
  console.log('*' * longestString);
}

console.log(stringsRecFrame(arr))