document.addEventListener('DOMContentLoaded', function() {
    const attendanceForm = document.getElementById('attendance-form');
    const attendanceIcon = document.getElementById('attendance-icon');
    const attendanceText = document.getElementById('attendance-text');
    const attendanceCount = document.getElementById('attendance-count');
    const attendanceContainer = document.getElementById('attendance-container');

    attendanceContainer.addEventListener('click', function() {
        const formData = new FormData(attendanceForm);

        fetch(attendanceForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.user_attending) {
                attendanceIcon.classList.remove('icon-primary');
                attendanceIcon.classList.add('icon-success');
                attendanceText.classList.remove('text-primary1');
                attendanceText.classList.add('text-success1');
                attendanceText.textContent = "You're going!";
            } else {
                attendanceIcon.classList.remove('icon-success');
                attendanceIcon.classList.add('icon-primary');
                attendanceText.classList.remove('text-success1');
                attendanceText.classList.add('text-primary1');
                attendanceText.textContent = 'Going?';
            }
            attendanceCount.textContent = `${data.attending_count} Attending`;
        })
        .catch(error => console.error('Error:', error));
    });
});
