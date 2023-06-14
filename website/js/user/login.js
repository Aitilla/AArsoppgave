// //Variables
// const username = document.getElementById('username');
// const password = document.getElementById('password');
// const loginBtn = document.getElementById('loginBtn');

// //If button is pressed creates an function
// loginBtn.addEventListener('click', authorise);

// //Created function that send information to api and authorises user if met criteria
// function authorise() {
//     const user = {
//         username: username.value,
//         password: password.value
//     };

//     fetch('http://localhost:5000/loginUser', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(user)
//     })
//     .then((response) => response.json())
//     .then((data) => {
//         if (data.error) {
//             console.log('Wrong username or password');
//         } else {
//             console.log('Login successful');
//             console.log(user);
//             window.location.href = '../../download.html';

//         }
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//     });
// };
