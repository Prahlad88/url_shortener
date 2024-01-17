function shortenUrl() {
    var originalUrl = document.getElementById('originalUrl').value;

    // Using AJAX to send a POST request to the server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/shorten/', true);  // Use the URL from urls.py

    // Include CSRF token in the request header
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    // Set up the data to be sent in the request body
    var data = 'original_url=' + encodeURIComponent(originalUrl);

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                // Update the HTML with the shortened URL
                var shortenedUrlContainer = document.getElementById('shortenedUrl');
                shortenedUrlContainer.innerHTML = '<p>Shortened URL: <a href="' + response.short_url + '" target="_blank">' + response.short_url + '</a></p>';

                // Update the HTML with the qr code
                var qrEncodedCode = document.getElementById('qrUrl');
                qrEncodedCode.innerHTML = '<p>Scan this QR:<br> <img src="data:image/png;base64,' + response.qr_encoded + '" alt="QR Code"></p>';


                // Create a "Copy" button dynamically
                var copyButton = document.createElement('button');
                copyButton.textContent = 'Copy';
                copyButton.addEventListener('click', function() {
                    copyToClipboard(response.short_url);
                });

                // Append the "Copy" button to the container
                shortenedUrlContainer.appendChild(copyButton);
            } else {
                console.error('Failed to shorten URL. Server returned status ' + xhr.status);
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

// Function to copy text to clipboard
function copyToClipboard(text) {
    var textField = document.createElement('textarea');
    textField.innerText = text;
    document.body.appendChild(textField);
    textField.select();
    document.execCommand('copy');
    textField.remove();

    // Display a message on the page instead of alert
    var messageContainer = document.getElementById('copyMessage');
    messageContainer.textContent = 'Shortened URL copied to clipboard!';
}


