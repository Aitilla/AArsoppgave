

function englishToMorse(){
    // get the input element
    let textEng = document.getElementById("engLetter").value
    console.log(textEng)
    // get text from element

    // pass text with request (POST)
    
    fetch('http://localhost:5000/englishToMorse', {
        method: 'POST',
        body: textEng
        
    }).then((data) => {
        console.log(data)
    })

    // store response text as variable
    // console log text
    // put text where you want to show it
}

function morseToEnglish(){
    let text = document.getElementById("morseLetter").value
    console.log(text)

    fetch('http://localhost:5000/morseToEng', {
        method: 'POST',
        body: textMorse
    }).then((data) => {
        console.log(data)
    })
}

console.log(morseToEnglish)