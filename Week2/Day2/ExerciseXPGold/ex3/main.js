let input = prompt(`Please enter a verb`);

if(input.length < 3){
    alert(input)
}
else if(input.indexOf(`ing`) == -1){
    alert(input+`ing`)
}

else if(input.indexOf(`ly`) == -1){
    alert(input + `ly`)
}
