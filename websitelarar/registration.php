<?php
    if(isset($_POST['submit'])){
        $username = $_POST['username']
        $password = $_POST['password']

        $dbc = mysqli_connect('localhost', 'root', '', 'mydb')
            or die('Error connection to MySQØ server.');
        
        
        $query = "INSERT INTO users VALUES ('$username', '$password')";



        $result = mysqli_query($dbc, $query)
            or die('Error querying database.')



        msqli_close($dbc);



        if($result){
            echo "Thank you for registering. Press <a href='login.php'> to login"
        }else{
            echo "Something went wrong, please try again later"
        }

    }