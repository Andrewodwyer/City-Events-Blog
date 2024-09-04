from django.shortcuts import render, get_object_or_404
from django.views import generic 
from django.http import JsonResponse
from .models import AddEvent # Import the AddEvent model

# Create your views here.
class EventList(generic.ListView): 
    """
    All events in the database are displayed
    This ListView is a generic django view
    Displaying events from the AddEvent model
    """
    queryset = AddEvent.objects.all() # Gets all 'AddEvent' objects from the database and sends them to the template.
    template_name = "event/index.html"
    paginate_by = 6
    # paginate by 6 tells Django to display 6 posts at a time

def addevent_detail(request, slug):
    """
    Display an individual :model:`event.AddEvent`.

    **Context**

    ``addevent``
        An instance of :model:`event.AddEvent`.

    **Template:**

    :template:`event/addevent_detail.html`
    """

    queryset = AddEvent.objects.filter(status=1)
    addevent = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "event/addevent_detail.html",
        {"event": addevent,},
    )

def get_events(request):
    """
    This will retrieve all events from the AddEvent model
    After the loop finishes building the events_list,
    the function returns it as a JSON response using Django JsonResponse
    FullCalendar can use JSON to display events in the calendar
    """
    events = AddEvent.objects.all()  # Fetch events from AddEvent model
    # Create a list of events in the format required by FullCalendar
    events_list = []

    for event in events:
        # The for loop adds title and start(date) to the event_list array for the FullCalendar to use
        events_list.append({
            'title': event.title,
            'start': event.start_date_time.isoformat(),  # FullCalendar expects date in ISO format
            'url': f'/event/{event.slug}/',  # Provide the URL to the event detail page
        })

    return JsonResponse(events_list, safe=False)

def calendar_view(request):
    return render(request, 'event/calendar.html')