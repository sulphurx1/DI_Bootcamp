// box data
const box = document.getElementById('box');
const target = document.getElementById('target');

box.setAttribute('draggable', 'true');
box.setAttribute('ondragstart', 'onDragStart(event)');

target.setAttribute('ondrop', 'onDrop(event)');
target.setAttribute('ondragover', 'onDragOver(event)');

function onDragStart(event) {
    event.dataTransfer.setData('text', event.target.box);
}

function onDragOver(event) {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
}

function onDrop(event) {
    event.preventDefault();
    
    let data = event.dataTransfer.getData('text/plain');

    event.target.appendChild(box);
}