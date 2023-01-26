<?php
    if(isset($_POST['submit'])){
        $username = $_POST['username']
        $password = $_POST['password']

        $dbc = mysqli_connect('localhost', 'root', '', 'mydb')
            or die('Error connection to MySQØ server.');
        
        
        $query = "SELECT username, password from users where username='$username' and password='$password'"



        $result = mysqli_query($dbc, $query)
            or die('Error querying database.')



        msqli_close($dbc);



        if($result->num_rows > 0){
            header('location: success.html')
        }else{
            header('location: failure.html')
        }

    }

