const express = require('express');
const path = require('path');

const app = express();
const PORT = 8080;

app.use('/', express.static(path.join('..', 'website')));

app.listen(PORT, () => {
    console.log(`express running on port ${PORT}`);
})