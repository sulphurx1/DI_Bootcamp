const family = {
    first: `Sam`,
    second: `John`,
    third: `Johnny`,
    fourth: `Sarah`,
    fifth: `Dan`
};

for (const keys in family) {
    console.log(keys);

};



for (const values in family) {
    console.log(family[values]);

}