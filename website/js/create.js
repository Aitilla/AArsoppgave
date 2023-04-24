$(document).ready(function() {
    $('#signup').click(function(event) {
        event.preventDefault();
        var username = $('#createUser').val();
        var password = $('#createPassword').val();
        var data = {
            'username': username,
            'password': password
        };
        $.ajax({
            type: 'POST',
            url: '/create',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                console.log(response.message);
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        });
    });
});
