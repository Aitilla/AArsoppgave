const mysql = require('mysql');

const connection = mysql.createConnection({
    host: '10.2.1.211',
    port: 3306,
    user: 'rar',
    password: 'raring',
    database: 'aarsoppgave'
});

connection.connect((err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('connected to database');
    }
});

connection.query('SELECT * FROM users', (err, rows, fields) => {
    if (err) {
        console.log(err);
    } else {
        console.log(rows);
    }
});

connection.end();