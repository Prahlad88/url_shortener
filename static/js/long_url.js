function getLongUrl() {
    var shortUrl = document.getElementById('pasteShortUrl').value;

    // Using AJAX to send a POST request to the server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/shorten/', true);  // Use the appropriate URL from urls.py

    // Include CSRF token in the request header
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    // Set up the data to be sent in the request body
    var data = 'short_url=' + encodeURIComponent(shortUrl);

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                // Update the HTML with the long URL
                var longUrlContainer = document.getElementById('longUrl');
                longUrlContainer.innerHTML = '<p>Long URL: <a href="' + response.long_url + '" target="_blank">' + response.long_url + '</a></p>';
            } else {
                console.error('Failed to retrieve long URL. Server returned status ' + xhr.status);
            }
        }
    };

    // Send the request
    xhr.send(data);
}


// Function to get the CSRF cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
