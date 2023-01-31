const planetsArray = [
    {name: `Earth`, moons: 1},
    {name: `Mars`, moons: 2}, 
    {name: `Venus`, moons: 0},
    {name: `Mercury`, moons: 0}, 
    {name: `Uranus`, moons: 0}, 
    {name: `Jupiter`, moons: 66},
    {name: `Neptune`, moons: 13},
    {name: `Saturn`, moons: 27}
];

console.log(planetsArray);

const section = document.querySelector(`.listPlanets`)
console.log(section)
const planetElements = planetsArray.map(name => {
    const element = document.createElement(`div`)
    document.body.appendChild(element)
    element.classList.add(`planet`)
    element.classList.add(name.name.toLowerCase())
    for(let i = 0; i < name.moons; i++) {
        const newMoon = document.createElement(`div`)
        newMoon.classList.add(`moon`)
        element.appendChild(newMoon)
        newMoon.style.margin = `calc(5px * ${i}) 0 0 calc(20px * ${i})`;
    }       

    section.appendChild(element)
    return element;
    
})








