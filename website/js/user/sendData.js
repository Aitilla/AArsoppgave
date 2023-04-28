const username = document.getElementById('createUser');
const password = document.getElementById('createPassword');
const button = document.getElementById('signup');
const errorMessage = document.getElementById('errorMessage');

button.addEventListener('click', function(){
    const data = {
        username: username.value, 
        password: password.value
    };
    fetch('http://localhost:5000/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        // if (response.ok) {
            return response.json();
        // } else if (response.status === 400) {
        //     return response.text().then(msg => {
        //         throw new Error("Username or password is has incorrect input");
        //     });
        // } else {
        //     throw new Error('Either username is already taken or password is not containing atleast a letter and a number.');
        // }
    // }).then(response => {
    //     console.log(response);
    //     errorMessage.textContent = 'User created successfully';
    // 
    }).catch(error => {
        console.error(error);
        errorMessage.textContent = error.message;
    });
});

// username.addEventListener('input', function() {
//     errorMessage.textContent = '';
// });

// password.addEventListener('input', function() {
//     errorMessage.textContent = '';
// });
