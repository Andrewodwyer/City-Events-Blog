document.addEventListener("DOMContentLoaded", function () {
    // DOMContentLoaded event ensures that the DOM is fully loaded before executing the JS
    // A listener is attached to the attendance-btn in the addevent_detail.html
    const attendanceBtn = document.getElementById("attendance-btn");

    if (attendanceBtn) {
        attendanceBtn.addEventListener("click", function () {
            const eventId = this.getAttribute("data-event-id");
            
            // Perform AJAX request to toggle attendance, POST request to send data to the server
            fetch("/toggle-attendance/", {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),  // Include the CSRF token for security
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: new URLSearchParams({
                    "event_id": eventId
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.attending !== undefined) {
                    // Update the button text based on the attendance state
                    attendanceBtn.textContent = data.attending ? "Unattend" : "Attend";
                    
                    // Update the count of people attending
                    const attendanceCountElement = document.getElementById("attendance-count");
                    attendanceCountElement.textContent = `${data.attending_count} attending`;
                }
            })
            .catch(error => console.error("Error:", error));
        });
    }
});

// Function to get the CSRF token from the cookies
function getCSRFToken() {
    let cookieValue = null;
    const cookies = document.cookie.split(";");

    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith("csrftoken=")) {
            cookieValue = cookie.substring("csrftoken=".length);
            break;
        }
    }

    return cookieValue;
}