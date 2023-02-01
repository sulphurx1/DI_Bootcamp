let newDiv = document.getElementById('navBar')

newDiv.setAttribute('id', 'socialNetworkNavigation');

const li = document.createElement('li')

const ul = document.querySelector('ul')

ul.appendChild(li)

const logout = document.createTextNode('Logout')

li.appendChild(logout)

console.log(ul.lastElementChild.textContent);

console.log(ul.firstChild.textContent);