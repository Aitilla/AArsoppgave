<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/style.css">
    <title>PHP innlogging</title>
</head>
<body>
    
    <p>Login</p>
    <form method="post" action="user.html">
        <label for="username">Username</label>
        <input type="text" name="username">
        <label for="password">Password</label>
        <input type="password" name="password">

        <input type="submit" value="Login" name="submit">
    </form>
    <p><a href="../registration.php">Create new user</a></p>

<?php
    if(isset($_POST['submit'])){
        $username = $_POST['username'];
        $password = $_POST['password'];

        $dbc = mysqli_connect('localhost', 'root', '', 'mydb')
            or die('Error connection to MySQØ server.');
        
        
        $query = "SELECT username, password from users where username='$username' and password='$password'";



        $result = mysqli_query($dbc, $query)
            or die('Error querying database.');



        msqli_close($dbc);



        if($result->num_rows > 0){
            header('location: success.html');
        }else{
            header('location: failure.html');
        }

    }
?>

</body>
</html>