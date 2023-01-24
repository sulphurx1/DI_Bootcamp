let x = prompt(`Please enter a word`);

x = x.replace(/[a]/gi, '1');
x = x.replace(/[e]/gi, '2');
x = x.replace(/[i]/gi, '3');
x = x.replace(/[o]/gi, '4');
x = x.replace(/[u]/gi, '5');

alert(x);