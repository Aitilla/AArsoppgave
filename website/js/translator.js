

function englishToMorse(){
    let textEng = document.getElementById("engLetter").value
    console.log(textEng)
    
    fetch('http://localhost:5000/englishToMorse', {
        method: 'POST',
        body: textEng
    }).then((data) => {
        console.log(data)
    })

}

function morseToEnglish(){
    let textMorse = document.getElementById("morseLetter").value
    console.log(textMorse)

    fetch('http://localhost:5000/morseToEng', {
        method: 'POST',
        body: textMorse
    }).then((data) => {
        console.log(data)
    })
}
// store response text as variable
// console log text
// put text where you want to show it

console.log(morseToEnglish)
console.log(morseToEnglish)