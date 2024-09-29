/*
DOMContentLoaded, function runs only after the HTML document has been loaded
new FullCalendar.Calendar is called to create a new calendar instance,
in the html id=calander.
new FullCalendar.Calendar() is a function provided by the FullCalendar library
{}Options: The calendar is customized using an options object style
The info parameter comes from FullCalendar’s internal event handling system.
FullCalendar automatically passes information about the clicked event to the
function when the user clicks on an event.
When FullCalendar is initialized, it makes an HTTP request to /api/events/ to fetch the events.
This request triggers the get_events view, which sends back the events in JSON format. 
FullCalendar then uses this data to display the events on the calendar.
*/

document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',  // Default view
        events: '/api/events/',  // Fetch events from the specified URL (like Django uses JSON)
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
