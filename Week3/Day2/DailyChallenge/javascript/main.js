// Lit it button event
const onSubmission = document.getElementById('lib-button');
onSubmission.addEventListener('click', onClick, true);

// creating class id
const btn = document.createElement('button');
btn.innerHTML = 'Shuffle';
btn.classList.add('shuffle');
document.body.appendChild(btn);

// shuffle button event
const shuffleButton = document.getElementsByClassName('shuffle');
shuffleButton[0].addEventListener('click', shuffleStories, true);

// for random number generator
const low = 1, high = 3;



// get values as object
function getValues() {
    const noun = document.getElementById('noun').value;
    const adjective = document.getElementById('adjective').value;
    const person = document.getElementById('person').value;
    const verb = document.getElementById('verb').value;
    const place = document.getElementById('place').value;
    return{
        noun: noun,
        adjective: adjective,
        person: person,
        verb: verb,
        place: place
    };
    
}

function appendGeneratedStory(story) {
    const paragraph = document.getElementById('story')
    paragraph.innerText = story;
}

function generatedStory(noun, adjective, person, verb, place) {
    return `My ${adjective} ${noun} ${verb} ${person} and ${place}`
}

function generatedStory1(noun, adjective, person, verb, place) {
    return `She ${verb} ${adjective} ${person} ${noun} at ${place}`
}

function generatedStory2(noun, adjective, person, verb, place) {
    return `My Radomness ${verb} ${person} ${noun} no limits ${adjective} ${place}`
}

function generatedStory3(noun, adjective, person, verb, place) {
    return `How ${adjective} ${verb} ${noun} ${place} ${verb} ${person}`
}

// Lib it button function
function onClick(event) {
    event.preventDefault();

    //getting values from input
    const formValues = getValues()
    const noun = formValues.noun
    const adjective = formValues.adjective
    const person = formValues.person
    const verb = formValues.verb
    const place = formValues.place

    // condition if one space is left unfilled
    if(noun == '' || adjective == '' || person == '' || verb == '' || place == ''){
    return
    }

    // just gave up to try to move this
    let story = generatedStory(noun, adjective, person, verb, place)
    appendGeneratedStory(story)
}

// shuffle button function
function shuffleStories() {

    //getting values from input
    const formValues = getValues()
    const noun = formValues.noun
    const adjective = formValues.adjective
    const person = formValues.person
    const verb = formValues.verb
    const place = formValues.place

    if (randomNumberGenerator === 1) {
        story = generatedStory1(noun, adjective, person, verb, place)
    }
    else if(randomNumberGenerator === 2) {
        story = generatedStory2(noun, adjective, person, verb, place)
    }
    else{
        story = generatedStory3(noun, adjective, person, verb, place)
    }
    
    // just gave up to try to move this
    let story = generatedStory(noun, adjective, person, verb, place)
    appendGeneratedStory(story)
}


// generating random number from Math.floor()
function randomNumberGenerator(low, high) {
    return Math.floor(Math.random() * (high - low + 1) + low)
}






