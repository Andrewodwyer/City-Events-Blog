const attendanceForm = document.getElementById('attendance-form');
const attendanceButton = document.getElementById('attendance-btn');
const attendanceCount = document.getElementById('attendance-count');

attendanceForm.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission

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
    // Update button text and attendance count based on response
    attendanceButton.textContent = data.user_attending ? 'Unattend' : 'Attend';
    attendanceCount.textContent = `${data.attending_count} attending`;

    // Update the button class based on the attending status
    if (data.user_attending) {
        attendanceButton.classList.remove('btn-primary');
        attendanceButton.classList.add('btn-success');
        } else {
        attendanceButton.classList.remove('btn-success');
        attendanceButton.classList.add('btn-primary');
        }
  })
  .catch(error => console.error('Error:', error));
});