document.querySelector("#attendance-btn").addEventListener("click", function () {
    const eventId = this.getAttribute("data-event-id");
    
    fetch("/toggle-attendance/", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),  // Ensure you send CSRF token
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
            event_id: eventId
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.attending !== undefined) {
            const attendanceBtn = document.querySelector("#attendance-btn");
            const attendanceCount = document.querySelector("#attendance-count");

            // Update the button text based on the attending status
            if (data.attending) {
                attendanceBtn.textContent = "Unattend";
            } else {
                attendanceBtn.textContent = "Attend";
            }

            // Update the attendance count
            attendanceCount.textContent = `${data.attending_count} attending`;
        } else if (data.error) {
            console.error(data.error);
        }
    })
    .catch(error => console.error("Error:", error));
});

// Utility function to get the CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}