const username = document.getElementById('createUser');
const password = document.getElementById('createPassword');
const button = document.getElementById('signup');
const usernameError = document.getElementById('usernameError');
const passwordError = document.getElementById('passwordError');

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
            if (data.error.includes('Duplicate entry')) {
                usernameError.textContent = 'Username already exists';
            }
            if (data.error.includes('Password must contain at least one number and one character')) {
                passwordError.textContent = 'Password must contain at least one number and one character';
            }
        } else {
            usernameError.textContent = '';
            passwordError.textContent = '';
            console.log(data);
        }
    })
    .catch(error => {
        console.error(error);
    });
});
