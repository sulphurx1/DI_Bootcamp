setTimeout(alertSayHello, 2000);

const body = document.getElementById('container');

let timer = setInterval(printInHelloWorld, 2000);

const btn = document.getElementById('clear');
btn.addEventListener('click', removeIt);

function alertSayHello() {
    alert('Hello World!');
}
function printInHelloWorld() {
    const text = document.createElement('p');
    body.appendChild(text);
    text.innerHTML = 'Hello World!';
    noMoreThan5Para();
}
function stopIt() {
    clearInterval(timer); 
    removeIt();
}
function noMoreThan5Para() {
    const allChildren = body.getElementsByTagName('p').length;
    console.log(allChildren)
    if(allChildren > 5) {
        stopIt();
    }
}
function removeIt() {
    const e = document.querySelector('p:last-child');
    e.remove();
}


