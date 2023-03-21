fetch('database')
  .then(response => response.json())
  .then(data => {
    // Do something with the data returned by the API
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
