// Timeout function for messaging
setTimeout(function () {
    let messages = document.getElementById('msg');

    if (messages) {
        let alert = new bootstrap.Alert(messages);
        
        if (alert) {
            alert.close();
        }
    }
}, 3000);