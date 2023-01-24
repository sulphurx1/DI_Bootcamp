let x = 1980, y = 1960, year = 2023, older, age1, age2;
if(x > y){
    older = y
    young = x
}

else if(x < y){
    older = x
    young = y
}
else{
    console.log(`They are both the same age`)
}

age1 = (older - year)/2;
age2 = (young - year);
diff = age1 - age2
if(diff > 0){
    console.log(`He still did not reach half the old man's age`)
}
else if(diff < 0){
    date = young + (diff + age2)
    decimal = parseInt(date)
    console.log(decimal)
}
