const express = require('express');
const path = require('path');

const app = express();
const PORT = 8080;

app.use('/', (req, res, next) => {
    console.log(`noen som kobla seg til`);
    next();
})

app.use('/', express.static(path.join('..', 'website')));

app.listen(PORT, () => {
    console.log(`express running on port ${PORT}`);
})