document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',  // Default view
        events: '/api/events/',  // Fetch events from the backend
        headerToolbar: {
            left: 'prev',
            center: 'title',
            right: 'next'
        },
        eventClick: function(info) {
            // eventClick redirect to the event detail page, by changing the current href
            window.location.href = info.event.url; 
            // url in the info.event.url comes from the get_events function in views.py
        }
    });

    calendar.render();
});
