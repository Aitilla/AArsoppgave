const express = require('express');

const app = express();
const PORT = 8080;

app.get('/', (req, res) => {
    res.end("hello world")
})

app.listen(PORT, () => {
    console.log(`express running on port ${PORT}`);
})