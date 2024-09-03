from django.shortcuts import render, get_object_or_404
from django.views import generic 
from .models import AddEvent

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
        {"event": addevent},
    )