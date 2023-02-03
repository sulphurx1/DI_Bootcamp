const form = document.getElementById('myForm');
const radius = document.getElementById('radius');
const volume = document.getElementById('volume');

form.addEventListener('submit', submission);

function submission(event) {
    event.preventDefault();
    const r = Number(radius.value);
    if(Number.isNaN(r)) {
        return;
    }
    const value1 = (4 / 3) * Math.PI * Math.pow(r, 3);
    console.log(value1)
    volume.value = value1.toPrecision(3);

}