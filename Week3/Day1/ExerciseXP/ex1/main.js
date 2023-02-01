let container = document.getElementById('container').innerHTML;
console.log(container);


let name1 = document.getElementsByTagName('li')[1].innerHTML;
console.log(name1);
name1 = document.getElementsByTagName('li')[1].textContent = `Richard`;
console.log(name1);

const lists = document.querySelectorAll('.list')
lists.forEach(list => list.firstElementChild.textContent = 'David');

lists[1].children[1].remove()

// need to fix the loop 
// for(let i = 0; i < lists.length; i++) {
//     for(let j = 0; j < lists[i].children.length; j++) {
//         if(lists === 'Sarah') {
//             lists[i].children[j].remove()
//         }
//     }
// }

lists.forEach(list => list.classList.add('student_list'))

const firstUl = document.querySelector('ul.list.student_list')
firstUl.classList.add('university', 'attendance')