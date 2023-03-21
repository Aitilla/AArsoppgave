

function englishToMorse(){
    // get the input element
    let text = document.getElementById("engLetter").value
    console.log(text)
    // get text from element

    // pass text with request (POST)
    
    fetch('http://localhost:5000/morseToEng', {
        method: 'POST',
        headers: {
            
        }
    })

    // store response text as variable
    // console log text
    // put text where you want to show it
}

function morseToEnglish(text){
    fetch('http://localhost:5000/morseToEng')
}

console.log(morseToEnglish)