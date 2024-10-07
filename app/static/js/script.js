// Example JavaScript to enhance user experience

// Function to show alert messages
function showAlert(message, type) {
    const alertPlaceholder = document.getElementById('alert-placeholder');

    // Create alert div
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.role = 'alert';
    alertDiv.innerText = message;

    // Append alert to placeholder
    alertPlaceholder.appendChild(alertDiv);

    // Automatically remove alert after 3 seconds
    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

