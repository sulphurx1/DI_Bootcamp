let timer;

function myMove() {
    timer = setInterval(moving, 1)
}



function moving() {
    const block = document.getElementById('animate');
    let pos = block.getAttribute('data-pos')
    pos = parseInt(pos);
    pos = pos > 0 ? pos : 0;
    pos ++;
    pos = pos > 350 ? 350 : pos
    block.style.left = pos + 'px';
    block.setAttribute('data-pos', pos)
    
    if(pos >= 350) {
        clearInterval(timer);
    }
}


