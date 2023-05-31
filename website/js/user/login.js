const username = document.getElementById('username');
const password = document.getElementById('password');
const loginBtn = document.getElementById('loginBtn');

loginBtn.addEventListener('click', function() {
    const user = {
        username: username.value,
        password: password.value
    };

    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.error) {
            console.log('Wrong username or password');
        } else {
            console.log('Login successful');
            console.log(user);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
