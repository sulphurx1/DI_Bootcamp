const firstHead = document.getElementsByTagName('h1')[0];
console.log(firstHead.innerHTML);

const lastParagraph = document.getElementsByTagName('article')[0];
lastParagraph.lastElementChild.remove();

const secondHead = document.querySelector('h2');
secondHead.addEventListener('click', change);

const thirdHead = document.querySelector('h3');
thirdHead.addEventListener('click', displayNone);

const btn = document.createElement('button');
lastParagraph.appendChild(btn)
btn.innerHTML = 'Click Me';
btn.addEventListener('click', changeToBold);

firstHead.addEventListener('mouseover', changeSize);

const secondPara = document.querySelectorAll('p')[1]
secondPara.addEventListener('mouseover', textDisappear);

function textDisappear() {
    secondPara.classList.add('fadeout');

}


function change() {
    secondHead.style.backgroundColor = 'red';
}

function displayNone() {
    thirdHead.style.display = 'none';
}

function changeToBold() {
    const allParagraph = lastParagraph.getElementsByTagName('p').length;

    let targetAllParagraph;
    for (let i = 0; i < allParagraph; i++) {
        targetAllParagraph = document.querySelectorAll('p')[i];
        targetAllParagraph.style.fontWeight = 'bold';
    }
}

function randomNumberGenerator() {
    const num = Math.floor(Math.random() * 101);
    return num;
}

function changeSize() {
    const randomNumber = randomNumberGenerator();
    firstHead.style.fontSize = randomNumber + 'px';
}


