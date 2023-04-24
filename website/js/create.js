const signup = document.getElementById('signup')
const username = document.getElementById('createUser')
const password = document.getElementById('createPassword')

const mysql = require('mysql')

const connection = mysql.createConnection({
  host: '10.2.1.211',
  port: '3306',
  user: 'rar',
  password: 'raring',
  database: 'aarsoppgave'
});

connection.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL database: ', err);
    return;
  }

  console.log('Successfully connected to MySQL database');
});

// Use the connection to query the database
connection.query('SELECT * FROM users', (error, results, fields) => {
  if (error) {
    console.error('Error querying the database: ', error);
    return;
  }

  console.log('Query results: ', results);
});

// Close the connection when done
connection.end();


signup.addEventListener('click', function(){
    console.log(username.value)
    console.log(password.value)
});