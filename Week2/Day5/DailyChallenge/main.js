let numberofBeers = Number(prompt(`How many beers`));
let numberofBeersTookAway = 1;


while(numberofBeers > 0) {
    const lyrics = makeLyrics(numberofBeers, numberofBeersTookAway);
    console.log(lyrics);
    numberofBeers -= numberofBeersTookAway;
    numberofBeersTookAway++;
}

function makeLyrics(num, counter) {

    const bottleOrBottles = getbottleOrBottles(num, counter);
    const numberofBeersTookAway = getSmaller(counter, num);
    const remainsBottle = getBigger(num - counter, 0);
    const lyrics = `${num} ${bottleOrBottles} of beer on the wall\n` +
                    `${num} ${bottleOrBottles} of beer\n` +
                    `Take ${numberofBeersTookAway} down, pass it around\n` +
                    `${remainsBottle} ${getbottleOrBottles(remainsBottle)} of beer on the wall`;

    return lyrics;
}

function isValueTester(num) {
    return num > 1;
}

function getbottleOrBottles(num) {
    return isValueTester(num) ? `bottles` : `bottle`;
}

function getBigger(a, b) {
    if(a > b) {
        return a;
    }
    else{
        return b;
    }
}

function getSmaller(a, b) {
    if(a < b) {
        return a;
    }
    else {
        return b;
    }
}