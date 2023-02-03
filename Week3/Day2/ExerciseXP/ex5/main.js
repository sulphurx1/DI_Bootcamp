const form = document.getElementById('myForm');
const radius = document.getElementById('radius');
const volume = document.getElementById('volume');
const btn = document.getElementById('submit');

form.addEventListener('submit', submission);

function submission(event) {
    event.preventDefault();
    const r = Number(radius.value);
    const value1 = (4 / 3) * Math.PI * Math.pow(r, 3);
    console.log(value1)
    volume.value = value1.toPrecision(3);

}

radius.addEventListener('mouseover', () => {console.log('mouse inside radius')
radius.style.fontSize = '10px';
});
radius.addEventListener('mouseout', () => {radius.style.fontSize = '40px'});
btn.addEventListener('click', () => console.log('submit'));

