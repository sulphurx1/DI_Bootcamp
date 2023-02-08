
const form = document.getElementsByTagName('form')[0];
form.addEventListener('submit', handleSubmit);

const tasks = [];

function handleSubmit(event) {
    event.preventDefault();
    const task = formData.get('task');

    if(task === '') {
        return;
    }

    addTask(tasks);
    tasks.push(task);
    form.reset();
}

const ul = document.createTextNode('ul');
const list = document.getElementsByName('list-tasks');
list.appendChild(ul);

function addTask(tasks) {
    const task = tasks[0];
    const li = document.createTextNode('li');
    li.innerText = task;
    ul.appendChild(li);
}

function printTask(task) {
    console.log('task')
}
tasks.forEach(printTask);

