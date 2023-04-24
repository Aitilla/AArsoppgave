const express = require('express');
const mysql = require('mysql');

const app = express();

// Create a database connection pool
const pool = mysql.createPool({
  host: '10.2.1.211',
  port: '3306',
  user: 'rar',
  password: 'raring',
  database: 'aarsoppgave'
});

// Define an endpoint for retrieving all users
app.get('/users', (req, res) => {
  pool.query('SELECT * FROM users', (error, results, fields) => {
    if (error) {
      console.error('Error querying the database: ', error);
      res.status(500).send('Internal server error');
      return;
    }

    res.json(results);
  });
});

// Define an endpoint for retrieving a specific user
app.get('/users/:id', (req, res) => {
  const userId = req.params.id;

  pool.query('SELECT * FROM users WHERE id = ?', [userId], (error, results, fields) => {
    if (error) {
      console.error('Error querying the database: ', error);
      res.status(500).send('Internal server error');
      return;
    }

    if (results.length === 0) {
      res.status(404).send('User not found');
      return;
    }

    res.json(results[0]);
  });
});

// Start the server
app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
