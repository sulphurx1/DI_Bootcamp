const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  let x = ' ';
  for (const key in details) {

    x = x + ' ' + key + ' ' + details[key]
  }

  console.log(x);