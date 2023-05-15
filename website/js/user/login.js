const username = document.getElementById('username');
const password = document.getElementById('password');
const loginBtn = document.getElementById('loginBtn');

loginBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const user = {
        username: username.value,
        password: password.value
    };
    fetch('/user/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    }).then((response) => {
        if (response.status === 200) {
            window.location.href = '/user/profile';
        } else {
            alert('Invalid username or password');
        }
    });
});