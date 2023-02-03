let allBoldItems;

function getBolditems() {
    allBoldItems = document.getElementsByTagName('strong');
}
function highlight() {
    getBolditems()
    for (const boldItem of allBoldItems) {
        boldItem.style.backgroundColor = 'blue'
    }
}

function returnNormal() {
    getBolditems()
    for (const boldItem of allBoldItems) {
        boldItem.style.backgroundColor = 'transparent'
    }
}

const para = document.querySelector('p');

para.addEventListener('mouseover', highlight);
para.addEventListener('mouseout', returnNormal);