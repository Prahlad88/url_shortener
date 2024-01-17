// register.js

function registerEvent() {
    // Get form data
    var formData = {
        'username': $('#username').val(),
        'email': $('#email').val(),
        'password': $('#password').val(),
        'confirm_password': $('#confirm_password').val(),
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
    };

    // Send AJAX request
    $.ajax({
        type: 'POST',
        url: '{% url "register" %}',
        data: formData,
        success: function (data) {
            // Handle success response (e.g., show a success message)
            console.log('Registration successful:', data);
        },
        error: function (error) {
            // Handle error response (e.g., display error message)
            console.error('Registration failed:', error);
        }
    });
}
