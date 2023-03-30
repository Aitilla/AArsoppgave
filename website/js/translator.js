

function englishToMorse(){
    let textEng = document.getElementById("engLetter").value
    console.log(textEng)
    
    fetch('http://localhost:5000/englishToMorse', {
        method: 'POST',
        body: textEng
    }).then(function(response) {
        return response.text();
      }).then(function(data) {
        console.log(data);
        let translatedElement = document.getElementById('engToMorseResult')
        translatedElement.value = data
      });

}

function morseToEnglish(){
    let textMorse = document.getElementById("morseLetter").value
    console.log(textMorse)

    fetch('http://localhost:5000/morseToEng', {
        method: 'POST',
        body: textMorse
    }).then(function(response) {
        return response.text();
      }).then(function(data) {
        console.log(data);
        let translatedElement = document.getElementById('morseToEngResult')
        translatedElement.value = data
      });



}
// store response text as variable
// console log text
// put text where you want to show it

console.log(morseToEnglish)
console.log(morseToEnglish)