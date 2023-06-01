//Variables
const username = document.getElementById('createUser');
const password = document.getElementById('createPassword');
const button = document.getElementById('signup');
var errorMessage = document.getElementById('errorMessage');

//When pressed creates an function that sends information to api and creates user if met criteria.
button.addEventListener('click', function() {
    const data = {
        username: username.value,
        password: password.value
    };
    fetch('http://localhost:5000/createUser', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            if (data.error.includes('Duplicate entry') && data.error.includes('Password must contain at least one number and one character')) {
                errorMessage.innerHTML('Username already exists or password does not meet the criteria')
            }
        } else {
            console.log(data);
        }
    })
    .catch(error => {
        console.error(error);
        errorMessage = 'noProblem'
        console.log(errorMessage)
    });
});
